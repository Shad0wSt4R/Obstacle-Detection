import pandas as pd
import numpy as np
import os
import keras
import matplotlib.pyplot as plt
from keras.layers import Dense,GlobalAveragePooling2D
from keras.applications import MobileNet
from keras.preprocessing import image
from keras.applications.mobilenet import preprocess_input
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Model
from keras.optimizers import Adam

base_model=MobileNet(weights='imagenet',include_top=False) #imports the mobilenet model and discards the last 1000 neuron layer.

x=base_model.output
x=GlobalAveragePooling2D()(x)
x=Dense(1024,activation='relu')(x) #we add dense layers so that the model can learn more complex functions and classify for better results.
x=Dense(1024,activation='relu')(x) #dense layer 2
x=Dense(512,activation='relu')(x) #dense layer 3
preds=Dense(120,activation='softmax')(x) #final layer with softmax activation

model = Model(inputs=base_model.input,outputs=preds)

for i,layer in enumerate(model.layers):
    print(i, layer.name)

for layer in model.layers:
    layer.trainable=False

for layer in model.layers[:20]:
    layer.trainable=False

for layer in model.layers[20:]:
    layer.trainable=True

train_datagen=ImageDataGenerator(preprocessing_function=preprocess_input)

train_genrator=train_datagen.flow_from_directory('path-to-the-main-data-folder',
                                                target_size=(224,224),
                                                color_mode='rgb',
                                                batch_size=32,
                                                class_mode='categorical',
                                                shuffle=True)

model.compile(optimizer='Adam', loss='categorical_crossentcopy',metrics=['accuracy'])

step_size_train=train_generator.n/train_generator.batch_size
model.fit_generator(generator=train_generator,steps_per_epoch=step_size_train, epochs=10)

model.save("model.h5")


