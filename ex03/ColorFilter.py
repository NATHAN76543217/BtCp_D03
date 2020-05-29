import numpy as np


class ColorFilter():
    def __init__(self):
        pass

    def invert(self, array):
        """
            Renvoie une copie negative de l'image passé en parametre
            Authorized functions: None
            Authorized operator: -
        """
        new = np.copy(array)
        new = 255 - new
        return new

    def to_blue(self, array):
        """
            Takes a NumPy array of an image as an argument
                and returns an array with a blue filter.
            Authorized functions: .zeros, .shape
            Authorized operator: None
        """
        new = np.copy(array)
        # zero = np.zeros(new.shape, int)
        # zero[:, :, :2] = 255
        # new = new - zero
        # new[new < 0] = 0
        new[:, :, :2] = 0
        return new

    def to_green(self, array):
        """
            Takes a NumPy array of an image as an
                argument and returns an array with a green filter.
            Authorized functions: None
            Authorized operator: *
        """
        new = np.copy(array)
        new[:, :, 0] = 0
        new[:, :, 2] = 0
        return new

    def to_red(self, array):
        """
            Takes a NumPy array of an image as an argument and
                returns an array with a red filter.
            Authorized functions : green, blue
            Authorized operator: -, +
        """
        new = np.copy(array)
        new -= self.to_green(new) + self.to_blue(new)
        return new
