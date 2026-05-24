import cv2
import numpy as np
import torch
from src.common import utils

class YOLO:
    def __init__(self, model_path='assets/models/yolo_rune.pt'):
        try:
            # Assuming YOLOv5 or v8
            self.model = torch.hub.load('ultralytics/yolov5', 'custom', path=model_path)
            self.ready = True
        except Exception as e:
            print(f"[!] Failed to load YOLO model: {e}")
            self.ready = False

    def detect(self, image):
        if not self.ready:
            return []

        results = self.model(image)
        # results.xyxy[0] is n x 6 tensor (x1, y1, x2, y2, conf, cls)
        detections = results.xyxy[0].cpu().numpy()

        # Sort by x coordinate to get the sequence of arrows
        detections = detections[detections[:, 0].argsort()]

        label_map = {0: 'up', 1: 'down', 2: 'left', 3: 'right'}
        return [label_map[int(d[5])] for d in detections]
