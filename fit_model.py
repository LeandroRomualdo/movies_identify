import keras
from keras.models import Sequential
from keras.layers import Dense, Conv2D, Activation, Dropout, MaxPooling2D, Flatten
from keras.optimizers import SGD
from keras.preprocessing.image import ImageDataGenerator

from train_test import train_test

class model_fit():

    def __init__(self, train, test):
        self.train = train
        self.test = test 

    def fit_model(self, train, test):

        model = Sequential()
        # Conv
        model.add(Conv2D(32,(3,3), input_shape = (520, 520,3), activation = 'relu'))
        # Pooling
        model.add(MaxPooling2D(pool_size = (2,2)))
        # Second Conv
        model.add(Conv2D(32,(3,3), activation='relu'))
        model.add(MaxPooling2D(pool_size = (2,2)))
        # Flatting
        model.add(Flatten())
        # Full Connected
        model.add(Dense(units = 128, activation = 'relu'))
        model.add(Dense(units = 1, activation = 'sigmoid'))
        # Compiling CNN
        model.compile(optimizer = 'rmsprop', 
                        loss = 'categorical_crossentropy',
                        metrics = ['accuracy'])

        ## Normalize data
        training_data = train_test()

