from keras.preprocessing.image import ImageDataGenerator
from get_image import get_videos_frames


class image_treatment():

    def __init__(self, path):
        self.path = path

    def datagen(self):
        train_datagen = ImageDataGenerator(rescale = 1./255,
                                            shear_range = 0.2,
                                            zoom_range = 0.2,
                                            horizontal_flip = True)
        
        test_datagen = ImageDataGenerator(rescale = 1./255)

    def data_generator(self):
        training_data = datagen.flow_from_directory(
            'train/',
            target_size = (520,520),
            batch_size=32,
            class_mode='categorical')
    
