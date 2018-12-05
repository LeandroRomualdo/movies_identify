from pytube import YouTube
from pytube import Playlist
import cv2
import math
import numpy as np
from skimage.transform import resize
import os

class get_videos_frames():

    def __init__(self, url,movie, dataset):
        self.url = url
        self.dataset = dataset
        self.movie = movie

    # Baixa trailers do youtube
    def get_videos_playlist(self, url):

        input_loc = 'movies/'
        print('Inicio do processo')
        mv = Playlist(self.url)
        if not os.path.exists(input_loc):
            os.makedirs(input_loc)
            print('Baixando conteudo')
        mv.download_all(input_loc)
        print('Finalizado!')

    def get_frames(self,movie,dataset):

        output_loc = dataset+'/'
        input_loc = 'movies/'
        
        vidcap = cv2.VideoCapture(input_loc+self.movie)
        success,image = vidcap.read()
        count = 0
        while success:
            writename = str(self.movie)+'%d.jpg' % count
            cv2.imwrite(output_loc+writename, image)
            success,image = vidcap.read()
            #print('Read a new frame: ', success)
            count += 1