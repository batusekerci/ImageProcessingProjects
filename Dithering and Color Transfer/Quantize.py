import numpy as np
import cv2 as cv
import pa1_2
pathOfImage = "./example images/dithering/1.png"

myImage = cv.imread(pathOfImage, cv.IMREAD_GRAYSCALE)

height, width = myImage.shape
quantizedImage = np.zeros_like(myImage)

q = 55

for j in range(0, width):
    for i in range(0, height):
        oldPixel = myImage[i][j]
        quantizedImage[i][j] = round(q * oldPixel / 255) * int(255 / q)

cv.imshow("Quantized", quantizedImage)
cv.waitKey()


cv.imshow("Dithered", pa1_2.FloydSteinberg(myImage, q))
cv.waitKey()
