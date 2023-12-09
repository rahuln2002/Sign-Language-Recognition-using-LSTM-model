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
![Screenshot 2023-12-09 132837](https://github.com/rahuln2002/Sign-Language-Recognition-using-LSTM-model/assets/99525324/ac2a79b4-dc30-4381-93a1-041bb9aba8e7)

