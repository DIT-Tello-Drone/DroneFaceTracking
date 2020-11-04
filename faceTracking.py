from utils import *


# init drone
myDrone = initTello()

### getting image from tello

#declare width and height for image
w, h = 360, 240


while True:
    #get frame
    img = telloGetFrame(myDrone, dim)

    #call find face
    img = findFace(img)

    cv2.imshow('img', img)

    # stop the drone on q kay (safety measure)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        myDrone.land()
        break







#track face