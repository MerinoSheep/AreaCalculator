import os
import tkinter
from tkinter import * 
import graph

window = tkinter.Tk()
window.title("GUI")

STARTRANGE = 0
ENDRANGE = 15
N = 20
DRAWTYPE = True # true means rectangle false means trapezoid
def runGraph(STARTRANGE,ENDRANGE,N):
    graph.draw(STARTRANGE,ENDRANGE,N)

def isRiemannCheck():
    DRAWTYPE = True
    isTrapezoidCheck.deselect()

def isTrapezoidCheck():
    DRAWTYPE = False
    isRiemannCheck.deselect()

graphButton = tkinter.Button(window, text = "Graph", command = lambda: runGraph(STARTRANGE,ENDRANGE,N))
graphButton.grid(row = 1, column = 0, pady = 2)

e1 = Entry(window)
e1.grid(row=0, column = 0,sticky = W,pady = 2)

isRiemannCheck = Checkbutton(window, text = "Riemann", command=isRiemannCheck)
isTrapezoidCheck = Checkbutton(window, text = "Trapezoid", command=isTrapezoidCheck)
isRiemannCheck.grid(row = 0, column = 1,sticky = W,pady = 2)
isTrapezoidCheck.grid(row = 1, column = 1,sticky = W,pady = 2)


window.mainloop()
