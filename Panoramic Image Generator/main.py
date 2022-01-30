from helper import *

# Read images

img1 = cv2.imread('building1.jpg')  # L
img2 = cv2.imread('building2.jpg')  # C
img3 = cv2.imread('building3.jpg')  # R


# Laplace blending
middle_lpb = Image_Stitching().laplace(img1, img2)
final_lpb = Image_Stitching().laplace(middle_lpb, img3)

cv2.imwrite('laplace.jpeg', final_lpb)
