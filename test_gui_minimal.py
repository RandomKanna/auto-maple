import tkinter as tk
from tkinter import ttk
import sys
from unittest.mock import MagicMock

# Mock everything
sys.modules['src.common'] = MagicMock()
sys.modules['src.common.config'] = MagicMock()
sys.modules['src.gui.theme'] = MagicMock()
from src.gui.theme import Theme
Theme.BACKGROUND = '#21252b'

class MockTab:
    def __init__(self, *args, **kwargs): pass
    def pack(self, *args, **kwargs): pass

sys.modules['src.gui'] = MagicMock()
sys.modules['src.gui.view'] = MagicMock()
sys.modules['src.gui.edit'] = MagicMock()
sys.modules['src.gui.settings'] = MagicMock()
sys.modules['src.gui.menu'] = MagicMock()

import os
os.environ['SDL_VIDEODRIVER'] = 'dummy'

def test_imports():
    files = [
        'src/gui/view/details.py',
        'src/gui/view/routine.py',
        'src/gui/view/status.py',
        'src/gui/edit/commands.py',
        'src/gui/edit/components.py',
        'src/gui/edit/controls.py',
        'src/gui/edit/main.py',
        'src/gui/edit/record.py',
        'src/gui/edit/status.py',
        'src/gui/settings/pets.py'
    ]

    for f in files:
        print(f"Checking {f}...")
        with open(f, 'r') as file:
            content = file.read()
            if 'ttk.' in content and 'from tkinter import ttk' not in content:
                print(f"FAILED: {f} is missing ttk import")
                sys.exit(1)
    print("All files have correct imports!")

if __name__ == "__main__":
    test_imports()
