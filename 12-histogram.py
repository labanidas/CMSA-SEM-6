# Display the histograms of low-contrast, medium-constrast, and high-constrast images.


import cv2
import matplotlib.pyplot as plt

def display_histogram(image_path):
    # Load the image
    image = cv2.imread(image_path, 0)

    # Calculate the histogram
    histogram = cv2.calcHist([image], [0], None, [256], [0, 256])

    # Display the histogram
    plt.figure(figsize=(8, 5))
    plt.plot(histogram, color='black')
    plt.title('Histogram')
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')
    plt.xlim([0, 256])
    plt.show()

# Example usage
low_contrast_image_path = 'images/Einstein low contrast.tif'
medium_contrast_image_path = 'images/Einstein med contrast.tif'
high_contrast_image_path = 'images/Einstein high contrast.tif'

display_histogram(low_contrast_image_path)
display_histogram(medium_contrast_image_path)
display_histogram(high_contrast_image_path)
