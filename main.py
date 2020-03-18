from tkinter import * 
from tkinter import ttk
import graph

window = Tk()
window.title("Area Visualization")



STARTRANGE = None
ENDRANGE = None
N = 20 
DRAWTYPE = True # true means rectangle false means trapezoid

def runGraph():
    statusS, STARTRANGE =  retrieve_strt()
    statusE, ENDRANGE= retrieveEnd()
    status_n, N = retrieve_n()
    fx = retrieve_fx()
    if statusS and statusE and status_n:
        if(ENDRANGE>STARTRANGE):
            graph.draw(STARTRANGE,ENDRANGE,N,DRAWTYPE,fx,menu.get().upper())
    else:
        print("incorrect")
    

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

def retrieve_strt():
    try: 
        strtRange = float(startRangeEntry.get())
    except ValueError :
        return False, 0
    return True, strtRange

def retrieveEnd():
    try: 
        endRange = float(endRangeEntry.get())
    except ValueError :
        return False, 0
    return True, endRange

def retrieve_n():
    try: 
        n = float(nEntry.get())
    except ValueError :
        return False, 0
    return True, n

def retrieve_fx():
    fx = fxEntry.get()
    return fx



fxText = Label(window, text = "Function")
startRangeText = Label(window, text = "Start Range")
endRangeText = Label(window, text = "End Range")
nText = Label(window, text = "N")   

#Initialize Labels to grid
fxText.grid(row = 0,column = 0)

startRangeText.grid(row = 1,column = 0)
endRangeText.grid(row = 2,column = 0)
nText.grid(row =3,column = 0)

graphButton = Button(window, text = "Graph",command =  runGraph)
graphButton.grid(row = 4, column = 1, pady = 2)

#Text Entry Fields
startRangeEntry = Entry(window)
endRangeEntry = Entry(window)
nEntry = Entry(window)
fxEntry = Entry(window)

#Initialize Text Entry Fields to 
fxEntry.grid(row=0, column = 1,sticky = W,pady = 2)
startRangeEntry.grid(row=1, column = 1,sticky = W,pady = 2)
endRangeEntry.grid(row=2,column = 1,stick = W,pady = 2)
nEntry.grid(row=3,column = 1,stick = W,pady = 2)

options = ["LEFT","RIGHT","MIDDLE"]
splash = StringVar(window)
splash.set("Riemman Draw Location")
#Combobox
menu = ttk.Combobox(window,textvariable = splash,values =["Left","Right","Middle"],state = "readonly")
menu.grid(row = 3, column = 3,sticky = EW,pady = 2,)

isRiemannCheck = Checkbutton(window, text = "Riemann", command=isRiemannCheck)
isTrapezoidCheck = Checkbutton(window, text = "Trapezoid", command=isTrapezoidCheck)

isRiemannCheck.grid(row = 0, column = 3,sticky = W,pady = 2)
isTrapezoidCheck.grid(row = 1, column = 3,sticky = W,pady = 2)

break_line = ttk.Separator(orient=HORIZONTAL)
break_line.grid(row = 2, column = 3,sticky = EW,pady = 2)

window.mainloop()
