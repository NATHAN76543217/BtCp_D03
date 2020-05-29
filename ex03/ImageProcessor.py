import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import numpy as np


class ImageProcessor():

    def load(self, path, convert_in_int=0, force_to_rgb=0):
        img = mpimg.imread(path)
        # Si le résultat n'est pas un tableau d'entiers
        if convert_in_int:
            img = (img * 255).astype(np.uint8)
        if force_to_rgb:
            img = img[:, :, :3]
        print("Loading image of dimensions {} x {}".format(*img.shape))
        return img

    def display(self, array, title=None):
        plt.imshow(array)
        if title:
            plt.title(title)
        plt.show()
