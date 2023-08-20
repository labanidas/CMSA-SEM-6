# Display the results of edge detection by Prewitt operator, using ‘house’ image.

import cv2
import numpy as np
import matplotlib.pyplot as plt


def apply_prewitt_operator(image_path):
    # Load the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Apply the Prewitt operator
    gradient_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    gradient_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)

    # Combine the gradients to obtain the edge magnitude
    gradient_magnitude = np.sqrt(np.square(gradient_x) + np.square(gradient_y))

    # Normalize the gradient magnitude to the range [0, 255]
    gradient_magnitude_normalized = cv2.normalize(gradient_magnitude, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)

    # Display the original and edge-detected images
    titles = ['Original Image', 'Prewitt Edge Detection']
    images = [image, gradient_magnitude_normalized]

    plt.figure(figsize=(10, 5))
    for i in range(2):
        plt.subplot(1, 2, i + 1)
        plt.imshow(images[i], cmap='gray')
        plt.title(titles[i])
        plt.axis('off')

    plt.tight_layout()
    plt.show()


# image path
input_image_path = 'images/house.jpg'

apply_prewitt_operator(input_image_path)
