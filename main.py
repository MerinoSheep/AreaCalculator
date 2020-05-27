'''main.py'''
# TODO limit eval
from tkinter import Checkbutton, Tk, ttk, StringVar, Label, Button, Entry, W, EW, HORIZONTAL, Frame
import graph
import integral_window





class MainWindow():
    '''Parent window'''
    def __init__(self,master):
        self.master = master
        self.error_var = StringVar()
        self.draw_type = None
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
            self.master, text="Calculate", command=self.run_calculate)
        self.calculate_button.grid(row=4, column=0, pady=2)
        # Text Entry Fields
        self.startRangeEntry = Entry(self.master, validate="key")
        self.endRangeEntry = Entry(self.master)
        self.nEntry = Entry(self.master, validate="key")
        self.nEntry['validatecommand'] = (
            self.nEntry.register(self.test_val), '%P', '%d')
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
        self.is_riemann_check_box = Checkbutton(
            self.master, text="Riemann", command=self.is_riemann_check)
        self.is_trapezoid_check_box = Checkbutton(
            self.master, text="Trapezoid", command=self.is_trapezoid_check)
        # Initialized
        self.is_riemann_check_box.grid(row=0, column=3, sticky=W, pady=2)
        self.is_trapezoid_check_box.grid(row=1, column=3, sticky=W, pady=2)

        # Breakline
        self.break_line = ttk.Separator(orient=HORIZONTAL)
        self.break_line.grid(row=2, column=3, sticky=EW, pady=2)

    def validate(self):  # TODO optimize return
        '''Grab input from tk.entrys'''
        status_s = self.val_strt()  # statuses are a boolean return
        status_e = self.val_end()
        status_n = self.val_n()
        fx = self.val_fx()
        if not status_s:
            self.error_var.set('Invalid Start Range')
            return False
        elif not status_e:
            self.error_var.set('Invalid End Range')
            return False
        elif not status_n:
            self.error_var.set("Invalid N")
            return False
        elif not fx:
            self.error_var.set("Invalid Function")
            return False
        elif int(self.startRangeEntry.get()) > int(self.endRangeEntry.get()):
            self.error_var.set("Invalid Range")
            return False
        return True

    def run_graph(self):
        '''Grab input from tk.entrys'''
        if self.validate():
            self.error_var.set('')
            graph.draw(float(self.startRangeEntry.get()), float(self.endRangeEntry.get()), int(self.nEntry.get()),
                       self.draw_type, self.fxEntry.get(), self.menu.get())
            # error_var.set('Invalid Function')

    def run_calculate(self):
        '''Runs integral root'''

        integral_window.IntegralWindow(
            0, 5, 4, '2*x')

    def is_riemann_check(self):
        '''Reverses the menu disabled from is_trapezoid_check()'''
        self.draw_type = True
        self.menu.state(['!disabled'])
        self.is_trapezoid_check_box.deselect()

    def is_trapezoid_check(self):
        ''' disables the Riemann sum menu because Trapezoids only have one state'''
        self.draw_type = False
        self.menu.state(['disabled'])
        self.is_riemann_check_box.deselect()

    def val_strt(self):
        '''Does some simple checks before returning a boolean'''
        try:
            strt_range = float(self.startRangeEntry.get())
        except ValueError:
            # self.error_var.set('Input a valid starting range')
            return False
        else:
            return True

    def val_end(self):
        '''Retrieves endrange of function'''
        try:
            end_range = float(self.endRangeEntry.get())
        except ValueError:
            # self.error_var.set('Input a valid end range')
            return False
        else:
            return True,

    def val_n(self):
        '''Retrieves number of rectangles wanted'''
        try:
            n = float(self.nEntry.get())
        except ValueError:
            return False
        else:
            return True

    def val_fx(self):
        '''retrieve function'''
        fx = self.fxEntry.get()
        return fx.lower()

    def test_val(self, in_str, acttyp):
        '''Forces an integer input on n input'''
        if acttyp == '1':  # insert
            if not in_str.isdigit():
                return False
        return True


if __name__ == "__main__":
    root = Tk()
    main_window = MainWindow(root)
    root.mainloop()
