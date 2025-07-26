# UGV-Pi

   A project utilizing the Waveshare Rover kit and a Pi-5 for object detection and person following.

## Description

### Hardware

* Waveshare Rover kit
* Raspberry pi 5
* Arducam

### Dependencies

* opencv-python
* supervision
* rfdetr
* picamera2


### Executing program

#### Clone the repo from cmd line in a project directory of your choosing on your raspberry pi-5
```
git clone https://github.com/SamKa1u/Web-Server-Rover.git
```

####  Connect to the UGV AP from the pi
  <img src="images/UGV.png">

#### Get the IP address of your wave rover and modify the URL variable in config.py to reach it

```
# UGV base-URL and json commands
URL = "http://192.168.4.1/js?json="
```

####  You can change the object of interest by modifying the OBJECT variable in config.py, once this is selected run main.py
```
# Object of interest
OBJECT = "person"
```


## Author


Samuel Kalu
  
* email : [samkalu@ttu.edu](mailto:samkalu@ttu.edu)
* linkedin : [@SamuelKalu](https://www.linkedin.com/in/samuel-kalu-74a359342/)


## Inspiration, code snippets, etc.

* [Wiki](https://www.waveshare.com/wiki/General_Driver_for_Robots)
* [Timestocome](https://github.com/timestocome/RaspberryPi-Robot/tree/master/Hardware)
* [Roboflow](https://github.com/roboflow/rf-detr)
* [Saral Tayal](https://www.instructables.com/Object-Finding-Personal-Assistant-Robot-Ft-Raspber/)
* [Lukas Biewald](https://www.oreilly.com/content/how-to-build-a-robot-that-sees-with-100-and-tensorflow/)
