import numpy as np
def FloydSteinberg(image,qValue):
    height, width = image.shape
    newImage = image.copy()

    for i in range(0, height - 1):
        for j in range(1, width - 1):

            oldPixel = newImage[i][j]
            newPixel = round(qValue * oldPixel / 255) * int(255 / qValue)
            newImage[i][j] = newPixel

            error = oldPixel - newPixel

            newImage[i][j + 1   ] = np.clip(newImage[i][j + 1   ] + round(error * 7 / 16),0,255)
            newImage[i + 1][j - 1] = np.clip(newImage[i + 1][j - 1] + round(error * 3 / 16),0,255)
            newImage[i + 1   ][j ] = np.clip(newImage[i + 1   ][j ]  + round(error * 5 / 16),0,255)
            newImage[i + 1][j + 1] = np.clip(newImage[i + 1][j + 1] + round(error * 1 / 16),0,255)

    return newImage
