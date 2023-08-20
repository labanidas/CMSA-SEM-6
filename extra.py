# importing required libraries of opencv
import cv2

# importing library for plotting
from matplotlib import pyplot as plt

try:
    # reads an input image
    img = cv2.imread('images/high_contrast_image.webp', 0)

    if img is None:
        raise Exception("Unable to open or read the image file.")
    # find frequency of pixels in range 0-255
    histr = cv2.calcHist([img], [0], None, [256], [0, 256])

    # show the plotting graph of an image
    plt.plot(histr)
    plt.show()

except Exception as e:
    print("Error:", str(e))