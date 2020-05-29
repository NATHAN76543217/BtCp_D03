from ScrapBooker import ScrapBooker
from ImageProcessor import ImageProcessor


Imp = ImageProcessor()
print("LOAD BOX...")
ar = Imp.load("box.png")
print("BOX=", ar.shape)
Imp.display(ar)

ScBr = ScrapBooker()
print("\nthin on BOX n = {} et ax ={}".format(2, 1))
arr = ScBr.thin(ar, 2, 1)
print("BOX=", arr.shape)
print("\nthin on BOX n = {} et ax ={}".format(3, 0))
arr = ScBr.thin(arr, 3, 0)
print("BOX=", arr.shape)

Imp.display(arr)

arr = ScBr.juxtapose(arr, 2, 1)
print("\njuxtapose on BOX n = {} et ax ={}".format(2, 1))
print("BOX=", arr.shape)

arr = ScBr.mosaic(arr, (3, 3))
print("\nmosaic on BOX x = {} et y ={}".format(3, 3))
print("BOX=", arr.shape)

Imp.display(arr)

dim = (120, 120)
pos = (0, 0)
arr = ScBr.crop(ar, dim, pos)
print("\ncrop on BOX newx = {} et newy ={} at {}".format(dim[0], dim[1], pos))
print("BOX=", arr.shape)
Imp.display(arr)
