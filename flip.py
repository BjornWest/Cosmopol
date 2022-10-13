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
    period = 4
    frames = 1000
    maxHeight = 2000
    observeHeight = 5000
    sizeC = 1000
    startHeight = 0
    for x in range(frames):
        heightFactor = sizeC/(observeHeight-(maxHeight - startHeight) *(-x*(x-frames)/(frames/2)**2))
        my_canvas.delete("all")
        rotSinPos = abs(math.sin(x * period * pi / (2 * frames)))
        rotCosPos = abs(math.cos(x * period * pi / (2 * frames)))
        radius = sizeC*heightFactor
        yRadius = radius*rotSinPos
        my_canvas.create_line(0,yRange/2,xRange,yRange/2)
        for y in range(int(2*radius)):
            xCircle = sqrt(radius**2-((y-radius)**2))*heightFactor/(heightFactor-sizeC*rotSinPos*)
            #my_canvas.create_line(0,yRange/2-radius+y,xRange/2-xCircle,yRange/2-radius+y,fill="white")
            my_canvas.create_line(xRange/2-xCircle,yRange/2-yRadius+y*rotSinPos,xRange/2+xCircle,yRange/2-yRadius+y*rotSinPos,fill="red")
            #my_canvas.create_line(xRange/2+xCircle,yRange/2-radius+y,xRange,yRange/2-radius+y,fill="white")

        root.update()
for x in range(10):
    flip()
root.mainloop()