import cv2 as cv
import pa2_2
import matplotlib.pyplot as pyp
image1 = "./example images/colortransfer/scotland_house.jpg"
image2 = "./example images/colortransfer/scotland_plain.jpg"

firstImage = cv.imread(image1)
secondImage = cv.imread(image2)

cv.imshow('result',pa2_2.colorTransfer(firstImage, secondImage))
cv.waitKey()
