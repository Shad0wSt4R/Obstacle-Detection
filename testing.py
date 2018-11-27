import keras
from keras import models

model = models.load_model('model.h5')

model.predict(image_array)
