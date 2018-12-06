from get_image import get_videos_frames
from resize_image import image_treatment
from sklearn import train_test_split
import os
from keras.preprocessing import ImageDataGenerator
import configparser

class train_test():

    def __init__(self):
        pass

    def get_movies(self):

        # Lê arquivo de configuração com a lista das playlists.
        config = configparser.ConfigParser()
        config.read('config.conf')
        playlists = config.get("lista")

        # Baixa os trailer em mp4.
        try:
            for p in playlists:
                get_videos_frames.get_videos_playlist(p)
        except:
            print('Falha ao gerar os frames do video',p)

    def frames(self):

        # Faz o frame dos videos e salva.
        movies = os.listdir('movies/')
        try:
            for m in movies:
                get_videos_frames.get_frames(m)
        except:
            print('Erro ao extrair os frames dos videos')
        
        # Resize das imagens para 520x520 e salva no diretório de treino.
        img = os.listdir('Frames/')
        for i in img:
            image_treatment.resize_image(i, train)


    # Faz o slice das imagens e salva gerando o dataset de treino e teste.
    def train_and_test(self):
        
        train_datagen = ImageDataGenerator(rescale=1./255,
                                            shear_range=0.2,
                                            zoom_range=0.2,
                                            horizontal_flip=True)
        
        test_datagen = ImageDataGenerator(rescale=1./255)

        try:
            training_set = train_datagen.flow_from_directory('train/',
                                                             target_size=(520,520),
                                                             batch_size=32,
                                                             class_mode=None)
        except: 
            print('Erro ao gerar dataset de treino)

        try:
            test_set = test_datagen.flow_from_directory('test/',
                                                        target_size=(520,520),
                                                        batch_size=32,
                                                        class_mode=None)
        except:
            print('Erro ao gerar dataset de test')



