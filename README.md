# Sign-Language-Recognition-using-LSTM-model

The project “Sign-Language-Recognition-using-LSTM-model” is a deep learning model designed to recognize sign language gestures. It uses Long Short Term Memory (LSTM) neural networks for training and testing.

The LSTM model is trained on a "sequential" model with 14 layers and 4 dense layers. The model is compiled with the ‘Adam’ optimizer, ‘categorical_crossentropy’ loss, and ‘accuracy’ metrics.

The project begins by using OpenCV with MediaPipe Holistic to identify key markers of the poser. The identified keypoints are then collected and stored to be trained on later.

This project aims to help children and adult with hearing loss.

## Dataset

The model in this project has been trained on a custom dataset. This dataset was created and curated by us, and it includes various sign language gestures. Each gesture in the dataset is labeled as 'zero','one','two','three','four','five','six','seven','eight','nine'.

## Accuracy

### LSTM:

Train Accuracy: 94.28%

Test Accuracy: 91.50%

### VGG16:

Train Accuracy: 88.18%

Test Accuracy: 83.33%

### ResNet:

Train Accuracy: 87.43% 

Test Accuracy: 77.50%


## Model Summary

### LSTM Model
The LSTM model is trained on a "sequential_8" model with 14 layers and 4 dense layers. The model is compiled with the ‘Adam’ optimizer, ‘categorical_crossentropy’ loss, and ‘accuracy’ metrics.

![Screenshot 2023-12-10 195007](https://github.com/rahuln2002/Sign-Language-Recognition-using-LSTM-model/assets/99525324/9630fff4-609b-44eb-a42f-bfba33ecc460)

### ResNet
The ResNet model is trained on a "model" model with 75 layers and 2 dense layers. The model is compiled with the ‘Adam’ optimizer, ‘categorical_crossentropy’ loss, and ‘accuracy’ metrics.

![Screenshot 2023-12-09 163200](https://github.com/rahuln2002/Sign-Language-Recognition-using-LSTM-model/assets/99525324/1a1d80d3-7f6d-4bd7-9946-9a2d71ff7054)

![Screenshot 2023-12-09 163221](https://github.com/rahuln2002/Sign-Language-Recognition-using-LSTM-model/assets/99525324/de672cf4-80e3-4c59-b8f9-8ec18a2aaa4b)

![Screenshot 2023-12-09 163238](https://github.com/rahuln2002/Sign-Language-Recognition-using-LSTM-model/assets/99525324/55c1d35d-737b-4402-bf6d-066dce86afe4)

![Screenshot 2023-12-09 163257](https://github.com/rahuln2002/Sign-Language-Recognition-using-LSTM-model/assets/99525324/ec3a5f19-1de1-47e2-91d0-c980b88015b5)


### VGG16
The VGG16 model is trained on a "sequential" model with 29 layers and 3 dense layers. The model is compiled with the ‘Adam’ optimizer, ‘categorical_crossentropy’ loss, and ‘accuracy’ metrics.

![Screenshot 2023-12-09 163509](https://github.com/rahuln2002/Sign-Language-Recognition-using-LSTM-model/assets/99525324/6819810c-0a3d-46a2-bb9e-9186a2e1ddca)

![Screenshot 2023-12-09 163529](https://github.com/rahuln2002/Sign-Language-Recognition-using-LSTM-model/assets/99525324/7ff0d1b8-72c4-42c0-a520-0fd9695d821f)



