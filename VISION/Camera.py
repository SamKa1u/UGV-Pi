import cv2
from picamera2 import Picamera2
import time

class CameraStream:
    def __init__(self, shared):
        # initialize shared dictionary and picamera
        self.shared = shared
        self.cam = Picamera2()
        
    def run(self):
        # start stream
        self.cam.start(show_preview=True)
        while True:
            # capture as array
            frame = self.cam.capture_array()
            if frame is None:
                print('[Camera]--(!) No captured frame')
                continue
#             frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#             cv2.imshow("frame", frame_rgb)
#             print(frame_rgb)
            # store validated frame
            self.shared["frame"] = frame # _rgb
            time.sleep(.01)
            
    def __del__(self):
        cv2.destroyAllWindows()
            
            

