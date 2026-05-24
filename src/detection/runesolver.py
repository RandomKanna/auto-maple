import cv2
import numpy as np
from src.common import utils
from src.detection.yolo import YOLO

class RuneSolver:
    def __init__(self):
        self.yolo = YOLO()

    def solve(self, frame):
        """
        Solves the rune puzzle using YOLO detection.
        :param frame:   The input frame.
        :return:        A list of arrow directions.
        """
        if self.yolo.ready:
            return self.yolo.detect(frame)
        return []
