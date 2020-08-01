from tkinter import BooleanVar, Toplevel, W
from tkinter.ttk import Entry, Label, Checkbutton, Button
import configparser
import vcmdtk

class SettingsWindow(Toplevel):
    def __init__(self) -> None:
        Toplevel.__init__(self)
        self.title("Settings")
        #self.geometry("300x180")
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')
        self.val_int_cmd = (self.register(vcmdtk.test_int),'%d', '%S')
        self.create_gui()
        self.load_settings()
        self.grid_gui()

    def create_gui(self):
        #Label

        self.y_max_label = Label(self, text='Y max')
        self.y_min_label = Label(self, text='Y min')
        #Entry
        self.y_max_entry = Entry(self, validate='key',validatecommand=self.val_int_cmd)
        self.y_min_entry = Entry(self, validate='key', validatecommand=self.val_int_cmd)
        #Check buttons
        self.check_var_1 = BooleanVar()
        self.check_var_1.set(self.config.getboolean('Y Limits', 'use_auto_values'))
        self.auto_y_cbutton = Checkbutton(self, text='Use auto Y-value ranges', variable=self.check_var_1, command=self.auto_y)
        #buttons
        self.ok_button = Button(self, text='Ok', command=self.ok_command)
        self.cancel_button = Button(self, text='Cancel', command=self.destroy)
    def grid_gui(self):
        self.y_max_label.grid(row=0, column=0, pady=2)
        self.y_min_label.grid(row=1, column=0, pady=2)
        self.y_max_entry.grid(row=0, column=1, pady=2)
        self.y_min_entry.grid(row=1, column=1, pady=2)
        self.auto_y_cbutton.grid(row=0, column=2, columnspan=2, sticky=W)
        self.ok_button.grid(row=2, column=2)
        self.cancel_button.grid(row=2, column=3)
    def auto_y(self):
        '''configures values afor check button'''
        if self.check_var_1.get(): #if checked
            state = 'disabled'
        else:
            state = 'enabled'
        self.y_max_entry['state'] = state
        self.y_min_entry['state'] = state
    def load_settings(self): #Inserts settings values(if not none) to tk.entry widghets
        if (x:= self.config['Y Limits']['y_max']) != 'None':
            self.y_max_entry.insert(0, x)
        if (x:= self.config['Y Limits']['y_min']) != 'None':
            self.y_min_entry.insert(0, x)
        self.auto_y() #disables entry if required after setting values


    def ok_command(self):
        '''writes values inputed to config file'''
        if not self.check_var_1.get(): #If not using auto y values write y values into ini file
            if self.y_max_entry.get(): #if not empty
                self.config.set('Y Limits', 'y_max', self.y_max_entry.get())
            if self.y_min_entry.get():
                self.config.set('Y Limits', 'y_min', self.y_min_entry.get())
        self.config.set('Y Limits', 'use_auto_values', str(self.check_var_1.get()))

        with open('config.ini', 'w') as configfile:
            self.config.write(configfile)

        self.destroy()

if __name__ == "__main__":
    pass
