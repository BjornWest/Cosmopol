import math
import tkinter
from tkinter import *
from math import *
from random import *
import time


root = Tk()
root.title("Cosmopol")
root.geometry("1000x1000")


my_canvas = Canvas(root, width=1000, height=1000, bg="white")
my_canvas.pack(pady=20)

centerX = 500
centerY = 500

# storlek på fönstret
xRange = 1000
yRange = 1000
def flip():
    #antal flippar
    period = 8
    #antal frames i animationen
    frames = 250
    #hur mycket myntet rör sig
    TravelX = 2000
    #origo
    start = [0,0,0]
    #myntets punkt
    coinPos = start
    #observatörens position
    observe = [0,1000,1]
    #graderna på observatörens synfält OBS WIP
    observeDegrees = 45
    #riktning på observatör
    observeDirection = [1,0,0]
    #lutning på kamera, (mäts i radianer) standard = [1,0,0] och utvecklas [cos v,sin v, 0] OBS WIP
    observeRotation = 0
    #radien på myntet
    r = 1000
    for x in range(frames):

        coinPos[2] = start[0]+TravelX*(-x*(x-frames)/(frames/2)**2)
        my_canvas.delete("all")
        rotSinPos = math.sin(x * period * pi / (1 * frames))
        rotCosPos = math.cos(x * period * pi / (1 * frames))
        my_canvas.create_line(0,yRange/2,xRange,yRange/2)
        my_canvas.create_line(xRange/2,0,xRange/2,yRange)

        for y in range(2*r):
            #kanterna för raden som generaras
            height = coinPos[0]+(r-y)*rotCosPos
            edge1 = [coinPos[1]-sqrt(r**2-((y-r)**2)),height,coinPos[2]+(r-y)*rotSinPos]
            edge2 = [coinPos[1]+sqrt(r**2-((y-r)**2)),height,coinPos[2]+(r-y)*rotSinPos]
            vector1 = [edge1[0] - observe[0],edge1[1]- observe[1],edge1[2]- observe[2]]
            vector2 = [edge2[0] - observe[0],edge2[1]- observe[1],edge2[2]- observe[2]]
            proj1X = xRange/2+vector1[0]/vector1[2]*xRange/2    
            proj1Y = yRange/2+vector1[1]/vector1[2]*yRange/2
            proj2X = xRange/2+vector2[0]/vector2[2]*xRange/2
            proj2Y = yRange/2+vector2[1]/vector2[2]*yRange/2
            my_canvas.create_line(proj1X,proj1Y,proj2X,proj2Y,fill="red")

        root.update()
for x in range(10):
    flip()
root.mainloop()
