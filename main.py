import cv2
from CV import ObjectTrack
from config import MODEL_PATH
import threading
import time

shared_state = {
    "frame": None,
    "object": {
        "name" : None,
        "bbox" : None,
    },
}

def text_format(label, x1, x2, y2):
    fnt_scale = 5
    t_width = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, fnt_scale, 2)[0][0]
    t_height = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, fnt_scale, 2)[0][1]
    if t_width < x2-x1 and t_height < y2-(y2-40):
        return fnt_scale
    else:
        while t_width > x2-x1 or t_height > (y2-(y2-40)):
            fnt_scale *= .85
            t_width = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, fnt_scale, 2)[0][0]
            t_height = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, fnt_scale, 2)[0][1]
        return  fnt_scale

def main():
    cam = cv2.VideoCapture(0)
    if not cam.isOpened():
        print("Cannot open camera")
        exit()

    while True:
        ret, frame = cam.read()
        if ret is None:
            print('[main_cam]-(!) frame skipped')
            continue
        shared_state["frame"] = frame

        if shared_state["object"]["name"] is None:
            cv2.imshow("frame", frame)

            k = cv2.waitKey(1)
            if k == 27:
                break

            time.sleep(.05)
            continue
        else:
            font = cv2.FONT_HERSHEY_SIMPLEX
            label = shared_state["object"]["name"]
            x1 = shared_state["object"]["bbox"][0]
            y1 = shared_state["object"]["bbox"][1]
            x2 = shared_state["object"]["bbox"][2]
            y2 = shared_state["object"]["bbox"][3]
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (255,0,0), 2)
            cv2.rectangle(frame, (int(x1), int(y2) - 40), (int(x2), int(y2)), (255, 0, 0), -1)
            fnt_scale = text_format(label, int(x1), int(x2), int(y2))
            cv2.putText(frame, label, (int(x1), int(y2) - 10), font, fnt_scale, (255, 255, 255), 2)
            cv2.imshow("frame", frame)

            k = cv2.waitKey(1)
            if k == 27:
                break
            time.sleep(.05)

if __name__ == '__main__':
    # --- Start CV Thread ---
    tracker = ObjectTrack(shared_state, model_path=MODEL_PATH)
    tracker_thread = threading.Thread(target=tracker.run, daemon=True)
    tracker_thread.start()


    # --- Start Camera in main Thread ---
    main()
