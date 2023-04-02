import os
import tensorflow as tf
import numpy as np
from keras.utils import to_categorical
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

model = tf.keras.models.load_model("Number_Model3.h5")

model.summary()

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

matrix = tf.math.confusion_matrix(labels, sequences)

print(matrix)

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