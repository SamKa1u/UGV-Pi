from picamera2 import Picamera2
from CV_robo import ObjectDetect
from tracking import ObjectTracker
from config import x1,x2,y1,y2, OBJECT
import threading
import time
import cv2


# initialize Picamera
cam = Picamera2()
config = cam.create_preview_configuration({'format': 'BGR888'})
cam.configure(config)

 
# define shared state
shared_state = {
"frame": None,
"annotated": None,
"detections": None,
}

# --- Start CV Thread ---
detector = ObjectDetect(shared_state)
detector_thread = threading.Thread(target=detector.run, daemon=True)
detector_thread.start()

# --- Start Tracking Thread ---
tracker = ObjectTracker(shared_state)
tracker_thread = threading.Thread(target=tracker.run, daemon=True)
tracker_thread.start()

cam.start()
while True:
    frame = cam.capture_array()
    if frame is None:
        print('[main_cam]-(!) frame skipped')
        continue

    # store validated frame in shared state
    shared_state["frame"] = frame.copy()
    
    # get annotated frame from shared state
    annotated = shared_state.get("annotated")
    
    # replace frame with annotated if available
    if annotated is not None:
        frame = annotated
    
    # add ROI to frame
    cv2.rectangle(frame,(x1,y1),(x2,y2),(0,0,0),3)
    cv2.putText(frame, "Object of Interest: " + OBJECT, (5,470), cv2.FONT_HERSHEY_SIMPLEX, .75, (255,255,255),2)
 
    # display frame for viewing
    cv2.imshow("frame", cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    k = cv2.waitKey(1)
    if k == 27:
        break
        
    time.sleep(.05)
   
cv2.destroyAllWindows()

