import numpy as np
import cv2

def camera_functions():

    # find camera or webcam
    cap = cv2.VideoCapture(0)

    def save_video(videoName):
        # Define the codec and create VideoWriter object
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter(videoName, fourcc, 20.0, (640,480))

        while(cap.isOpened()):
            # Capture frame-by-frame
            ret, frame = cap.read()
            if ret:
                out.write(frame)

                # Display the frame; if color-converted,
                # replace frame param with the converted frame, e.g. gray
                cv2.imshow('Video Test', frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                break

        # When everything done, release the capture
        cap.release()
        out.release()
        cv2.destroyAllWindows()

    def play_grayscale_video():
        while (True):
            # Capture frame-by-frame
            ret, frame = cap.read()

            # Any color conversions you want here
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Display the resulting frame
            cv2.imshow('frame', gray)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # When everything done, release the capture
        cap.release()
        cv2.destroyAllWindows()

    save_video('test.avi')
camera_functions()