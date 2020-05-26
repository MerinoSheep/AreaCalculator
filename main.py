'''main.py'''
# TODO limit eval
from tkinter import Checkbutton, Tk, ttk, StringVar, Label, Button, Entry, W, EW,  HORIZONTAL, Toplevel, Frame
import graph
import integral_window


DRAWTYPE = None

class MainWindow:
    def __init__(self, master):
        #Frame.__init__(self, master)
        self.master = master
        self.error_var = StringVar()
        # Labels
        self.fxText = Label(self.master, text="Function")
        self.startRangeText = Label(self.master, text="Start Range")
        self.endRangeText = Label(self.master, text="End Range")
        self.nText = Label(self.master, text="N")
        self.error_text = Label(
            self.master, fg="red", textvariable=self.error_var, font='bold')

        # Initialize Labels to grid
        self.fxText.grid(row=0, column=0)
        self.startRangeText.grid(row=1, column=0)
        self.endRangeText.grid(row=2, column=0)
        self.nText.grid(row=3, column=0)
        self.error_text.grid(row=4, column=3)

        # Button
        self.graphButton = Button(
            self.master, text="Graph", command=self.run_graph)
        self.graphButton.grid(row=4, column=1, pady=2)
        self.calculate_button = Button(
            self.master, text="Calculate", command= self.run_calculate)
        self.calculate_button.grid(row=4, column=0, pady=2)
        # Text Entry Fields
        self.startRangeEntry = Entry(self.master, validate="key")
        self.endRangeEntry = Entry(self.master)
        self.nEntry = Entry(self.master, validate="key")
        self.nEntry['validatecommand'] = (
            self.nEntry.register(test_val), '%P', '%d')
        self.fxEntry = Entry(self.master)

        # Initialized to Grid
        self.fxEntry.grid(row=0, column=1, sticky=W, pady=2)
        self.startRangeEntry.grid(row=1, column=1, sticky=W, pady=2)
        self.endRangeEntry.grid(row=2, column=1, stick=W, pady=2)
        self.nEntry.grid(row=3, column=1, stick=W, pady=2)

        self.options = ["LEFT", "RIGHT", "MIDDLE"]
        self.splash = StringVar(self.master)
        self.splash.set("Riemman Draw Location")
        # Combobox
        self.menu = ttk.Combobox(self.master, textvariable=self.splash, values=[
            "Left", "Right", "Middle"], state="readonly")
        self.menu.grid(row=3, column=3, sticky=EW, pady=2,)

        # CheckButton
        self.is_riemann_check = Checkbutton(
            self.master, text="Riemann", command=self.is_riemann_check)
        self.is_trapezoid_check = Checkbutton(
            self.master, text="Trapezoid", command=self.is_trapezoid_check)
        # Initialized
        self.is_riemann_check.grid(row=0, column=3, sticky=W, pady=2)
        self.is_trapezoid_check.grid(row=1, column=3, sticky=W, pady=2)

        # Breakline
        self.break_line = ttk.Separator(orient=HORIZONTAL)
        self.break_line.grid(row=2, column=3, sticky=EW, pady=2)


    def run_graph(self):
        '''Grab input from tk.entrys'''
        status_s, start_range = self.retrieve_strt()  # statuses are a boolean return
        status_e, end_range = self.retrieve_end()
        status_n, n = self.retrieve_n()
        fx = self.retrieve_fx()
        if status_s and status_e and status_n:
            if end_range > start_range:
                self.error_var.set('')
                graph.draw(start_range, end_range, n,
                        DRAWTYPE, fx, self.menu.get())
                #error_var.set('Invalid Function')
            else:
                self.error_var.set('Invalid Function')


    def run_calculate(self):
        '''Runs integral root'''
        #t = Toplevel()
        #t.title("Hello")
        integral = integral_window.IntegralWindow(
            0, 5, 4, '2*x')

    def is_riemann_check(self):
        '''Reverses the menu disabled from is_trapezoid_check()'''
        global DRAWTYPE
        DRAWTYPE = True
        self.menu.state(['!disabled'])
        self.is_trapezoid_check.deselect()


    def is_trapezoid_check(self):
        ''' disables the Riemann sum menu because Trapezoids only have one state'''
        global DRAWTYPE
        DRAWTYPE = False
        self.menu.state(['disabled'])
        self.is_riemann_check.deselect()


    def retrieve_strt(self):
        '''Does some simple checks before passing strtRange to draw(*args)'''
        try:
            strt_range = float(self.startRangeEntry.get())
        except ValueError:
            self.error_var.set('Input a valid starting range')
            return False, 0
        return True, strt_range


    def retrieve_end(self):
        '''Retrieves endrange of function'''
        try:
            end_range = float(self.endRangeEntry.get())
        except ValueError:
            self.error_var.set('Input a valid end range')
            return False, 0
        return True, end_range


    def retrieve_n(self):
        '''Retrieves number of rectangles wanted'''
        try:
            n = float(self.nEntry.get())
        except ValueError:
            return False, 0
        return True, n


    def retrieve_fx(self):
        '''retrieve function'''
        fx = self.fxEntry.get()
        return fx.lower()


def test_val(in_str, acttyp):
    '''Forces an integer input on n input'''
    if acttyp == '1':  # insert
        if not in_str.isdigit():
            return False
    return True


if __name__ == "__main__":
    root = Tk()
    main_window = MainWindow(root)
    root.mainloop()