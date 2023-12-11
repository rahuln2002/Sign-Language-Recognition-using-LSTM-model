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
The LSTM model is trained on a "sequential" model with 14 layers and 4 dense layers. The model is compiled with the ‘Adam’ optimizer, ‘categorical_crossentropy’ loss, and ‘accuracy’ metrics.

![Screenshot 2023-12-10 195007](https://github.com/rahuln2002/Sign-Language-Recognition-using-LSTM-model/assets/99525324/9630fff4-609b-44eb-a42f-bfba33ecc460)

### ResNet
The ResNet model is trained on a "model" model with 18 layers and 2 dense layers. The model is compiled with the ‘Adam’ optimizer, ‘categorical_crossentropy’ loss, and ‘accuracy’ metrics.
![Screenshot 2023-12-10 221602](https://github.com/rahuln2002/Sign-Language-Recognition-using-LSTM-model/assets/99525324/8650fc2b-6e5a-4248-9530-4a92972a3a93)

![Screenshot 2023-12-10 221622](https://github.com/rahuln2002/Sign-Language-Recognition-using-LSTM-model/assets/99525324/e0ae9dca-13c0-4db3-9d4e-77c9bc391665)

![Screenshot 2023-12-10 221638](https://github.com/rahuln2002/Sign-Language-Recognition-using-LSTM-model/assets/99525324/efb1bc6a-b375-4136-8dea-1edc0631041f)

![Screenshot 2023-12-10 221656](https://github.com/rahuln2002/Sign-Language-Recognition-using-LSTM-model/assets/99525324/6e5c814b-3013-4648-80f3-6c5ba68755ac)

![Screenshot 2023-12-10 221707](https://github.com/rahuln2002/Sign-Language-Recognition-using-LSTM-model/assets/99525324/0e5f3a8a-78d1-486d-b65b-fa56f57c0d72)


### VGG16
The VGG16 model is trained on a "sequential" model with 28 layers and 2 dense layers. The model is compiled with the ‘Adam’ optimizer, ‘categorical_crossentropy’ loss, and ‘accuracy’ metrics.

![Screenshot 2023-12-10 222048](https://github.com/rahuln2002/Sign-Language-Recognition-using-LSTM-model/assets/99525324/f89dcf60-1168-419f-8421-63b6602903df)

![Screenshot 2023-12-10 222105](https://github.com/rahuln2002/Sign-Language-Recognition-using-LSTM-model/assets/99525324/36ff12ba-959c-4dcf-93fd-6c94c212243f)



