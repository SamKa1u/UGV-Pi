# ------- config

# Object of interest
OBJECT = "person" #cat person

# ROI
if OBJECT == "person":
    x1 = 245
    x2 = 395
    y1 = 20
    y2 = 460
else:
    x1 = 245
    x2 = 395
    y1 = 165
    y2 = 315
    
# tolerances
AREA_TOLERANCE = 2500
CENTER_X_TOLERANCE = 50
COLLISION_DIST = 25

# UGV base-URL and json commands
URL = "http://192.168.4.1/js?json="

SWIVEL_LEFT = "{%22T%22:1,%22L%22:-0.3,%22R%22:0.3}"
SWIVEL_RIGHT = "{%22T%22:1,%22L%22:0.3,%22R%22:-0.3}"
FORWARDS = "{%22T%22:1,%22L%22:0.3,%22R%22:0.3}"
BACK = "{%22T%22:1,%22L%22:-0.3,%22R%22:-0.3}"
STOP = "{%22T%22:1,%22L%22:0,%22R%22:0}"

BACK_RIGHT = "{%22T%22:1,%22L%22:-0.3,%22R%22:-.15}"
BACK_LEFT = "{%22T%22:1,%22L%22:-0.15,%22R%22:-0.3}"
TURN_RIGHT = "{%22T%22:1,%22L%22:.35,%22R%22:.1}"
TURN_LEFT = "{%22T%22:1,%22L%22:.1,%22R%22:.35}"
