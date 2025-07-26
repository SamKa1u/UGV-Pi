from picamera2 import Picamera2
from CV_robo import ObjectTrack
from config import MODEL_PATH
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
}

# --- Start CV Thread ---
tracker = ObjectTrack(shared_state)
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
        
    cv2.imshow("frame", frame)
    k = cv2.waitKey(1)
    if k == 27:
        break
        
    time.sleep(.05)
    
cv2.destroyAllWindows()
