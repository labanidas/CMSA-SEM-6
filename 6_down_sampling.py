
from PIL import Image

def downsample_image(image_path, output_path, factor):
    # Open the image
    image = Image.open(image_path)

    # Calculate the new width and height based on the downsampling factor
    width = image.width // factor
    height = image.height // factor

    # Downsample the image using the 'ANTIALIAS' filter for better quality
    downscaled_image = image.resize((width, height), Image.ANTIALIAS)

    downscaled_image.show()

def show_downsampled_image(file_name):
    input_image_path = f"Images/{file_name}"
    output_image_path = f"6/{file_name.split('.')[0]}_downsampled.jpg"
    downsampling_factor = 2

    #  downsample and save image
    downsample_image(input_image_path, output_image_path, downsampling_factor)

# face image
show_downsampled_image("face.jpg")
# rose image
show_downsampled_image("rose-512.bmp")








# Display the results of down-sampling using ‘face’ and ‘rose’ image.