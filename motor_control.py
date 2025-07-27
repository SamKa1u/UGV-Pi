from config import URL, SWIVEL_LEFT, SWIVEL_RIGHT, FORWARDS, BACK, STOP, BACK_RIGHT,BACK_LEFT,TURN_RIGHT,TURN_LEFT
import requests
import random

class Control:
    def __init__(self, shared):
        self.shared = shared  
        
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
            rand = random.randint(0, 1)
            lateral = self.shared["motion"]["lateral"]
            f_b = self.shared["motion"]["f_b"]
            
            if rand == 0:
                rand = -1

            if self.shared.get("collision") == True:
                self.cmd(rand, -1)
            else:
                self.cmd(lateral, f_b)
