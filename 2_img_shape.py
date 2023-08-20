#Display Dimensions of image

# importing cv2 
import cv2

img = cv2.imread("images/Catching.jpg")

# get dimensions of image
dimensions = img.shape
 
# height, width, number of channels in image
height = img.shape[0]
width = img.shape[1]
channels = img.shape[2]
 
print('Image Dimension    : ',dimensions)
print('Image Height       : ',height)
print('Image Width        : ',width)
print('Number of Channels : ',channels)
print('Number of Pixel : ',img.size)


# Write down the dimensions of an image
# output
#  give only the console values