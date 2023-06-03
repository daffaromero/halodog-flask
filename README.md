# halodog-flask
Back-end Flask untuk https://github.com/daffaromero/Halodog

Machine Learning (CNN - ResNet-50)
------
![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-%23D00000.svg?style=for-the-badge&logo=Keras&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Kaggle](https://img.shields.io/badge/Kaggle-035a7d?style=for-the-badge&logo=kaggle&logoColor=white)

Kode Machine Learning (image classification) menggunakan model ResNet-50 dari [Tensorflow Hub](https://tfhub.dev/). Dataset diambil dari [Kaggle](https://www.kaggle.com/datasets/lasaljaywardena/animal-images-dataset). Model menerima input gambar yang diubah menjadi tensor. Akurasi mencapai 92-93% dengan ResNet-50.


Back-end (Flask + Azure)
------
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![Azure](https://img.shields.io/badge/azure-%230072C6.svg?style=for-the-badge&logo=microsoftazure&logoColor=white)
![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)

Ditulis dalam bahasa Python (Flask) dan di-deploy menggunakan Azure VM (Ubuntu 20.04) di URL: http://tulations.eastus.cloudapp.azure.com:5000

Route yang tersedia:

- '/' (GET): home page
- '/predict' (GET, POST): hasil prediksi foto dari URL


Daffa Muhammad Romero, 2023
