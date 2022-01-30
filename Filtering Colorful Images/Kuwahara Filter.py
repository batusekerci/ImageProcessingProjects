import numpy as np
import cv2 as cv

readImage = cv.imread('france.png')


def kuwaharaFilterFunction(image, kernel_size=5):
    height, width, channel = image.shape[0], image.shape[1], image.shape[2]

    r = int((kernel_size - 1) / 2)

    # Padding operation
    image = np.pad(image, ((r, r), (r, r), (0, 0)), "edge")

    average, variance = cv.integral2(image)
    average = (average[:-r - 1, :-r - 1] + average[r + 1:, r + 1:] -
               average[r + 1:, :-r - 1] - average[:-r - 1, r + 1:]) / (r +
                                                                       1) ** 2
    variance = ((variance[:-r - 1, :-r - 1] + variance[r + 1:, r + 1:] -
                 variance[r + 1:, :-r - 1] - variance[:-r - 1, r + 1:]) /
                (r + 1) ** 2 - average ** 2).sum(axis=2)

    def filter(i, j):
        return np.array([
            average[i, j], average[i + r, j], average[i, j + r], average[i + r,
                                                                         j + r]
        ])[(np.array([
            variance[i, j], variance[i + r, j], variance[i, j + r],
            variance[i + r, j + r]
        ]).argmin(axis=0).flatten(), j.flatten(),
            i.flatten())].reshape(width, height, channel).transpose(1, 0, 2)

    filtered_image = filter(*np.meshgrid(np.arange(height), np.arange(width)))

    filtered_image = filtered_image.astype(image.dtype)
    filtered_image = filtered_image.copy()

    return filtered_image


output3 = kuwaharaFilterFunction(readImage, 3)
# output5 = kuwaharaFilterFunction(readImage, 5)
# output7 = kuwaharaFilterFunction(readImage, 7)
# output9 = kuwaharaFilterFunction(readImage, 9)
#
#
cv.imwrite("kuw3.png", output3)
# cv.imwrite("kuw5.png", output5)
# cv.imwrite("kuw7.png", output7)
# cv.imwrite("kuw9.png", output9)
