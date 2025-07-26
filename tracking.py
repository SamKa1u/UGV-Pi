from config import x1,x2,y1,y2, OBJECT, URL, SWIVEL_LEFT, SWIVEL_RIGHT, FORWARDS, BACK, STOP, BACK_RIGHT,BACK_LEFT,TURN_RIGHT,TURN_LEFT, AREA_TOLERANCE, CENTER_X_TOLERANCE
import time
import requests
from rfdetr.util.coco_classes import COCO_CLASSES

class ObjectTracker:
    def __init__(self, shared):
        self.shared = shared   
        self.ROIarea = (x2-x1)*(y2-y1)
        self.centerX = 320
        self.centerY = 240
        
    def cmd(self, lateral, f_b):
        if lateral == 1 and f_b == 0:
            requests.get(URL+SWIVEL_RIGHT)
            
        elif lateral == -1 and f_b == 0:
            requests.get(URL+SWIVEL_LEFT)
            
        elif lateral == 0 and f_b == 1:
            requests.get(URL+FORWARDS)
            
        elif lateral == 0 and f_b == -1:
            requests.get(URL+BACK)
            
        elif lateral == 1 and f_b == 1:
            requests.get(URL+TURN_RIGHT)
            
        elif lateral == -1 and f_b == -1:
            requests.get(URL+BACK_RIGHT)
            
        elif lateral == 1 and f_b == -1:
            requests.get(URL+BACK_LEFT)
            
        elif lateral == -1 and f_b == 1:
            requests.get(URL+TURN_LEFT)
            
        else:
            requests.get(URL+STOP)
        
    def run(self):
        while True:
            # retrieve detections from shared state
            detect = self.shared.get("detections")
#             print("[Tracking]", detect)
            
            # compute object bbox center
            if detect is not None:
                xys = detect.xyxy
                labels = detect.class_id
                
                if len(xys) != 0:
                    label_idx = labels[0]
                    obj_x1 = xys[0][0]
                    obj_y1 = xys[0][1]
                    obj_x2 = xys[0][2]
                    obj_y2 = xys[0][3]
#                     print(obj_x1, obj_y1, obj_x2, obj_y2)
                    obj_centerX = obj_x1+(obj_x2-obj_x1)/2
                    obj_area = (obj_x2-obj_x1)*(obj_y2-obj_y1)
#                     obj_centerY = obj_y1+(obj_y2-obj_y1)/2
#                     print(obj_centerX) #, obj_centerY

                    if COCO_CLASSES[label_idx] == OBJECT:
                # ------Lateral motion planning
                        # if object center is to the right of camera center pivot right (R back | L forwards) 
                        if obj_centerX >= self.centerX+CENTER_X_TOLERANCE:
                            print("[Tracking]--Moving Right")
                            lateral = 1
                        # if object center is to the left of camera center pivot left (R forwards | L back) 
                        elif obj_centerX <= self.centerX-CENTER_X_TOLERANCE:
                            print("[Tracking]--Moving Left")
                            lateral = -1
                        # stop lateral motion
                        else:
                            print("[Tracking]--No lateral")
                            lateral = 0
      
                        
                # ------Forward motion planning    
                        # if object area is less than ROI area move forwards (R forwards | L forwards) 
                        if obj_area < self.ROIarea-AREA_TOLERANCE:
                            print("[Tracking]--Moving Up")
                            f_b = 1
                            
                        # if object area is greater than ROI area move back (R back | L back) 
                        elif obj_area > self.ROIarea+AREA_TOLERANCE:
                            print("[Tracking]--Moving Back")
                            f_b = -1
                        # stop front/back motion
                        else:
                            print("[Tracking]--No front/back")
                            f_b = 0
                            
                        self.cmd(lateral, f_b)
                        
            time.sleep(.05)

            


