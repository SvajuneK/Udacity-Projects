# Build a Model with Google AutoML
## by Svajune Klimasauskaite


## Goal

The goal is to build a product that helps doctors quickly identify cases of pneumonia in children. Therefore we want to build a classification system that
* Can help flag serious cases
* Quickly identify healthy cases
* And, generally, act as a diagnostic aid for doctors.

## Scope

In this project, I use Google AutoML, an automated machine learning tool that allows to build the model and host it in the cloud. In order to appreciate how training data impact models, I build models with 4 variants of the dataset:
* Training a model by using 100 images from the “normal” class and 100 images from the “pneumonia” class. 
* Use 100 images from the “normal” class and 300 images in the “pneumonia” class. 
* Original dataset of 100 "normal" and 100 "pneumonia" images. Then switch the labels of 30 images in each class. 
* Create a three-class model with the classes “normal”, “bacterial pneumonia”, and “viral pneumonia” with 100 images in each class.  

## Dataset

The dataset is taken from [Kaggle chest x-ray](https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia).

----------
