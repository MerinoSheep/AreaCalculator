import os
import tkinter
from tkinter import * 
import graph

window = tkinter.Tk()
window.title("Area Visualization")

STARTRANGE = 0
ENDRANGE = 15
N = 20
DRAWTYPE = None # true means rectangle false means trapezoid
def runGraph(STARTRANGE,ENDRANGE,N,DRAWTYPE):
    status, STARTRANGE =  retrieve_n()
    if status:
        graph.draw(STARTRANGE,ENDRANGE,N,DRAWTYPE)
    else:
        print(STARTRANGE)
    

def isRiemannCheck():
    global DRAWTYPE
    DRAWTYPE = True
    print(DRAWTYPE)
    isTrapezoidCheck.deselect()

def isTrapezoidCheck():
    global DRAWTYPE
    DRAWTYPE = False
    print(DRAWTYPE)
    isRiemannCheck.deselect()

def retrieve_n():
    print("retrieve_n()")
    try: 
        strtRange = float(startRangeEntry.get())
    except ValueError :
        return False, 0
    except TypeError :
        return False, 0
    return True, strtRange


fxText = Label(window, text = "Function")
startRangeText = Label(window, text = "Start Range")
endRangeText = Label(window, text = "End Range")
nText = Label(window, text = "N")   

fxText.grid(row = 0,column = 0)
startRangeText.grid(row = 1,column = 0)
endRangeText.grid(row = 2,column = 0)
nText.grid(row =3,column = 0)

graphButton = tkinter.Button(window, text = "Graph", command = lambda: runGraph(STARTRANGE,ENDRANGE,N,DRAWTYPE))
graphButton.grid(row = 4, column = 1, pady = 2)

startRangeEntry = Entry(window)
endRangeEntry = Entry(window)
nEntry = Entry(window)
fxEntry = Entry(window)

fxEntry.grid(row=0, column = 1,sticky = W,pady = 2)
startRangeEntry.grid(row=1, column = 1,sticky = W,pady = 2)
endRangeEntry.grid(row=2,column = 1,stick = W,pady = 2)
nEntry.grid(row=3,column = 1,stick = W,pady = 2)


isRiemannCheck = Checkbutton(window, text = "Riemann", command=isRiemannCheck)
isTrapezoidCheck = Checkbutton(window, text = "Trapezoid", command=isTrapezoidCheck)

isRiemannCheck.grid(row = 0, column = 3,sticky = W,pady = 2)
isTrapezoidCheck.grid(row = 1, column = 3,sticky = W,pady = 2)


window.mainloop()
