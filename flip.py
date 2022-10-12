import math
import tkinter
from tkinter import *
from math import *
from random import *
import time


root = Tk()
root.title("Cosmopol")
root.geometry("2000x1000")


my_canvas = Canvas(root, width=1000, height=1000, bg="white")
my_canvas.pack(pady=20)

centerX = 500
centerY = 500


xRange = 1000
yRange = 1000
def flip():
    period = 20
    frames = 10000
    maxHeight = 5 / 2
    observeHeight = 5
    coinRelativeSize = 1/2
    sizeC = 200
    startHeight = 1
    for x in range(frames):
        height = startHeight + (maxHeight - startHeight) *(-x*(x-frames)/(frames/2)**2)
        my_canvas.delete("all")
        rotSinPos = abs(math.sin(x * period * pi / (2 * frames)))
        rotCosPos = abs(math.cos(x * period * pi / (2 * frames)))
        for y in range(yRange):
            my_canvas.create_line(0,y,cos(y/500*pi)*xRange/2,y,fill="red")
            my_canvas.create_line(xRange-cos(y/500*pi)*xRange/2,y,xRange,y,fill="red")
        root.update()

flip()
root.mainloop()