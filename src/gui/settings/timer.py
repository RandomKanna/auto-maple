import tkinter as tk
from tkinter import ttk
from src.gui.interfaces import LabelFrame, Frame
from src.common import config, settings
from src.common.interfaces import Configurable

class Timer(LabelFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, 'Schedule', **kwargs)

        self.settings = TimerSettings('timer')
        config.enabled_schedule = self.settings.config['Enabled']
        config.start_time = self.settings.config['Start time']
        config.stop_time = self.settings.config['Stop time']

        self.enabled_var = tk.BooleanVar(value=config.enabled_schedule)
        self.start_var = tk.StringVar(value=config.start_time)
        self.stop_var = tk.StringVar(value=config.stop_time)

        # Enable/Disable Schedule
        self.enable_row = Frame(self)
        self.enable_row.pack(side=tk.TOP, fill='x', expand=True, padx=5, pady=5)

        self.enable_check = ttk.Checkbutton(
            self.enable_row,
            text='Enable Schedule',
            variable=self.enabled_var,
            command=self._save_settings
        )
        self.enable_check.pack(side=tk.LEFT)

        # Start Time
        self.start_row = Frame(self)
        self.start_row.pack(side=tk.TOP, fill='x', expand=True, padx=5, pady=5)

        self.start_label = ttk.Label(self.start_row, text='Start Time (HH:MM):')
        self.start_label.pack(side=tk.LEFT, padx=(0, 5))

        self.start_entry = ttk.Entry(self.start_row, textvariable=self.start_var, width=10)
        self.start_entry.pack(side=tk.LEFT)
        self.start_entry.bind('<FocusOut>', lambda e: self._save_settings())
        self.start_entry.bind('<Return>', lambda e: self._save_settings())

        # Stop Time
        self.stop_row = Frame(self)
        self.stop_row.pack(side=tk.TOP, fill='x', expand=True, padx=5, pady=5)

        self.stop_label = ttk.Label(self.stop_row, text='Stop Time (HH:MM):')
        self.stop_label.pack(side=tk.LEFT, padx=(0, 5))

        self.stop_entry = ttk.Entry(self.stop_row, textvariable=self.stop_var, width=10)
        self.stop_entry.pack(side=tk.LEFT)
        self.stop_entry.bind('<FocusOut>', lambda e: self._save_settings())
        self.stop_entry.bind('<Return>', lambda e: self._save_settings())

    def _save_settings(self):
        """Validates and saves the timer settings."""

        try:
            config.enabled_schedule = self.enabled_var.get()
            config.start_time = settings.validate_time(self.start_var.get())
            config.stop_time = settings.validate_time(self.stop_var.get())

            self.settings.config['Enabled'] = config.enabled_schedule
            self.settings.config['Start time'] = config.start_time
            self.settings.config['Stop time'] = config.stop_time
            self.settings.save_config()

            print(f"\n[~] Schedule updated: {config.enabled_schedule} ({config.start_time} - {config.stop_time})")
        except ValueError as e:
            print(f"\n[!] Invalid time format: {e}")
            # Reset UI to current config values if invalid
            self.start_var.set(config.start_time)
            self.stop_var.set(config.stop_time)


class TimerSettings(Configurable):
    DEFAULT_CONFIG = {
        'Enabled': False,
        'Start time': '00:00',
        'Stop time': '00:00'
    }
