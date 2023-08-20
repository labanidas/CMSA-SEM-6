# Display the results of morphological operation ‘dilation’ and ‘erosion’ using ‘house’ image

import cv2
import numpy as np
import matplotlib.pyplot as plt

def apply_morphological_operations(image_path):
    # Load the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Define the structuring element for morphology
    kernel = np.ones((3, 3), np.uint8)

    # Apply dilation and erosion operations
    dilated_image = cv2.dilate(image, kernel, iterations=1)
    eroded_image = cv2.erode(image, kernel, iterations=1)

    # Display the original, dilated, and eroded images
    titles = ['Original Image', 'Dilated Image', 'Eroded Image']
    images = [image, dilated_image, eroded_image]

    plt.figure(figsize=(10, 5))
    for i in range(3):
        plt.subplot(1, 3, i+1)
        plt.imshow(images[i], cmap='gray')
        plt.title(titles[i])
        plt.axis('off')

    plt.tight_layout()
    plt.show()

# Example usage
input_image_path = 'images/house.jpg'

apply_morphological_operations(input_image_path)
