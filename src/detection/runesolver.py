import cv2
import numpy as np
import os
from src.common import utils
from src.detection.yolo import YOLO

class RuneSolver:
    def __init__(self):
        self.yolo = YOLO()
        self.assets_path = 'assets/runes'
        self.templates = {
            'up': cv2.imread(os.path.join(self.assets_path, 'up.png'), 0),
            'down': cv2.imread(os.path.join(self.assets_path, 'down.png'), 0),
            'left': cv2.imread(os.path.join(self.assets_path, 'left.png'), 0),
            'right': cv2.imread(os.path.join(self.assets_path, 'right.png'), 0)
        }

    def solve(self, frame):
        """
        Solves the rune puzzle using YOLO detection or template matching as fallback.
        :param frame:   The input frame.
        :return:        A list of arrow directions.
        """
        # 1. Try YOLO first
        if self.yolo.ready:
            solution = self.yolo.detect(frame)
            if solution and len(solution) == 4:
                print(f"[~] YOLO detected solution: {solution}")
                return solution

        # 2. Fallback to Template Matching if YOLO fails or is not ready
        print("[~] YOLO failed or not ready, falling back to template matching...")
        return self._template_solve(frame)

    def _template_solve(self, frame):
        """
        A simple template matching implementation for arrow detection.
        """
        if frame is None:
            return []

        # Preprocessing: Color filtering can help isolate arrows
        # MapleStory arrows are usually bright and distinctive
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # Assuming a range that captures the arrows (adjust as needed)
        mask = cv2.inRange(hsv, (0, 50, 50), (180, 255, 255))
        processed = cv2.bitwise_and(frame, frame, mask=mask)
        gray = cv2.cvtColor(processed, cv2.COLOR_BGR2GRAY)

        # Crop to the middle-top where runes usually appear
        height, width = gray.shape[:2]
        roi = gray[height//4:height//2, width//4:3*width//4]

        detections = []
        for direction, template in self.templates.items():
            if template is None:
                continue
            res = cv2.matchTemplate(roi, template, cv2.TM_CCOEFF_NORMED)
            threshold = 0.6
            loc = np.where(res >= threshold)
            for pt in zip(*loc[::-1]):
                detections.append({'dir': direction, 'x': pt[0], 'score': res[pt[1], pt[0]]})

        if not detections:
            return []

        # Simple filtering and sorting
        detections.sort(key=lambda x: x['score'], reverse=True)

        # Keep only unique arrows by position
        unique_detections = []
        for d in detections:
            is_new = True
            for u in unique_detections:
                if abs(d['x'] - u['x']) < 20:
                    is_new = False
                    break
            if is_new:
                unique_detections.append(d)

        unique_detections.sort(key=lambda x: x['x'])
        final_solution = [d['dir'] for d in unique_detections[:4]]

        if len(final_solution) == 4:
            print(f"[~] Template matching detected solution: {final_solution}")
        return final_solution if len(final_solution) == 4 else []
