from tkinter import * 
from tkinter import ttk
import graph
from math import *

window = Tk()
window.title("Area Visualization")



STARTRANGE = None
ENDRANGE = None
N = 20 
DRAWTYPE = True # true means rectangle false means trapezoid

def runGraph():
    statusS, STARTRANGE =  retrieve_strt() #status is a boolean return 
    statusE, ENDRANGE= retrieveEnd()
    status_n, N = retrieve_n()
    fx = retrieve_fx()
    if statusS and statusE and status_n:
        if(ENDRANGE>STARTRANGE):
            if(valid_fx()):
                error_var.set('')
                graph.draw(STARTRANGE,ENDRANGE,N,DRAWTYPE,fx,menu.get().upper())
            else:
                error_var.set('Invalid Function')

    

def isRiemannCheck():
    global DRAWTYPE
    DRAWTYPE = True
    print(DRAWTYPE)
    menu.state(['!disabled'])
    isTrapezoidCheck.deselect()

def isTrapezoidCheck():
    global DRAWTYPE
    DRAWTYPE = False
    print(DRAWTYPE)
    menu.state(['disabled'])
    isRiemannCheck.deselect()

def retrieve_strt():
    try: 
        strtRange = float(startRangeEntry.get())
    except ValueError :
        error_var.set('Input a valid starting range')
        return False, 0
    return True, strtRange

def retrieveEnd():
    try: 
        endRange = float(endRangeEntry.get())
    except ValueError :
        error_var.set('Input a valid end range')
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

def valid_fx():
    x=0
    try:
        eval(retrieve_fx())
    except(NameError,SyntaxError,TypeError) as e:
        return False
    else:
        return True

def test_val(inStr,acttyp):
    if acttyp == '1': #insert
        if not inStr.isdigit():
            return False
    return True

    


error_var = StringVar()
#Labels
fxText = Label(window, text = "Function")
startRangeText = Label(window, text = "Start Range")
endRangeText = Label(window, text = "End Range")
nText = Label(window, text = "N")
error_text = Label(window,fg="red", textvariable = error_var,font='bold')   

#Initialize Labels to grid
fxText.grid(row = 0,column = 0)
startRangeText.grid(row = 1,column = 0)
endRangeText.grid(row = 2,column = 0)
nText.grid(row =3,column = 0)
error_text.grid(row = 4, column = 3)

#Button
graphButton = Button(window, text = "Graph",command =  runGraph)
graphButton.grid(row = 4, column = 1, pady = 2)


#Text Entry Fields
startRangeEntry = Entry(window, validate="key")
endRangeEntry = Entry(window)
nEntry = Entry(window, validate="key")
nEntry['validatecommand'] = (nEntry.register(test_val),'%P','%d')
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
