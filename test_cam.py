import thread
import cv2
import sys
import serial
import time
import numpy as np
import socket

#Can be done using TCP and node.js(libmraa)
#s = socket.socket()         # Create a socket object
#host = '192.168.1.150' # Get local machine name
#port = 1337                # Reserve a port for your service.
#s.connect((host, port))
#def send_data(x,y):


 #s.send(str(np.asscalar(x)).encode()+"#"+str(np.asscalar(y)).encode())
 #print s.recv(1024)




ser = serial.Serial('COM5', 9600, timeout=0) #Change port and baud rate

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')  #Select the proper example file from OpenCV directories
frame_no = 0
video_capture = cv2.VideoCapture(1) #Select the appropriate Video Capture device
print "Frame default resolution: (" + str(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH)) + "; " + str(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT)) + ")"

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    frame_no +=1
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2 ,
        minNeighbors=25,
        minSize=(30,30)

    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        print str(np.asscalar(x)) + "x "
        print y
        #try:
        #    thread.start_new_thread(send_data, (x, y))
        #except:
        #    print "No send data moi"
        ser.write(str(np.asscalar(x)).encode()+"\n"+str(np.asscalar(y)).encode())


    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        ser.write("0\n0");
        break


# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
#s.close