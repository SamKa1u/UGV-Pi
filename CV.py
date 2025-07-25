import time
from ultralytics import YOLO
from config import LABEL_MAP
import torch
import cv2


class ObjectTrack:
    def __init__(self, shared, model_path):
        self.shared = shared
        
        #load model from hub
        # self.model = torch.hub.load("ultralytics/yolov5", "yolov5s")

        # load from pt
        self.model = YOLO("yolov5su.pt")
        
    def run(self):
        while True:
            # retrieve shared frame
            frame = self.shared.get("frame")
            # print("[CV]", frame)
            if frame is None:
                time.sleep(.01)
                continue

            # run model inference
            results = self.model.predict(frame, conf=.60, imgsz=480, max_det=1, verbose=False)
            for result in results:
                boxes = result.boxes.cls.tolist()
                bbox = result.boxes.xyxy.tolist()
                if boxes:
                    label = int(boxes[0])
                    obj = LABEL_MAP.get(label, None)
                    if obj:
                        print(f"[Object Track] Detected: {obj} at: {bbox[0]}")
                        self.shared["object"]["name"] = obj
                        self.shared["object"]["bbox"] = bbox[0]
                    else:
                        self.shared["object"]["name"] = None
                        self.shared["object"]["bbox"] = None
            time.sleep(.5)

