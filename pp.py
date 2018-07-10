import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))
 
time.sleep(0.1)
 
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	image = frame.array
 

	cv2.imshow("Frame", image)
	key = cv2.waitKey(1) & 0xFF
 
	# clear the stream in preparation for the next frame
	rawCapture.truncate(0)
 
	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break

