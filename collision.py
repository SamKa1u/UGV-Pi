from gpiozero import DistanceSensor
from time import sleep
from config import COLLISION_DIST

class CollisionDetect:
    def __init__(self, shared):
        self.shared = shared
        self.ultra = DistanceSensor(echo=24, trigger=23)
    
    def run(self):
        while True:
            dist = self.ultra.distance * 100
            if dist <= COLLISION_DIST:
                print('[collison]--! COLLISION DETECTED', dist)
                self.shared["collision"] = True
            else:
                self.shared["collision"] = False
                sleep(.05)

