import cv2 as cv
import numpy as np

image1 = cv.imread('france.png')


def convolutionFunction(inputImage, kernel):
    imageWidth = inputImage.shape[0]
    imageHeight = inputImage.shape[1]
    kernelWidth = kernel.shape[0]
    kernelHeight = kernel.shape[1]
    padX = (kernelWidth - 1) // 2
    padY = (kernelHeight - 1) // 2

    # Creating identity matrix
    resultImage = np.ones((imageWidth, imageHeight, 3))
    # Creating zero matrix
    padImg = np.zeros((imageWidth + (2 * padX), imageHeight + (2 * padX), 3))

    padImgW = padImg.shape[0]
    padImgH = padImg.shape[1]
    padImg[padX:padImgW - padX, padY:padImgH - padY] = inputImage

    # iteration through the image; convolution of the image and kernel
    for i in range(imageWidth):
        for j in range(imageHeight):
            # Calculation for every channel
            resultImage[i, j, 0] = np.sum(kernel * padImg[i:i + kernelWidth, j:j + kernelHeight, 0])
            resultImage[i, j, 1] = np.sum(kernel * padImg[i:i + kernelWidth, j:j + kernelHeight, 1])
            resultImage[i, j, 2] = np.sum(kernel * padImg[i:i + kernelWidth, j:j + kernelHeight, 2])

    # returns the filtered image
    return resultImage


def gaussianFilter(inputImage, sigma):
    kernel = np.zeros((sigma, sigma))

    # Apply the gaussian function by iterating
    for i in range(sigma):
        for j in range(sigma):
            kernel[i, j] = (1 / (2 * np.pi * (sigma ** 2)) * np.exp(
                -(((i ** 2) + (j ** 2)) / (2 * (sigma ** 2)))))  # 2D Gaussian Function

    result = convolutionFunction(inputImage, kernel)

    # Scaling the image
    scaledImage = 255 * (result / np.max(result))



    # cv.imwrite("gaus3.png", scaledImage)
    # cv.imwrite("gaus5.png", scaledImage)
    # cv.imwrite("gaus7.png", scaledImage)
    cv.imwrite("gaus9.png", scaledImage)

    return scaledImage


# gaus_3x3 = gaussianFilter(image1, 3)  # sigma of 3
# gaus_5x5 = gaussianFilter(image1, 5)  # sigma of 5
# gaus_7x7 = gaussianFilter(image1, 7)  # sigma of 7
gaus_9x9 = gaussianFilter(image1, 9)  # sigma of 9



