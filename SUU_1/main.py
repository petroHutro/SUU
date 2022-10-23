from imutils.video import VideoStream
import imutils
import cv2
import time


def face_capture():
    filter_face = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    filter_eye = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
    vs = VideoStream(src=0).start()
    time.sleep(2.0)

    while True:
        frame = vs.read()
        frame = imutils.resize(frame, width=600)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = filter_face.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=10,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )

        for (x, y, width, height) in faces:
            cv2.rectangle(frame, (x, y), (x + width, y + height), (255, 255, 0), 2)
            img_eyes = gray[y:y+height, x:x+width]
            eyes = filter_eye.detectMultiScale(
                img_eyes,
                scaleFactor=1.1,
                minNeighbors=19,
                flags=cv2.CASCADE_SCALE_IMAGE
            )
            for (x_e, y_e, width_e, height_e) in eyes:
                cv2.rectangle(frame, (x + x_e, y + y_e), (x + x_e + width_e, y + y_e + height_e), (255, 255, 0), 2)
        cv2.imshow('Faces', frame)

        if cv2.waitKey(1) == ord('q'):
            break

    vs.stop()
    cv2.destroyAllWindows()


def main():
    face_capture()


if __name__ == '__main__':
    main()
