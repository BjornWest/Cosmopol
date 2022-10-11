import math
import tkinter
from tkinter import *
from math import *
from random import *
import time


root = Tk()
root.title("Cosmopol")
root.geometry("2000x1000")

my_canvas = Canvas(root, width=1000, height=1000, bg="black")
my_canvas.pack(pady=20)



centerX = 500
centerY = 500



def flip():
    period = 20
    frames = 10000
    maxHeight = 3 / 2
    observeHeight = 5
    coinRelativeSize = 1/2
    sizeC = 200
    startHeight = 1
    for x in range(frames):
        height = startHeight + (maxHeight - startHeight) *(-x*(x-frames)/(frames/2)**2)
        my_canvas.delete("all")
        rotSinPos = abs(math.sin(x * period * pi / (2 * frames)))
        rotCosPos = abs(math.cos(x * period * pi / (2 * frames)))
        if math.cos(x * period * math.pi / (2 * frames)) > 0:
            my_canvas.create_oval(centerX - sizeC * height, centerY - sizeC * height + abs(sizeC * height * rotSinPos),
                                  centerX + sizeC * height, centerX + sizeC * height - height * sizeC * abs(rotSinPos),
                                  fill="black")
            my_canvas.create_rectangle(centerX - sizeC / 2 * height,
                                       centerY - height * (sizeC * 3 / 4 - sizeC * 3 / 4 * rotSinPos),
                                       centerX + height * sizeC / 2,
                                       centerY - height * (sizeC / 2 - sizeC / 2 * rotSinPos), fill="red")
            my_canvas.create_rectangle(centerX - height * sizeC / 6,
                                       centerY - height * (sizeC / 2 - sizeC / 2 * rotSinPos),
                                       centerX + height * sizeC / 6,
                                       centerY + height * (sizeC * 3 / 4 - sizeC * 3 / 4 * rotSinPos), fill="red")
        else:
            my_canvas.create_oval(centerX - sizeC * height, centerY - sizeC * height + abs(sizeC * height * rotSinPos),
                                  centerX + sizeC * height, centerX + sizeC * height - height * sizeC * abs(rotSinPos),
                                  fill="red")
            my_canvas.create_rectangle(centerX - height * sizeC / 6,
                                       centerY - height * (sizeC * 3 / 4 - sizeC * 3 / 4 * rotSinPos),
                                       centerX + height * sizeC / 6,
                                       centerY + height * (sizeC * 3 / 4 - sizeC * 3 / 4 * rotSinPos), fill="black")
        root.update()


sizeR = 200
def roulette():
    for x in range(frames):
        my_canvas.delete("all")
        my_canvas.create_oval(centerX-sizeR,centerY-sizeR,centerX+sizeR,centerY+sizeR,fill="black")
        coord = centerX-sizeR, centerY-sizeR, centerX+sizeR, centerY+sizeR
        deg = x*20/(frames+1)
        for y in range(12):
            my_canvas.create_arc(coord, start=deg*360+y*2*360/25, extent=360/25, fill="red")
        my_canvas.create_arc(coord, start=deg*360+24 * 360 / 25, extent=360 / 25, fill="green")
        root.update()


def crash(bet,guess):
    #guess = input("Enter your guess: ")
    guess = float(guess)
    crashTime = random()*random()*random()*random*20+1
    adjust = 1
    scale = 100
    scales = [2,5,10,20,50,100]
    scalePointer = 0
    for x in range(1000):

        yRange = 900
        xRange = 100
        xStart = xRange
        deriv = 1
        realHeight = 900
        height = yRange
        my_canvas.delete("all")
        for y in range(x):
            xEnd = xStart +(my_canvas.winfo_width()-xRange) /x
            my_canvas.create_line(xStart,height,xEnd,height-deriv/adjust,fill="red",width="2")
            xStart += (my_canvas.winfo_width()-xRange)/x
            realHeight = realHeight-deriv
            height = height-deriv/adjust
            deriv +=1/10
        my_canvas.create_line(xRange/2,yRange,xRange/2,0,fill="green",width="3")

        if realHeight-my_canvas.winfo_width() < -10 * scale:
            scale = 100*scales[scalePointer]
            scalePointer += 1
        for y in range(int(20)):
            my_canvas.create_line(xRange/4,yRange-scale*y/adjust,xRange*3/4,yRange-scale*y/adjust,fill="green",width="2")
            my_canvas.create_text(xRange/5,yRange-scale*y/adjust, text=int(scale*y)/1000+1, fill="green", width="10", anchor=tkinter.CENTER)
        if height<yRange/2:
            adjust = 1+1.05*(yRange/2-realHeight)/yRange
        if (realHeight-yRange)/my_canvas.winfo_height() < -crashTime+1:
            print(f"Your guess: {guess}")
            print(f"Crash point: {crashTime}")
            if guess <= crashTime:
                my_canvas.create_text(500, 500, text=f'{bet*(guess-1)} $ win! Keep going!', anchor=tkinter.CENTER, width="10i", fill="blue")
                print(f'{bet*(guess-1)} $ win! Keep going!')
                return bet*(guess-1)
            else:
                my_canvas.create_text(500,500,text="game over",anchor=tkinter.CENTER,width="10i",fill="blue")
                root.update()
                print("Better luck next time!")
            return -bet

        root.update()
        time.sleep(1/20)
cash = 100
times = 0
while cash>0:
    times+=1
    cash = cash +crash(10,2)
    print("cash:",cash)

print("wins: ",times/2-5, "losses: ",5+times/2, "win %",(times/2-5)/times)

root.mainloop()
