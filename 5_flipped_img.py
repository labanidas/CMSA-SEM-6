#Resize given image

# importing cv2 
import cv2
import matplotlib.pyplot as plt
from PIL import Image


img = Image.open("images/Catching.jpg")
hori_flippedImage = img.transpose(Image.FLIP_LEFT_RIGHT)
Vert_flippedImage = img.transpose(Image.FLIP_TOP_BOTTOM)
degree_flippedImage = img.rotate(45)
degree90_flippedImage = img.transpose(Image.ROTATE_90)


imgs = [img, hori_flippedImage, Vert_flippedImage, degree_flippedImage, degree90_flippedImage]
title = ['Original', 'horizontally_flipped', 'Vertically_flipped', 'specifying degree', '90degree_flipped']


plt.subplot(2, 3, 1)
plt.title(title[0])
plt.imshow(imgs[0])
plt.xticks([])
plt.yticks([])

plt.subplot(2, 3, 2)
plt.title(title[1])
plt.imshow(imgs[1])
plt.xticks([])
plt.yticks([])

plt.subplot(2, 3, 3)
plt.title(title[2])
plt.imshow(imgs[2])
plt.xticks([])
plt.yticks([])

plt.subplot(2, 3, 4)
plt.title(title[3])
plt.imshow(imgs[3])
plt.xticks([])
plt.yticks([])
plt.subplot(2, 3, 5)
plt.title(title[4])
plt.imshow(imgs[4])
plt.xticks([])
plt.yticks([])


plt.show()


# Display the results of flipping an image vertically and horizontally. Also rotate the image by
# 45 degrees and 90 degrees.
# output