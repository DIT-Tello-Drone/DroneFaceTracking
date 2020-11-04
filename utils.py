from djitellopy import Tello
import cv2

# params
# w,h
width = 360
height = 240

dim = (width, height)

# connect to drone
# set starting params
def initTello():
    myDrone = Tello()
    myDrone.connect()

    #set velicties to 0
    myDrone.for_back_velocity = 0
    myDrone.left_right_velocity = 0
    myDrone.up_down_velocity = 0
    myDrone.yaw_velocity = 0
    myDrone.speed = 0

    # get battery status
    print(myDrone.get_battery())

    # turn off stream
    myDrone.streamoff()

    # stream on
    myDrone.streamon()
    return myDrone

    #get image; (drone, image dimentions)



### get frame from camera
def telloGetFrame(myDrone, dim ):
    frame = myDrone.get_frame_read()
    frame = frame.frame

    # resize using cv2
    img = cv2.resize(frame, dim)
    return img

def findFace(img):
    print('image passed in to this function is: ' )
    print(img) # Image loaded OK
    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    print('faceCascade variable is empty? ')
    print(faceCascade.empty())

    # convert to grayscale
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    print('ingGray variable is: ')
    print(imgGray)

    # detect
    faces = faceCascade.detectMultiScale(imgGray, 1.2, 4)
    print('faces')
    print(faces) # THIS is empty!?

    #find all faces and draw rectangle (image, position 1, position 2, colour, thickness)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        return img