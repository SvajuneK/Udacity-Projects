import argparse
import numpy as np
import pandas as pd
import tensorflow as tf
import tensorflow_hub as hub
import json
from PIL import Image

#### Functions ####

def load_image(image_path):
    """This function loads the image from the specified repository"""
    im = Image.open(image_path)
    return np.asarray(im)

def process_image(image):
    """This is image normalisation function"""
    image_size = 224
    image = tf.image.resize(image, (image_size, image_size))
    image /= 255
    return image.numpy()

def predict_prob_class(image, model_path, K_classes):
    """This function reshapes the image to feed the prediction model and returns the specified number of classes with the highest  probabilities."""
    
    model = tf.keras.models.load_model(model_path, custom_objects={'KerasLayer':hub.KerasLayer})

    reshape_image = np.expand_dims(image, axis = 0)
    ps = model.predict(reshape_image)
    classes = np.argsort(ps[0])[::-1][:K_classes]
    probs = ps[0][classes]
    return probs, classes

def class_dictionary(class_dic_path, classes):
    """This function loads classes labels and do basic cleaning."""
    with open(class_dic_path, 'r') as f:
        class_names = json.load(f)
    
    # Fix the flower number. Need to align starting points. 
    class_names_ = pd.DataFrame.from_dict(class_names,orient='index').reset_index()
    class_names_['index'] = class_names_['index'].astype(int)-1
    class_names_ = class_names_.set_index('index')
    class_names = pd.DataFrame.to_dict(class_names_)[0]

    class_labels = []
    for flower in classes:
        class_labels.append(class_names[flower])
    
    return class_labels

def main(image_path, model_path, K_classes = 5, class_dic_path = None):
    
    """This function runs the prediction on a given image. 
    
    INPUT: 
            - Image path, 
            - Predictive model path, 
            - Number of classed with the largest probabilities, 
            - Path to class dictionary with labels
            
    OUTPUT:
            - Prediction of the flower class with the assigned probability. """
    
    image = load_image(image_path)
    image = process_image(image)
    probs, classes = predict_prob_class(image, model_path, K_classes)
    if class_dic_path != None:
        class_labels = class_dictionary(class_dic_path, classes)
        classes = class_labels
    
    return classes, probs
    
    
if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument("image_path")
    parser.add_argument("model_path")
    parser.add_argument("--K_classes")
    parser.add_argument("--class_dic_path")
    
    args = parser.parse_args()
    
    if args.K_classes == None:
        args.K_classes = 5
    args.K_classes = int(args.K_classes)
    
    if args.class_dic_path == None:
        args.class_dic_path = None
    
   
    classes, probs = main(args.image_path,
                          args.model_path,
                          args.K_classes,
                          args.class_dic_path)
    
    print("Classes are:", classes)
    print("Probabilities of corresponding classes are:", probs)
