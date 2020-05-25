'''main.py'''
from tkinter import Tk, ttk, StringVar, Label, Button, Entry, W, EW, Checkbutton, HORIZONTAL
import graph

window = Tk()
window.title("Area Visualization")



DRAWTYPE = None


def run_graph():
    '''Grab input from tk.entrys'''
    status_s, start_range = retrieve_strt()  # statuses are a boolean return
    status_e, end_range = retrieve_end()
    status_n, n = retrieve_n()
    fx = retrieve_fx()
    if status_s and status_e and status_n:
        if end_range > start_range:
            error_var.set('')
            if not graph.draw(start_range, end_range, n, DRAWTYPE, fx, menu.get()):
                error_var.set('Invalid Function')
        else:
            error_var.set('Invalid Function')


def is_riemann_check():
    '''Reverses the menu disabled from is_trapezoid_check()'''
    global DRAWTYPE
    DRAWTYPE = True
    menu.state(['!disabled'])
    is_trapezoid_check.deselect()


def is_trapezoid_check():
    ''' disables the Riemann sum menu because Trapezoids only have one state'''
    global DRAWTYPE
    DRAWTYPE = False
    menu.state(['disabled'])
    is_riemann_check.deselect()


def retrieve_strt():
    '''Does some simple checks before passing strtRange to draw(*args)'''
    try:
        strt_range = float(startRangeEntry.get())
    except ValueError:
        error_var.set('Input a valid starting range')
        return False, 0
    return True, strt_range


def retrieve_end():
    '''Retrieves endrange of function'''
    try:
        end_range = float(endRangeEntry.get())
    except ValueError:
        error_var.set('Input a valid end range')
        return False, 0
    return True, end_range


def retrieve_n():
    '''Retrieves number of rectangles wanted'''
    try:
        n = float(nEntry.get())
    except ValueError:
        return False, 0
    return True, n


def retrieve_fx():
    '''retrieve function'''
    fx = fxEntry.get()
    return fx.lower()


def test_val(in_str, acttyp):
    '''Forces an integer input on n input'''
    if acttyp == '1':  # insert
        if not in_str.isdigit():
            return False
    return True


error_var = StringVar()
# Labels
fxText = Label(window, text="Function")
startRangeText = Label(window, text="Start Range")
endRangeText = Label(window, text="End Range")
nText = Label(window, text="N")
error_text = Label(window, fg="red", textvariable=error_var, font='bold')

# Initialize Labels to grid
fxText.grid(row=0, column=0)
startRangeText.grid(row=1, column=0)
endRangeText.grid(row=2, column=0)
nText.grid(row=3, column=0)
error_text.grid(row=4, column=3)

# Button
graphButton = Button(window, text="Graph", command=run_graph)
graphButton.grid(row=4, column=1, pady=2)

# Text Entry Fields
startRangeEntry = Entry(window, validate="key")
endRangeEntry = Entry(window)
nEntry = Entry(window, validate="key")
nEntry['validatecommand'] = (nEntry.register(test_val), '%P', '%d')
fxEntry = Entry(window)

# Initialized to Grid
fxEntry.grid(row=0, column=1, sticky=W, pady=2)
startRangeEntry.grid(row=1, column=1, sticky=W, pady=2)
endRangeEntry.grid(row=2, column=1, stick=W, pady=2)
nEntry.grid(row=3, column=1, stick=W, pady=2)

options = ["LEFT", "RIGHT", "MIDDLE"]
splash = StringVar(window)
splash.set("Riemman Draw Location")
# Combobox
menu = ttk.Combobox(window, textvariable=splash, values=[
    "Left", "Right", "Middle"], state="readonly")
menu.grid(row=3, column=3, sticky=EW, pady=2,)

# CheckButton
is_riemann_check = Checkbutton(
    window, text="Riemann", command=is_riemann_check)
is_trapezoid_check = Checkbutton(
    window, text="Trapezoid", command=is_trapezoid_check)
# Initialized
is_riemann_check.grid(row=0, column=3, sticky=W, pady=2)
is_trapezoid_check.grid(row=1, column=3, sticky=W, pady=2)

# Breakline
break_line = ttk.Separator(orient=HORIZONTAL)
break_line.grid(row=2, column=3, sticky=EW, pady=2)

window.mainloop()
