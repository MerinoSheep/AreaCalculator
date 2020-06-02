'''main.py'''
# TODO limit eval
from tkinter import Checkbutton, Tk, ttk, StringVar, Label, Button, Entry, W, EW, HORIZONTAL
import graph
import integral_window


class MainWindow():
    '''Parent window'''
    def __init__(self, master):
        self.master = master
        self.error_var = StringVar()
        self.draw_type = None
        # Labels
        self.fx_text = Label(self.master, text="Function")
        self.start_range_text = Label(self.master, text="Start Range")
        self.end_range_text = Label(self.master, text="End Range")
        self.n_text = Label(self.master, text="N")
        self.error_text = Label(
            self.master, fg="red", textvariable=self.error_var, font='bold')

        # Initialize Labels to grid
        self.fx_text.grid(row=0, column=0)
        self.start_range_text.grid(row=1, column=0)
        self.end_range_text.grid(row=2, column=0)
        self.n_text.grid(row=3, column=0)
        self.error_text.grid(row=4, column=3)

        # Button
        self.graph_button = Button(
            self.master, text="Graph", command=self.run_graph)
        self.graph_button.grid(row=4, column=1, pady=2)
        self.calculate_button = Button(
            self.master, text="Calculate", command=self.run_calculate)
        self.calculate_button.grid(row=4, column=0, pady=2)
        # Text Entry Fields
        self.start_range_entry = Entry(self.master, validate="key")
        self.end_range_entry = Entry(self.master)
        self.n_entry = Entry(self.master, validate="key")
        self.n_entry['validatecommand'] = (
            self.n_entry.register(self.test_val), '%P', '%d')
        self.fx_entry = Entry(self.master)

        # Initialized to Grid
        self.fx_entry.grid(row=0, column=1, sticky=W, pady=2)
        self.start_range_entry.grid(row=1, column=1, sticky=W, pady=2)
        self.end_range_entry.grid(row=2, column=1, stick=W, pady=2)
        self.n_entry.grid(row=3, column=1, stick=W, pady=2)

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
        status_s, strt_val = self.val_strt()  # statuses are a boolean return
        status_e, end_val = self.val_end()
        status_n, n_val = self.val_n()
        status_fx, fx = self.val_fx()
        if not status_s:
            self.error_var.set('Invalid Start Range')
            return False, []
        elif not status_e:
            self.error_var.set('Invalid End Range')
            return False, []
        elif not status_n:
            self.error_var.set("Invalid N")
            return False, []
        elif not status_fx:
            self.error_var.set("Invalid Function")
            return False, []
        elif int(self.start_range_entry.get()) > int(self.end_range_entry.get()):
            self.error_var.set("Invalid Range")
            return False, []
        return True, [strt_val, end_val, n_val, fx]

    def run_graph(self):
        '''Grab input from tk.entrys'''
        is_good, argum = self.validate()
        if is_good:
            self.error_var.set('')
            graph.draw(*argum, self.draw_type, self.menu.get(), self) # pylint: disable=no-value-for-parameter
            # error_var.set('Invalid Function')
        else:
            self.error_var.set("Invalid Parameter")
    def run_calculate(self):
        '''Runs integral root'''
        is_good, argum = self.validate()
        if is_good:
            integral_window.IntegralWindow(*argum) # pylint: disable=no-value-for-parameter
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
            strt_range = float(self.start_range_entry.get())
        except ValueError:
            # self.error_var.set('Input a valid starting range')
            return False, None
        else:
            return True, strt_range

    def val_end(self):
        '''Retrieves endrange of function'''
        try:
            end_range = float(self.end_range_entry.get())
        except ValueError:
            # self.error_var.set('Input a valid end range')
            return False, None
        else:
            return True, end_range

    def val_n(self):
        '''Retrieves and validates number of rectangles wanted'''
        try:
            n = int(self.n_entry.get())
        except ValueError:
            return False, None
        else:
            return True, n

    def val_fx(self):
        '''retrieve function'''
        temp_fx = self.fx_entry.get().lower().replace("^", "**")
        fx = ''
        for i in range(0, len(temp_fx)-1):
            fx += temp_fx[i]
            if temp_fx[i].isdigit() and (temp_fx[i+1] == 'x' or temp_fx[i+1] == '(' or temp_fx[i+1].isalpha()):
                fx += '*'
        fx += temp_fx[-1]
        return True, fx

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
