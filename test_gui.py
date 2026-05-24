import os
import tkinter as tk
from tkinter import ttk
import sys
from unittest.mock import MagicMock, patch

# Mock Windows-specific modules and other dependencies
os.environ['SDL_VIDEODRIVER'] = 'dummy'

mock_win32 = MagicMock()
sys.modules['win32con'] = mock_win32
sys.modules['win32api'] = mock_win32
sys.modules['win32gui'] = mock_win32
sys.modules['ctypes'] = MagicMock()
sys.modules['ctypes.wintypes'] = MagicMock()
sys.modules['keyboard'] = MagicMock()
sys.modules['cv2'] = MagicMock()
sys.modules['mss'] = MagicMock()
sys.modules['PIL'] = MagicMock()
sys.modules['PIL.Image'] = MagicMock()
sys.modules['PIL.ImageTk'] = MagicMock()
sys.modules['torch'] = MagicMock()

# Mock components before importing GUI
with patch('src.modules.bot.Bot'), \
     patch('src.modules.capture.Capture'), \
     patch('src.modules.notifier.Notifier'), \
     patch('src.modules.listener.Listener'), \
     patch('src.common.config'), \
     patch('src.gui.View'), \
     patch('src.gui.Edit'), \
     patch('src.gui.Settings'), \
     patch('src.gui.Menu'):

    # We need to make sure src.modules.bot exists for the import to work if it's imported as a module
    import src.modules.bot
    import src.modules.capture
    import src.modules.notifier
    import src.modules.listener

    from src.modules.gui import GUI

    def test_gui_init():
        root = tk.Tk()
        root.withdraw()

        with patch('tkinter.PhotoImage'):
            gui = GUI()
            print("GUI initialized successfully")

            style = ttk.Style()
            print(f"Current theme: {style.theme_use()}")

        root.destroy()

if __name__ == "__main__":
    test_gui_init()
