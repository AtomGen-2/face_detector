# import the library opencv
# OPENCV is a open source computer vision librabry maintained by the people, which contains a lot of pre trained data sets
import cv2
# load some pre-trained data on face frontals from opencv (haar cascade algorithms)
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# Classifier basically means a detector. It is an object that can detect or classify stuff as a face or not.
# Choose an image to detect face in (imread = imageRead)
# images are basically an array of numbers [pixels are reporesented as numbers]
img = cv2.imread('rdj.jpg')
# we need to convert images into grayscale, because thats the only way with which you can identify images in opencv { not in color }
grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Detect faces
face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)


# cv2.imshow('name you want to be displayed in loaded image', img)
cv2.imshow('FaceDetector', grayscaled_img)
# the image loads and immediatly closes. We do not want that, so we use the "cv2.waitKey()" to ensure that the image stays and waits until we press a key.
cv2.waitKey()

print("Code Completed")