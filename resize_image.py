import cv2

class image_treatment():

    def __init__(self, image,path):
        self.image = image
        self.path = path

    def resize_image(self,image,path):

        width = 520
        height = 520
        path_loc = path+'/'

        img = cv2.resize(image, width,height)
        cv2.imwrite(path_loc, img)