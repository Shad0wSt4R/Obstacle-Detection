import cv2
import math
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import keras
from keras import models
from keras.preprocessing import image

# Load model to make predictions
model = models.load_model('model_cat_dog.h5')


# Turn video frames into image array
#vidcap = cv2.VideoCapture('driving_vids/Downtown.mp4')
#ret, frame = vidcap.read()
#ratio = 1.0
#image = cv2.resize(frame, (0, 0), None, ratio, ratio)
#width2, height2, channels = image.shape

#while True:
#    ret, frame = vidcap.read()

    # Repeat video when finished
#    if not ret:
#        frame = cv2.VideoCapture('driving_vids/Downtown.mp4')
#        continue
#    if ret:
#        image = cv2.resize(frame, (0, 0), None, ratio, ratio)
#        cv2.imshow("image", image)

# Make prediction
model.predict(image)
