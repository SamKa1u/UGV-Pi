import cv2
from VISION.Camera import CameraStream
from VISION.CV import ObjectTrack
from config import MODEL_PATH, LABEL_MAP
import threading

shared_state = {
    "frame": None,
    "Object": None,
}

# --- Start Camera Thread ---
camera = CameraStream(shared_state)
camera_thread = threading.Thread(target=camera.run, daemon=True)
camera_thread.start()
    
# --- Start CV Thread ---
tracker = ObjectTrack(shared_state, model_path=MODEL_PATH)
tracker_thread = threading.Thread(target=camera.run, daemon=True)
tracker_thread.start()
