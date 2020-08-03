'''main.py'''
# TODO limit eval
from tkinter import Tk, ttk, StringVar, Label, W, EW, HORIZONTAL, IntVar
from tkinter.ttk import Button, Combobox, Radiobutton, Entry
from typing import Tuple, Union
import graph
import integral_window
import settingswindow
import vcmdtk

class MainWindow():
    '''Parent window'''

    def __init__(self, master: Tk):  # TODO CLEAN INIT
        self.master = master
        self.error_var = StringVar()
        self.draw_type = True # Defaults to Riemann Sum
        self.master.title('Area Calculator')
        val_float_cmd = (self.master.register(vcmdtk.test_float),'%d', '%S', '%s')
        # Labels
        self.fx_text = Label(self.master, text="Function")
        self.start_range_text = Label(self.master, text="Start Range")
        self.end_range_text = Label(self.master, text="End Range")
        self.n_text = Label(self.master, text="N")
        self.error_text = Label(
            self.master, fg="red", textvariable=self.error_var, font=(None, 12))
        # Buttons
        self.graph_button = Button(
            self.master, text="Graph", command=self.run_graph)
        # Calculate Button
        self.calculate_button = Button(
            self.master, text="Calculate", command=self.run_calculate)
        # Settings Button
        self.settings_button = Button(
            self.master, text='Settings', command=lambda:settingswindow.SettingsWindow())
        # Help Button
        self.help_button = Button(self.master, text='Help')
        # Text Entry Fields
        self.start_range_entry = Entry(self.master, validate="key", validatecommand=val_float_cmd)
        self.end_range_entry = Entry(self.master, validate="key", validatecommand=val_float_cmd)
        self.n_entry = Entry(self.master, validate='key', validatecommand=(self.master.register(vcmdtk.test_int), '%d', '%S'))

        self.fx_entry = Entry(self.master)
        self.splash = StringVar(self.master)
        self.splash.set('Riemman Draw Location')
        self.menu = Combobox(self.master, textvariable=self.splash, values=[
            "Left", "Right", "Middle"], state="readonly", width=22)
        # CheckButton

        self.tk_int_var = IntVar(value=0)
        self.is_riemann_check_box = Radiobutton(
            self.master, text="Riemann", value=0, variable=self.tk_int_var, command=self.radio_selection)
        self.is_trapezoid_check_box = Radiobutton(
            self.master, text="Trapezoid", value=1, variable=self.tk_int_var, command=self.radio_selection)
        # Breakline
        self.break_line = ttk.Separator(orient=HORIZONTAL)
        self.grid_gui()

    def grid_gui(self):
        '''grids widgets'''
        self.fx_text.grid(row=0, column=0)
        self.is_riemann_check_box.grid(
            row=0, column=3, sticky=W, pady=2, padx=(4, 0),columnspan=2)
        self.fx_entry.grid(row=0, column=1, sticky=W, pady=2)
        self.start_range_text.grid(row=1, column=0)
        self.start_range_entry.grid(row=1, column=1, sticky=W, pady=2)
        self.is_trapezoid_check_box.grid(
            row=1, column=3, sticky=W, pady=2, padx=(4, 0))
        self.end_range_text.grid(row=2, column=0)
        self.end_range_entry.grid(row=2, column=1, stick=W, pady=2)
        self.break_line.grid(row=2, column=3, sticky=EW, pady=2, padx=(4, 5))
        self.n_text.grid(row=3, column=0)
        self.n_entry.grid(row=3, column=1, stick=W, pady=2)
        self.menu.grid(row=3, column=3, sticky=EW, pady=2, padx=(4, 2))
        self.calculate_button.grid(row=4, column=0, pady=2)
        self.graph_button.grid(row=4, column=1, pady=2, sticky=W)
        self.error_text.grid(row=4, column=3)
        self.settings_button.grid(row=5, column=0)
        self.help_button.grid(row=5, column=1, sticky=W, pady=2)

    def validate(self):
        '''Grab input from tk.entrys'''
        status_s, strt_val = self.val_float(self.start_range_entry.get())  # statuses are a boolean return
        status_e, end_val = self.val_float(self.end_range_entry.get())
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

    def run_graph(self) -> None:
        '''Grab input from tk.entrys'''
        is_good, argum = self.validate()
        if is_good:
            self.error_var.set('')
            graph.draw(*argum, self.draw_type, self.menu.get(), self)  # pylint: disable=no-value-for-parameter

    def radio_selection(self) -> None:
        '''switches state of draw_type and combobox'''
        selection = self.tk_int_var.get()
        if selection == 0:
            self.draw_type = True
            self.menu.state(['!disabled'])
        elif selection == 1:
            self.draw_type = False
            self.menu.state(['disabled'])

    def run_calculate(self) -> None:
        '''Runs integral root'''
        is_good, argum = self.validate()
        if is_good:
            integral_window.IntegralWindow(*argum)  # pylint: disable=no-value-for-parameter

    def val_float(self, entry:str):
        '''checks for entry'''
        if entry:
            return True, float(entry)
        else:
            return False, None

    def val_n(self) -> Tuple[bool, Union[None, int]]:
        '''Retrieves and validates number of rectangles wanted'''
        if self.n_entry.get():
            return True, int(self.n_entry.get())
        else:
            return False, None

    def val_fx(self) -> Tuple[bool, str]:
        '''retrieve function'''
        temp_fx = self.fx_entry.get().lower()
        if temp_fx == '':
            return False, temp_fx
        temp_fx = temp_fx.replace("^", "**").replace("log", "log10").replace("ln", "log")
        fx = ''
        for i in range(0, len(temp_fx)-1):
            fx += temp_fx[i]
            if temp_fx[i].isdigit() and (temp_fx[i+1] == 'x' or temp_fx[i+1] == '(' or temp_fx[i+1].isalpha()):
                fx += '*'
        fx += temp_fx[-1]
        return True, fx
if __name__ == "__main__":
    root = Tk()
    main_window = MainWindow(root)
    root.mainloop()
