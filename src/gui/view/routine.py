import tkinter as tk
from tkinter import ttk
from src.gui.interfaces import LabelFrame
from src.common import config
from src.gui.theme import Theme


class Routine(LabelFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, 'Routine', **kwargs)

        self.scroll = ttk.Scrollbar(self)
        self.scroll.pack(side=tk.RIGHT, fill='both', pady=5)

        self.listbox = tk.Listbox(self, width=25,
                                  listvariable=config.gui.routine_var,
                                  exportselection=False,
                                  activestyle='none',
                                  yscrollcommand=self.scroll.set,
                                  bg=Theme.ACCENT, fg=Theme.FOREGROUND,
                                  selectbackground=Theme.HIGHLIGHT,
                                  selectforeground=Theme.BACKGROUND,
                                  borderwidth=0, highlightthickness=0)
        self.listbox.bind('<Up>', lambda e: 'break')
        self.listbox.bind('<Down>', lambda e: 'break')
        self.listbox.bind('<Left>', lambda e: 'break')
        self.listbox.bind('<Right>', lambda e: 'break')
        self.listbox.bind('<<ListboxSelect>>', parent.details.show_details)
        self.listbox.pack(side=tk.LEFT, expand=True, fill='both', padx=(5, 0), pady=5)

        self.scroll.config(command=self.listbox.yview)

    def select(self, i):
        self.listbox.selection_clear(0, 'end')
        self.listbox.selection_set(i)
        self.listbox.see(i)
