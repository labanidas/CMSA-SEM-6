import numpy as np
from PIL import Image

# Open the image and convert it to grayscale
image = Image.open('images/house.jpg')

# Convert the image to a NumPy array
image_array = np.array(image)

# Calculate the mean value
mean_value = np.mean(image_array)

# show mean value
print("Mean value:", mean_value)

# Create a binary image by applying the threshold
# if image_array >= mean_value TRUE value assigned to that pixel is 255
# if image_array >= mean_value FALSE value assigned to that pixel is 0
binary_image = np.where(image_array >= mean_value, 255, 0).astype(np.uint8)

# Convert the NumPy array back to an image
binary_image = Image.fromarray(binary_image)

# show the binary image
binary_image.show()





# Calculate mean value of a grayscale image. Convert the grayscale image to a binary image
# using the mean value as the threshold. Use ‘house’ image to show the results
