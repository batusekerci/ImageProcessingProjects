import numpy as np
import cv2

inputImage = cv2.imread('france.png')

def meanFilter(inputImage, filterSize):
    outputImage = np.zeros(inputImage.shape, np.uint8)

    height = inputImage.shape[0]
    width = inputImage.shape[1]

    result = 0.0
    # Setting temp variable for different filter size
    if filterSize == 9:  # mean filter for 3x3
        temp = 1  # Temporary variable to use in loop
        n = 3  # n is from n x n .For this if block, it is n=3 from 3x3.
    elif filterSize == 25:  # mean filter for 5x5
        temp = 2
        n = 5

    elif filterSize == 49:  # mean filter for 7x7
        temp = 3
        n = 7

    elif filterSize == 81:  # mean filter for 9x9
        temp = 4
        n = 9

    else:
        temp = 1
        n = 3

    for j in range(temp, height - temp):
        for i in range(temp, width - temp):
            for y in range(-temp, (-temp + n)):
                for x in range(-temp, (-temp + n)):
                    result = result + inputImage[j + y, i + x]
            outputImage[j][i] = result / filterSize

            result = 0.0

    return outputImage


mean_3x3 = meanFilter(inputImage, 9)

# mean_5x5 = meanFilter(inputImage, 25)

# mean_7x7 = meanFilter(inputImage, 49)
#
# mean_9x9 = meanFilter(inputImage, 81)
#
cv2.imwrite("mean3.png", mean_3x3)
# cv2.imwrite("mean.png", mean_5x5)
# cv2.imwrite("mean7.png", mean_7x7)
# cv2.imwrite("mean9.png", mean_9x9)
