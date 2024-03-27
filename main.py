import cv2 as cv
import sys 

img = cv.imread(cv.samples.findFile("starry_night.jpg"))
if img is None:
    sys.exit("Could'nt read the iamge ")
cv.imshow("Display Window",img)
k = cv.waitKey(0)
if k == ord("s"):
    img = cv.imwrite("starry_night.jpg",img)
