import keras
from keras.model import 
from resize_image import image_treatment

class fit():

    def __init__(self, train, test):
        self.train = train
        self.test = test 
        
        training_data = image_treatment.data_generator()

    def fit_model(train, test):

        model = Sequential()
        # Conv
        model.add(Conv2D(32,(3,3), input_shape = (520, 520,3), activation = 'relu'))
        # Pooling
        model.add(MaxPooling(pool_size = (2,2)))
        # Second Conv
        model.add(Conv2D(32,(3,3), activation='relu'))
        model.add(MaxPooling(pool_size = (2,2)))
        # Flatting
        model.add(Flatten())
        # Full Connected
        model.add(Dense(units = 128, activation = 'relu'))
        model.add(Dense(units = 1, activation = 'sigmoid'))
        # Compiling CNN
        model.compile(optmizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])
    
    def training(df_train):
        model.fit_generator(
            training_data,
            steps_per_epoch = 8000,
            epochs = 25,
            validation_steps = 2000)
