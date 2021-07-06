import cv2

# static
filename = 'video.avi'
frames_per_second = 24.0
my_res = '4k'
# dictionary
STD_DIMENSIONS = {
    "480p": (640, 480),
    "720p": (1280, 720), 
    "1080p": (1920, 1080), 
    "4k": (3840, 2160),
}

# change resolution
def change_res(webcam, width, height):
    webcam.set(3, width)
    webcam.set(4, height)


def get_dims(webcam, res):
    width, height = STD_DIMENSIONS["480p"]
    if res in STD_DIMENSIONS:
        width,height = STD_DIMENSIONS[res]
    ## change the current caputre device
    ## to the resulting resolution
    change_res(webcam, width, height)
    print(height, width)
    return width, height


webcam = cv2.VideoCapture(0)
dims = get_dims(webcam, my_res)
while(True):
    ret, frame = webcam.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()