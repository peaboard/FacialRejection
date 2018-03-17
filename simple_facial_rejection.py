import cv2
import numpy as np
import sys

facePath = "/opt/ros/kinetic/share/OpenCV-3.3.1/haarcascades/haarcascade_frontalface_default.xml"
smilePath = "/opt/ros/kinetic/share/OpenCV-3.3.1/haarcascades/haarcascade_smile.xml"
faceCascade = cv2.CascadeClassifier(facePath)
smileCascade = cv2.CascadeClassifier(smilePath)

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

#sF = 1.05
#sF = 1.2
sF = 1.08

while True:

    ret, frame = cap.read() # Capture frame-by-frame
    img = frame
    result_image = img.copy()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor= sF,
        minNeighbors=8,
        minSize=(55, 55),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    # ---- Draw a rectangle around the faces

    for (x, y, w, h) in faces:
        #cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
        blur_face = frame[y:y+h, x:x+w]
        blur_face = cv2.GaussianBlur(blur_face,(23, 23), 30)
        result_image[y:y+blur_face.shape[0], x:x+blur_face.shape[1]] = blur_face

        #roi_gray = gray[y:y+h, x:x+w]
        #roi_color = frame[y:y+h, x:x+w]



        # smile = smileCascade.detectMultiScale(
        #     roi_gray,
        #     scaleFactor= 1.7,
        #     minNeighbors=22,
        #     minSize=(25, 25),
        #     flags=cv2.CASCADE_SCALE_IMAGE
        #     )

        # # Set region of interest for smiles
        # for (x, y, w, h) in smile:
        #     print "Found", len(smile), "smiles!"
        #     cv2.rectangle(roi_color, (x, y), (x+w, y+h), (255, 0, 0), 1)
        # else: 
        #     print "!!!!!!!!!!!!!!!!!"

    # Blur the face area in the image 
    # Draw the face area in image:
    # cv2.rectangle(imgout, (x0,y0),(x1,y1),(0,255,0),2)
    #blur_face = imgout[y0:y1, x0:x1]
    # apply a gaussian blur on this new recangle image
    #blur_face = cv2.GaussianBlur(blur_face,(23, 23), 30)
    # merge this blurry rectangle to our final image
    #result_image[y0:y0+blur_face.shape[0], x0:x0+blur_face.shape[1]] = blur_face
    #face_file_name = "./face_" + str(y) + ".jpg"
    #cv2.imwrite(face_file_name, blur_face)

    #cv2.flip(result_image, 1)


    cv2.namedWindow("test", cv2.WND_PROP_FULLSCREEN)          
    cv2.setWindowProperty("test", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow('test', result_image)
    c = cv2.waitKey(7) % 0x100
    if c == 27:
        break

cap.release()
cv2.destroyAllWindows()