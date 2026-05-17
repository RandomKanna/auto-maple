import tkinter as tk
from src.gui.interfaces import LabelFrame


class Status(LabelFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, 'Status', **kwargs)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(3, weight=1)

        self.curr_cb = tk.StringVar()
        self.curr_routine = tk.StringVar()

        self.cb_label = tk.Label(self, text='Command Book:')
        self.cb_label.grid(row=0, column=1, padx=5, pady=(5, 2), sticky=tk.E)
        self.cb_display = tk.Label(self, textvariable=self.curr_cb, bg='#2c313a', anchor=tk.W, padx=5)
        self.cb_display.grid(row=0, column=2, padx=(0, 5), pady=(5, 2), sticky=tk.EW)

        self.r_label = tk.Label(self, text='Routine:')
        self.r_label.grid(row=1, column=1, padx=5, pady=(2, 5), sticky=tk.E)
        self.r_display = tk.Label(self, textvariable=self.curr_routine, bg='#2c313a', anchor=tk.W, padx=5)
        self.r_display.grid(row=1, column=2, padx=(0, 5), pady=(2, 5), sticky=tk.EW)

    def set_cb(self, string):
        self.curr_cb.set(string)

    def set_routine(self, string):
        self.curr_routine.set(string)
