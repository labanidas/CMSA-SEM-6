#Read and display image

# importing cv2 
import cv2

# Using cv2.imread() method
# Using 0 to read image in grayscale mode
img = cv2.imread("images/Catching.JPG", 0)
# Displaying the image
cv2.imshow('image', img)

# Using 1 to read image in color mode
img = cv2.imread("images/Catching.jpg", 1)
# Displaying the image
cv2.imshow('image1', img)

# Wait for the user to press a key
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()


# Read and display an image.
# output
# 1   show greyscale image of catching
# 2   show image in color mode