# Sign-Language-Recognition-using-LSTM-model

The project “Sign-Language-Recognition-using-LSTM-model” is a deep learning model designed to recognize sign language gestures. It uses Long Short Term Memory (LSTM) neural networks for training and testing.

The LSTM model is trained on a "sequential_8" model with 8 layers and 4 dense layers. The model is compiled with the ‘Adam’ optimizer, ‘categorical_crossentropy’ loss, and ‘accuracy’ metrics.

The project begins by using OpenCV with MediaPipe Holistic to identify key markers of the poser. The identified keypoints are then collected and stored to be trained on later.

This project aims to help children and adult with hearing loss.

## Dataset

The model in this project has been trained on a custom dataset. This dataset was created and curated by us, and it includes various sign language gestures. Each gesture in the dataset is labeled as 'zero','one','two','three','four','five','six','seven','eight','nine'.

## Accuracy

### LSTM:

train accuracy: 96.19%

test/val accuracy: 90%

### VGG16:

Train: 89%

test/Val: 79%

### ResNet:

Train: 91%

test/val: 78%


## Model Summary

### LSTM Model
The LSTM model is trained on a "sequential_8" model with 8 layers and 4 dense layers. The model is compiled with the ‘Adam’ optimizer, ‘categorical_crossentropy’ loss, and ‘accuracy’ metrics.

![Screenshot 2023-12-09 132837](https://github.com/rahuln2002/Sign-Language-Recognition-using-LSTM-model/assets/99525324/ac2a79b4-dc30-4381-93a1-041bb9aba8e7)

### ResNet
The ResNet model is trained on a "model_4" model with 75 layers and 2 dense layers. The model is compiled with the ‘Adam’ optimizer, ‘categorical_crossentropy’ loss, and ‘accuracy’ metrics.

![Screenshot 2023-12-09 161734](https://github.com/rahuln2002/Sign-Language-Recognition-using-LSTM-model/assets/99525324/0b5ecdbc-8cce-4b82-bd59-edf12e7dcfff)

![Screenshot 2023-12-09 161744](https://github.com/rahuln2002/Sign-Language-Recognition-using-LSTM-model/assets/99525324/31ce7cae-31ea-4896-8e48-b8e94cfe2926)

![Screenshot 2023-12-09 161755](https://github.com/rahuln2002/Sign-Language-Recognition-using-LSTM-model/assets/99525324/9477538c-dbe0-4e82-8ec5-d5f1cedbe766)

![Screenshot 2023-12-09 161807](https://github.com/rahuln2002/Sign-Language-Recognition-using-LSTM-model/assets/99525324/1066e70a-73e1-4393-b8f8-484479e005f2)

### VGG16
The VGG16 model is trained on a "sequential_2" model with 29 layers and 3 dense layers. The model is compiled with the ‘Adam’ optimizer, ‘categorical_crossentropy’ loss, and ‘accuracy’ metrics.

![Screenshot 2023-12-09 162111](https://github.com/rahuln2002/Sign-Language-Recognition-using-LSTM-model/assets/99525324/56bee45c-e7e8-4b95-957a-5834e54b4369)

![Screenshot 2023-12-09 162123](https://github.com/rahuln2002/Sign-Language-Recognition-using-LSTM-model/assets/99525324/31642b37-f6ee-4d4e-831a-cdd7c397acd0)



