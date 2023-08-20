# Display the results of salt-and-pepper noise reduction by using median filter on
# ‘Circuit_board_noisy’ image.

import cv2
import numpy as np
import matplotlib.pyplot as plt

def reduce_salt_and_pepper_noise(image_path,  kernel_size):
    # Load the image
    image = cv2.imread(image_path)

    # Add salt-and-pepper noise to the image
    noisy_image = add_salt_and_pepper_noise(image)

    # Apply median filter for noise reduction
    # The Median blur operation is similar to the other averaging methods.
    # Here, the central element of the image is replaced by the median of all the pixels in the kernel area.
    denoised_image = cv2.medianBlur(noisy_image, kernel_size)

    # Display the original, noisy, and denoised images
    titles = ['Original Image', 'Noisy Image', 'Denoised Image']
    images = [image, noisy_image, denoised_image]

    plt.figure(figsize=(10, 5))
    for i in range(3):
        plt.subplot(1, 3, i + 1)
        plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))
        plt.title(titles[i])
        plt.axis('off')

    plt.tight_layout()
    plt.show()

def add_salt_and_pepper_noise(image, noise_prob=0.05):
    # Generate a mask for salt-and-pepper noise
    mask = np.random.choice([0, 1, 2], size=image.shape[:2], p=[1 - noise_prob, noise_prob / 2, noise_prob / 2])

    # Add salt-and-pepper noise to the image
    noisy_image = np.copy(image)
    noisy_image[mask == 1] = 255  # Salt noise
    noisy_image[mask == 2] = 0  # Pepper noise

    return noisy_image


# image path
input_image_path = 'images/Circuit_board_noisy.tif'
kernel_size = 5

reduce_salt_and_pepper_noise(input_image_path,  kernel_size)


