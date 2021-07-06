import cv2
webcam = cv2.VideoCapture(0)

# cv2.namedWindow("Window")

def make_1080p():
    webcam.set(3, 1920)
    webcam.set(4, 1080)


def change_res(width, height):
    webcam.set(3, width)
    webcam.set(4, height)

# make_1080p()
change_res(4000, 2000)

while True:
    ret, frame = webcam.read()
    grayscaled_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("NormalFrame", frame)
    # cv2.imshow("GrayScaleFrame", grayscaled_frame)
    #This breaks on 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()