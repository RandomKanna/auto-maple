import tkinter as tk
from tkinter import ttk

class Theme:
    BACKGROUND = '#21252b'
    FOREGROUND = '#abb2bf'
    ACCENT = '#2c313a'
    HIGHLIGHT = '#61afef'
    BORDER = '#181a1f'

    def __init__(self):
        self.style = ttk.Style()

        # 'clam' is a good base for custom themes in many environments
        try:
            self.style.theme_use('clam')
        except tk.TclError:
            pass

        # Configure TFrame
        self.style.configure('TFrame', background=self.BACKGROUND)

        # Configure TLabel
        self.style.configure('TLabel',
                             background=self.BACKGROUND,
                             foreground=self.FOREGROUND,
                             font=('Helvetica', 10))

        # Configure TButton
        self.style.configure('TButton',
                             background=self.ACCENT,
                             foreground=self.FOREGROUND,
                             borderwidth=1,
                             focusthickness=0,
                             focuscolor=self.HIGHLIGHT,
                             lightcolor=self.BORDER,
                             darkcolor=self.BORDER,
                             font=('Helvetica', 10))
        self.style.map('TButton',
                       background=[('active', self.HIGHLIGHT), ('pressed', self.HIGHLIGHT)],
                       foreground=[('active', self.BACKGROUND)])

        # Configure TNotebook
        self.style.configure('TNotebook',
                             background=self.BORDER,
                             borderwidth=0)
        self.style.configure('TNotebook.Tab',
                             background=self.ACCENT,
                             foreground=self.FOREGROUND,
                             padding=[10, 5],
                             borderwidth=0)
        self.style.map('TNotebook.Tab',
                       background=[('selected', self.BACKGROUND)],
                       foreground=[('selected', self.HIGHLIGHT)])

        # Configure TLabelframe
        self.style.configure('TLabelframe',
                             background=self.BACKGROUND,
                             foreground=self.HIGHLIGHT,
                             borderwidth=1,
                             relief='solid')
        self.style.configure('TLabelframe.Label',
                             background=self.BACKGROUND,
                             foreground=self.HIGHLIGHT,
                             font=('Helvetica', 10, 'bold'))

        # Configure TEntry
        self.style.configure('TEntry',
                             fieldbackground=self.ACCENT,
                             foreground=self.FOREGROUND,
                             insertcolor=self.FOREGROUND,
                             borderwidth=0)

        # Configure TScrollbar
        self.style.configure('TScrollbar',
                             gripcount=0,
                             background=self.ACCENT,
                             troughcolor=self.BACKGROUND,
                             borderwidth=0,
                             arrowsize=10)
