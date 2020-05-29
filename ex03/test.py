from ColorFilter import ColorFilter
from ImageProcessor import ImageProcessor
import numpy as np
IP = ImageProcessor()
arr = IP.load("Elon.png", convert_in_int=1, force_to_rgb=1)
CF = ColorFilter()

print("Original")
IP.display(arr, title="Original")

print("Inverted")
inverted = CF.invert(arr)
IP.display(inverted, title="Inverted")

print("To_blue")
to_blue = CF.to_blue(arr)
IP.display(to_blue, title="to_blue")

print("To_green")
to_green = CF.to_green(arr)
IP.display(to_green, title="to_green")

print("To_red")
to_red = CF.to_red(arr)
IP.display(to_red, title="to_red")
