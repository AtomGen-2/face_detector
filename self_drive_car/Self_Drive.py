import cv2
import random
img_file = 'carBack.jpg'
# Pre-trained car classfier
classfier_file = 'car_detector.xml'
car_tracker = cv2.CascadeClassifier(classfier_file)
# create an opencv image
img = cv2.imread(img_file)
# grayscale
grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# get coordinates of car irrespective of size and scale
car_coordinates = car_tracker.detectMultiScale(grayscaled_img)
print(car_coordinates)
numberofcars = len(car_coordinates)
print(numberofcars)
for i in range(0, numberofcars):
    (x, y, w, h) = car_coordinates[i]
    cv2.rectangle(img, (x, y), (x + w, y + h), (random.randrange(128, 256), random.randrange(128, 256), random.randrange(128, 256)), 2)
# cv2.imshow('name you want to be displayed in loaded image', img)
    cv2.imshow('CarDetector', img)
# the image loads and immediatly closes. We do not want that, so we use the "cv2.waitKey()" to ensure that the image stays and waits until we press a key.
    cv2.waitKey() 
print("code completed")