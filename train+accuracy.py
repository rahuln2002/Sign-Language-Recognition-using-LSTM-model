import os
import numpy as np
import tensorflow as tf
from keras.models import Sequential
from keras.layers import LSTM, Dense, Flatten, Dropout
from keras.utils import to_categorical
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from keras.callbacks import TensorBoard

# 1.Train
DATA_PATH = os.path.join('dataset')
actions = np.array(['one', 'two','three', 'four', 'five', 'six', 'seven', 'eight', 'nine'])

sequence_length = 100

label_map = {label:num for num, label in enumerate(actions)}

sequences, labels = [], []
for action in actions:
    for sequence in np.array(os.listdir(os.path.join(DATA_PATH, action))).astype(int):
        window = []
        for frame_num in range(sequence_length):
            res = np.load(os.path.join(DATA_PATH, action, str(sequence), "{}.npy".format(frame_num)))
            window.append(res)
        sequences.append(window)
        labels.append(label_map[action])

x = np.array(sequences)

y = to_categorical(labels).astype(int)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.30)

log_dir = os.path.join('Logs')
callback = TensorBoard(log_dir=log_dir)
ACCURACY_THRESHOLD = 0.95
class myCallback(tf.keras.callbacks.Callback): 
    def on_epoch_end(self, epoch, logs={}): 
        if(logs.get('accuracy') > ACCURACY_THRESHOLD):   
            print("\nReached %2.2f%% accuracy, so stopping training!!" %(ACCURACY_THRESHOLD*100))   
            self.model.stop_training = True

tb_callback = myCallback()

model = Sequential()
model.add(LSTM(16, return_sequences=True, activation='relu', input_shape=(100, 126)))
model.add(LSTM(32, return_sequences=True, activation='relu'))
model.add(Dropout(0.2))
model.add(LSTM(16, return_sequences=True, activation='relu'))
model.add(Dropout(0.2))
model.add(LSTM(16, return_sequences=True, activation='relu'))
model.add(Dropout(0.2))
model.add(LSTM(8, return_sequences=True, activation='relu'))
model.add(Dropout(0.2))

model.add(Flatten())

model.add(Dense(2048, activation='relu', kernel_initializer='he_uniform'))
model.add(Dense(1536, activation='relu'))
model.add(Dense(1024, activation='relu'))

model.add(Dense(actions.shape[0], activation='softmax'))

tf.keras.optimizers.Adam(learning_rate=0.001, beta_1=0.9, beta_2=0.999, epsilon=1e-07, amsgrad=False, name="Adam")

model.compile(optimizer= 'Adam', loss='categorical_crossentropy', metrics=['accuracy'])

model.fit(x_train, y_train, validation_data=(x_test, y_test), epochs=300, batch_size=256, use_multiprocessing = True, callbacks=[tb_callback, callback])

model.summary()

res = model.predict(x_test)

model.save('Number_Model3.h5')

model.load_weights('Number_Model3.h5')

# 2. Test and Train Accuracy
yhat = model.predict(x_train)
ytrue = np.argmax(y_train, axis=1).tolist()
yhat = np.argmax(yhat, axis=1).tolist()

print("Train Accuracy :-> ")
print(accuracy_score(ytrue, yhat)*100)

yhat = model.predict(x_test)
ytrue = np.argmax(y_test, axis=1).tolist()
yhat = np.argmax(yhat, axis=1).tolist()

print("Test Accuracy :-> ")
print(accuracy_score(ytrue, yhat)*100)