import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np


class ImageProcessor():

    def load(self, path, convert_in_int=0):
        img = mpimg.imread(path)
        # Si le résultat n'est pas un tableau d'entiers
        if convert_in_int:
            img = (img * 255).astype(np.uint8)
        print("Loading image of dimensions {} x {}".format(*img.shape))
        return img

    def display(self, array):
        plt.imshow(array)
        plt.show()
