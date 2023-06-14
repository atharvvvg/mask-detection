import cv2
import time
import winsound

#import face data given by opencv by default
nose_cap=cv2.CascadeClassifier("C:/Users/athar/AppData/Roaming/Python/Python311/site-packages/cv2/data/haarcascade_mcs_nose.xml")

#to open camera feed
video_cap=cv2.VideoCapture(0)

t1=time.time()
while True:
    ret, video_data=video_cap.read()

    #Convert live feed to greyscale and detect face
    col=cv2.cvtColor(video_data, cv2.COLOR_BGR2GRAY)
    nose=nose_cap.detectMultiScale(
        col,
        scaleFactor=1.1,
        minNeighbors=8,
        minSize=(30,30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    for(x,y,w,h) in nose:
        cv2.rectangle(video_data, (x,y),(x+w,y+h),(0,255,0),2)
        t2=time.time()
        if(t2-t1)>1:
            print("wear your mask stupid")
            frequency = 2500  # Set Frequency To 2500 Hertz
            duration = 100  # Set Duration To 1000 ms == 1 second
            winsound.Beep(frequency, duration)
            t1=time.time()

    #video box
    cv2.imshow("live video feed", video_data)

    #press 'a' to close feed
    if cv2.waitKey(10)==ord("a"):
        break

video_cap.release()