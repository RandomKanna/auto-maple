"""A module for detecting and notifying the user of dangerous in-game events."""

import config
import utils
import time
import cv2
import pygame
import threading
import numpy as np
import keyboard as kb


# Other players' symbols on the minimap
OTHER_RANGES = (
    ((0, 245, 215), (10, 255, 255)),
)
other_filtered = utils.filter_color(cv2.imread('assets/other_template.png'), OTHER_RANGES)
OTHER_TEMPLATE = cv2.cvtColor(other_filtered, cv2.COLOR_BGR2GRAY)

# The Elite Boss's warning sign
ELITE_TEMPLATE = cv2.imread('assets/elite_template.jpg', 0)


class Notifier:
    def __init__(self):
        """Initializes this Notifier object's main thread."""

        pygame.mixer.init()
        self.mixer = pygame.mixer.music

        self.ready = False
        self.thread = threading.Thread(target=self._main)
        self.thread.daemon = True

    def start(self):
        """Starts this Notifier's thread."""

        print('\n[~] Started notifier.')
        self.thread.start()

    def _main(self):
        self.ready = True
        prev_others = 0
        while True:
            if config.enabled:
                frame = config.capture.frame
                height, width, _ = frame.shape
                minimap = config.capture.minimap['minimap']

                # Check for unexpected black screen
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                if np.count_nonzero(gray < 15) / height / width > 0.95:
                    self._alert()

                # Check for elite warning
                elite_frame = frame[height // 4:3 * height // 4, width // 4:3 * width // 4]
                elite = utils.multi_match(elite_frame, ELITE_TEMPLATE, threshold=0.9)
                if len(elite) > 0:
                    self._alert()

                # Check for other players entering the map
                filtered = utils.filter_color(minimap, OTHER_RANGES)
                others = len(utils.multi_match(filtered, OTHER_TEMPLATE, threshold=0.7))
                if others != prev_others:
                    if others > prev_others:
                        self._ding()
                    prev_others = others
            time.sleep(0.05)

    def _alert(self):
        """
        Plays an alert to notify user of a dangerous event. Stops the alert
        once the key bound to 'Start/stop' is pressed.
        """

        config.enabled = False
        config.listener.enabled = False
        self.mixer.load('./assets/alert.mp3')
        self.mixer.set_volume(0.75)
        self.mixer.play(-1)
        while not kb.is_pressed(config.listener.key_binds['Start/stop']):
            time.sleep(0.1)
        self.mixer.stop()
        time.sleep(2)
        config.listener.enabled = True

    def _ding(self):
        """A quick notification for when another player enters the map."""

        self.mixer.load('./assets/ding.mp3')
        self.mixer.set_volume(0.50)
        self.mixer.play()
