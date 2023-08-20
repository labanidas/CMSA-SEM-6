# Display the smoothing effects of 3×3 and 5×5 mean filters using ‘man’ image

import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def apply_mean_filter(image_path, kernel_size, title):
    # Open the image using Pillow
    image = Image.open(image_path)

    # Convert the image to a NumPy array
    image_array = np.array(image)

    # Apply the mean filter
    filtered_image_array = cv2.blur(image_array, (kernel_size, kernel_size))

    # convert image array to image
    filtered_image = Image.fromarray(filtered_image_array)

    # Display the image with the specified title
    plt.imshow(filtered_image, cmap='gray')
    plt.title(title)
    plt.axis('off')
    plt.show()



# man image path
input_image_path = 'images/man.gif'
kernel_size_3x3 = 3
kernel_size_5x5 = 5

apply_mean_filter(input_image_path, kernel_size_3x3, "smoothning using 3x3 mean filter")
apply_mean_filter(input_image_path, kernel_size_5x5,"smoothning using 5x5 mean filter ")
