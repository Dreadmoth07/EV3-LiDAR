### About The Project
#### Project Context
This was a project made for HackNotts 2025 as our first ever hackathon.
###### HackNotts25
HackNotts25 was a 25 hour overnight hackathon that took place from 12pm on the 25th of October 2025 to 12pm the next day. It was 25 hours due to the daylight-savings time switch happening during the night.
#### Equipment
We did this using a Lego EV3 running EV3dev with the matching Infrared Sensor. The whole project was written in Python.
#### How It Works
The Infrared sensor can estimate distance via an inbuilt mode. Bartosz wrote code to read the data from this to give us a relative distance from the centre. (sensors.py)
The object being scanned is rotated on a turntable that is controlled by one of the two motors. The other motor is used to control the height of the sensor, which allows us to scan the whole object in slices. The code to do this was written by Louise, and the physical structures that allow for this were made by Sam.
The data being output at this point was three data points; the distance, the rotation of the object, and the rotation of the motor containing the height. This needed to be converted into distances, the code of which was again written by Bartosz.
Alex wrote the code to take the coordinate data from a file provided by the above program, and convert it into a 3D model in a format which could be visualised in Blender. He also managed the GitHub Repository and assisted with issues regarding Git.