import tkinter as tk
from src.gui.interfaces import LabelFrame, Frame
from src.common.interfaces import Configurable


class ExpSettings(LabelFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, 'Experience', **kwargs)

        self.exp_settings = ExpSettings('exp')
        self.auto_exp = tk.BooleanVar(value=self.exp_settings.get('Auto-exp'))
        self.exp_duration = tk.StringVar(value=self.exp_settings.get('Exp duration'))
        self.exp_type = tk.StringVar(value=self.exp_settings.get('Exp type'))

        exp_row = Frame(self)
        exp_row.pack(side=tk.TOP, fill='x', expand=True, pady=5, padx=5)
        check = tk.Checkbutton(
            exp_row,
            variable=self.auto_exp,
            text='Auto-exp',
            command=self._on_change
        )
        check.pack()

        duration_row = Frame(self)
        duration_row.pack(side=tk.TOP, fill='x', expand=True, pady=(0, 5), padx=5)
        label = tk.Label(duration_row, text='Select experience duration:')
        label.pack(side=tk.LEFT, padx=(0, 15))
        duration_group = Frame(duration_row)
        duration_group.pack(side=tk.LEFT)

        durations = [('15 min', '15min'), ('30 min', '30min'), ('1 hour', '1hour')]
        for duration, value in durations:
            radio = tk.Radiobutton(
                duration_group,
                text=duration,
                variable=self.exp_duration,
                value=value,
                command=self._on_change
            )
            radio.pack(side=tk.LEFT, padx=(0, 10))

        type_row = Frame(self)
        type_row.pack(side=tk.TOP, fill='x', expand=True, pady=(0, 5), padx=5)
        label = tk.Label(type_row, text='Select experience type:')
        label.pack(side=tk.LEFT, padx=(0, 15))
        type_group = Frame(type_row)
        type_group.pack(side=tk.LEFT)

        types = [('MVP Exp', 'mvp_exp'), ('Mush Exp', 'mush_exp'), ('VIP Exp', 'vip_exp')]
        for exp_type, value in types:
            radio = tk.Radiobutton(
                type_group,
                text=exp_type,
                variable=self.exp_type,
                value=value,
                command=self._on_change
            )
            radio.pack(side=tk.LEFT, padx=(0, 10))

    def _on_change(self):
        self.exp_settings.set('Auto-exp', self.auto_exp.get())
        self.exp_settings.set('Exp duration', self.exp_duration.get())
        self.exp_settings.set('Exp type', self.exp_type.get())
        self.exp_settings.save_config()


class ExpSettings(Configurable):
    DEFAULT_CONFIG = {
        'Auto-exp': False,
        'Exp duration': '15min',
        'Exp type': 'mvp_exp'
    }

    def get(self, key):
        return self.config[key]

    def set(self, key, value):
        assert key in self.config
        self.config[key] = value
