import numpy as np
import cv2
from matplotlib import pyplot as plt

cap = cv2.VideoCapture(0)

def background_subtraction():
    fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()
    while(1):
        ret, frame = cap.read()
        fgmask = fgbg.apply(frame)
        cv2.imshow('original', frame)
        cv2.imshow('frame',fgmask)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
    cap.release()
    cv2.destroyAllWindows()

def hand_recognition():
    while (1):
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        # ret, thresh1 = cv2.threshold(blur, 70, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
        ret, thresh1 = cv2.threshold(blur, 70, 255, cv2.THRESH_OTSU)
        thresh3 = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

        # cv2.imshow('original', frame)
        cv2.imshow('blur', blur)
        cv2.imshow('threshold', thresh1)
        # cv2.imshow('adaptive threshold', thresh3)

        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
    cap.release()
    cv2.destroyAllWindows()

def skin_extraction():
    # first we need to detect the face
    face_cascade = cv2.CascadeClassifier('../classifier/haarcascade_frontalface_default.xml')
    while (1):
        ret, frame = cap.read()

        # Z = frame.reshape((-1, 3))
        # # convert to np.float32
        # Z = np.float32(Z)
        #
        # # define criteria, number of clusters(K) and apply kmeans()
        # criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
        # K = 2
        # ret, label, center = cv2.kmeans(Z, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
        #
        # # Now convert back into uint8, and make original image
        # center = np.uint8(center)
        # res = center[label.flatten()]
        # res2 = res.reshape((frame.shape))
        #
        # cv2.imshow('res2', res2)


        # draw rectangles around faces
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        ret, thresh = cv2.threshold(blur, 127, 255, cv2.THRESH_BINARY)
        thresh3 = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            # for x_value in range(x, x + w):
            #     for y_value in range(y, y + h):
            #         frame[y_value, x_value] = thresh[y_value, x_value]
            frame[y: y + h, x: x + w] = np.array(hsv[y: y + h, x: x + w])

        # hist = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])
        # plt.imshow(hist, interpolation='nearest')
        # plt.show()


        # find colors within rectangle, blur them, find threshold of color that's skin color, then apply a mask.

        # after mask has been applied, detect color again of just within the mask

        cv2.imshow('img', frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    cap.release()
    cv2.destroyAllWindows()

def take_image(imageName):
    ret, frame = cap.read()
    cv2.imwrite(imageName, frame)

# hand_recognition()
# background_subtraction()
skin_extraction()