#Resize given image

# importing cv2 
import cv2

img = cv2.imread('Resources/background.png')

print('Original Dimensions : ',img.shape)
 
scale_percent = 30 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
  
# resize image
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
 
print('Resized Dimensions : ',resized.shape)
 
cv2.imshow("Resized image", resized)


# Wait for the user to press a key
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()



# Display the results of height and width reduction of an image to 30% of its current height
# and width.
# output in console and image window