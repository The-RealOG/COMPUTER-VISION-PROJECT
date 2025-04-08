import cv2 as cv

img = cv.imread('Photos/parrot.jpg') #allows you to read and store selected image as a variable

cv.imshow('Cat', img) #shows the image in a new tab

cv.waitKey(0)

