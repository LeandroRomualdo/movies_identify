from pytube import YouTube
from pytube import Playlist
import cv2
import math
import numpy as np
from skimage.transform import resize
import os
from configparser import SafeConfigParser


class get_videos_frames():

    def __init__(self):
        pass
        #self.url = url
        #self.movie = movie

    # Baixa trailers do youtube
    def get_videos_playlist(self):
        # Extrai as informação de diretórios do arquivo de configuração.
        config = SafeConfigParser()
        config.read('config.conf')
        input_loc = config.get("input_loc")
        # Armazena as urls das playlists para download.
        urls = config.get("lista")

        for url in urls:
            print('Inicio do processo')
            mv = Playlist(url)
            if not os.path.exists(input_loc):
                os.makedirs(input_loc)
                print('Baixando conteudo')
            mv.download_all(input_loc)
            print('Finalizado!')

    def get_frames(self):
        # Extrai as informação de diretórios do arquivo de configuração.
        config = SafeConfigParser()
        config.read('config.conf')

        output_loc = config.get("output_loc")
        input_loc = config.get("input_loc")
        # Lista os filmes baixados no diretório
        movies = os.listdir('movies/')

        for movie in movies:
            vidcap = cv2.VideoCapture(input_loc+movie)
            success,image = vidcap.read()
            count = 0
            while success:
                writename = str(movie)+'%d.jpg' % count
                cv2.imwrite(output_loc+writename, image)
                success,image = vidcap.read()
                #print('Read a new frame: ', success)
                count += 1