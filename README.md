# halodog-flask
Back-end Flask untuk https://github.com/daffaromero/Halodog
<br>
<br>

Machine Learning (CNN - ResNet-50)
------
![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-%23D00000.svg?style=for-the-badge&logo=Keras&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Kaggle](https://img.shields.io/badge/Kaggle-035a7d?style=for-the-badge&logo=kaggle&logoColor=white)

Kode machine learning (image classification) menggunakan transfer learning dengan base model ResNet-50 dari [Tensorflow Hub](https://tfhub.dev/). Dataset diambil dari [Kaggle](https://www.kaggle.com/datasets/lasaljaywardena/animal-images-dataset). Model menerima input gambar yang diubah menjadi tensor. Akurasi mencapai 92-93% dengan ResNet-50.

------
**EN:** This machine learning (image classification) code uses ResNet-50 as its base model for transfer learning, taken from [Tensorflow Hub](https://tfhub.dev/). The dataset used for training is taken straight from [Kaggle](https://www.kaggle.com/datasets/lasaljaywardena/animal-images-dataset). The model takes images (converted to tensors) as input. Accuracy reaches 92-93% with ResNet-50.
<br>
<br>

Back-end (Flask + Azure)
------
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![Azure](https://img.shields.io/badge/azure-%230072C6.svg?style=for-the-badge&logo=microsoftazure&logoColor=white)
![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)

Ditulis dalam bahasa Python (Flask) dan di-deploy menggunakan Azure VM (Ubuntu 20.04) di URL: http://tulations.eastus.cloudapp.azure.com:5000

Inbound port: 22, 80, 443, 3389, 5000 (Flask), 8000

Route yang tersedia:

- '/' (GET): home page
- '/predict' (GET, POST): hasil prediksi foto dari URL

------
**EN:** Written in Python (Flask) and deployed on an Azure VM (Ubuntu 20.04) on this URL: http://tulations.eastus.cloudapp.azure.com:5000

Inbound ports: 22, 80, 443, 3389, 5000 (Flask), 8000

Available routes:

- '/' (GET): home page
- '/predict' (GET, POST): prediction result of a photo from a URL

Daffa Muhammad Romero, 2023
