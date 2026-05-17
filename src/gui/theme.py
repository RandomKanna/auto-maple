import tkinter as tk
from tkinter import ttk

# Modern Dark Theme Colors
BACK = '#21252b'
FORE = '#abb2bf'
ACCENT = '#2c313a'
HIGHLIGHT = '#61afef'
BORDER = '#181a1f'


def apply_theme(root):
    """
    Applies a modern dark theme to the provided Tkinter root window.
    Sets default styles for both standard Tkinter widgets and Ttk widgets.
    """

    root.configure(bg=BACK)

    # Ttk Style configuration
    style = ttk.Style()
    style.theme_use('clam')  # 'clam' is a good base for customization

    # Ttk Notebook
    style.configure('TNotebook', background=BACK, borderwidth=0)
    style.configure('TNotebook.Tab',
                    background=ACCENT,
                    foreground=FORE,
                    padding=[15, 5],
                    font=('Segoe UI', 10),
                    borderwidth=0)
    style.map('TNotebook.Tab',
              background=[('selected', BACK), ('active', HIGHLIGHT)],
              foreground=[('selected', HIGHLIGHT), ('active', BACK)])

    # Ttk LabelFrame
    style.configure('TLabelframe',
                    background=BACK,
                    foreground=FORE,
                    relief='flat',
                    borderwidth=1,
                    bordercolor=BORDER)
    style.configure('TLabelframe.Label',
                    background=BACK,
                    foreground=HIGHLIGHT,
                    font=('Segoe UI', 11, 'bold'))

    # Ttk Button
    style.configure('TButton',
                    background=ACCENT,
                    foreground=FORE,
                    padding=[10, 5],
                    font=('Segoe UI', 9),
                    borderwidth=0)
    style.map('TButton',
              background=[('active', HIGHLIGHT), ('pressed', BORDER)],
              foreground=[('active', BACK)])

    # Ttk Scrollbar
    style.configure('TScrollbar',
                    background=ACCENT,
                    arrowcolor=FORE,
                    troughcolor=BACK,
                    borderwidth=0)

    # Apply to standard Tkinter widgets via option_add (defaults)
    root.option_add('*Background', BACK)
    root.option_add('*Foreground', FORE)
    root.option_add('*Font', ('Segoe UI', 9))
    root.option_add('*Entry.Background', ACCENT)
    root.option_add('*Entry.Foreground', FORE)
    root.option_add('*Entry.relief', 'flat')
    root.option_add('*Entry.insertBackground', FORE)
    root.option_add('*Text.Background', ACCENT)
    root.option_add('*Text.Foreground', FORE)
    root.option_add('*Text.relief', 'flat')
    root.option_add('*Listbox.Background', ACCENT)
    root.option_add('*Listbox.Foreground', FORE)
    root.option_add('*Listbox.selectBackground', HIGHLIGHT)
    root.option_add('*Listbox.selectForeground', BACK)
    root.option_add('*Listbox.relief', 'flat')
    root.option_add('*Listbox.borderwidth', 0)
    root.option_add('*Label.Background', BACK)
    root.option_add('*Label.Foreground', FORE)
    root.option_add('*Button.Background', ACCENT)
    root.option_add('*Button.Foreground', FORE)
    root.option_add('*Button.activeBackground', HIGHLIGHT)
    root.option_add('*Button.activeForeground', BACK)
    root.option_add('*Button.relief', 'flat')
    root.option_add('*Button.borderwidth', 0)
    root.option_add('*Menu.Background', BACK)
    root.option_add('*Menu.Foreground', FORE)
    root.option_add('*Menu.activeBackground', HIGHLIGHT)
    root.option_add('*Menu.activeForeground', BACK)
    root.option_add('*Menu.relief', 'flat')
    root.option_add('*Menu.borderwidth', 0)
