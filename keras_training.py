import readLabels
from readLabels import readLabels
import keras
from keras.models import Sequential
from keras.layers import Dense, Activation

for i in range(7481):
    if(i < 10):
        readLabels('training/label_2', "00000"+i+".txt")
    elif(i >= 10 and i < 100):
        readLabels('training/label_2', "0000"+i+".txt")
    elif(i >= 100 and i < 1000):
        readLabels('training/label_2', "000"+i+".txt")
    else:
        readLabels('training/label_2', "00"+i+".txt")

#model = Sequential()

#model.add(Dense(32, input_dim=784))
#model.add(Activation('relu'))

#model.save("model.h5")
