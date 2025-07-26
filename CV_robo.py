import supervision as sv
import time
from PIL import Image
from rfdetr import RFDETRNano
from rfdetr.util.coco_classes import COCO_CLASSES


class ObjectTrack:
    def __init__(self, shared):
        self.shared = shared
        self.model = RFDETRNano(pretrain_weights="MODELS/rf-detr-nano.pth")

    def run(self):
        while True:
#             print(type(self.model))
#             print("[CV_robo] Start")
# 
            frame = self.shared.get("frame")
#             print("[CV_robo]", frame)
            
            if frame is None:
                print("[CV_robo]-! No frame received")
                continue
            
            detections = self.model.predict(frame, threshold=0.3)
            print("[CV_robo]", detections)

            labels = [
                f"{COCO_CLASSES[class_id]} {confidence:.2f}"
                for class_id, confidence
                in zip(detections.class_id, detections.confidence)
            ]
            print("[CV_robo] Labels", labels)

            annotated_frame = frame.copy()
            annotated_frame = sv.BoxAnnotator().annotate(annotated_frame, detections)
            annotated_frame = sv.LabelAnnotator().annotate(annotated_frame, detections, labels)
            self.shared["annotated"] = annotated_frame

            time.sleep(.5)
