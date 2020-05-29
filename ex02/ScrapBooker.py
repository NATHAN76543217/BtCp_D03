import numpy as np


class ScrapBooker():

    def crop(self, array, dimensions, position=(0, 0)):
        """
        crops the image as a rectangle with the given dimensions
        (meaning, the new height and width for the image), whose
        top left corner is given by the position argument.
        The position should be (0,0) by default.
        You have to consider it an error (and handle said error)
        if dimensions is larger than the current image size.
        """
        x = 0
        y = 0
        if (not isinstance(dimensions[0], int) or
                not isinstance(dimensions[1], int)):
            return None
        elif array.shape[0] < dimensions[0] or array.shape[1] < dimensions[1]:
            return None
        elif position[0] > array.shape[1] or position[1] > array.shape[0]:
            return None
        new = np.copy(array)
        # Suppr axe X avant
        while x < position[0]:
            new = np.delete(new, 0, axis=1)
            x += 1
        # Suppr axe X apres
        while dimensions[1] < new.shape[1]:
            new = np.delete(new, dimensions[1], axis=1)
        # Suppr axe Y avant
        while y < position[1]:
            new = np.delete(new, 0, axis=0)
            y += 1
        # Suppr axe Y apres
        while dimensions[0] < new.shape[0]:
            new = np.delete(new, dimensions[0], axis=0)
        return new

    def thin(self, array, n, axis=0):
        """
        deletes every n-th pixel row along the specified
            axis (0 vertical, 1 horizontal),
        example below.
        """
        new = np.copy(array)
        if n == 0 or not isinstance(axis, int):
            return new
        i = n
        if isinstance(axis, int) and axis < len(new.shape):
            maxi = new.shape[axis]
        else:
            maxi = min(new.shape[:2])
        while(i < maxi):
            new = np.delete(new, i, axis=axis)
            maxi -= 1
            i += n
        return new

    def juxtapose(self, array, n, axis):
        """
        juxtaposes n copies of the image along
            the specified axis (0 vertical, 1 horizontal).
        """
        new = np.copy(array)
        i = 1
        while i < n:
            new = np.append(new, array, axis=axis)
            i += 1
        return new

    def mosaic(self, array, dimensions):
        """
        makes a grid with multiple copies of the array.
        The dimensions argument specifies the dimensions
        (meaning the height and width) of the grid (e.g. 2x3).
        """
        new = np.copy(array)
        x, y = dimensions
        new = self.juxtapose(new, x, axis=1)
        new = self.juxtapose(new, y, axis=0)
        return new
