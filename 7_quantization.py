# import cv2
from PIL import Image

def quantize_image(image_path, output_path, num_colors):
    # Open the image
    image = Image.open(image_path)

    # Apply quantization by reducing the number of colors
    quantized_image = image.quantize(num_colors)

    #show image
    quantized_image.show()


def showQuantizedimage(file_name):
    input_image_path = f"images/{file_name}"
    output_image_path = f"7/{file_name.split('.')[0]}_quantized.jpg"
    num_colors = 20

    quantize_image(input_image_path, output_image_path, num_colors)

# face image
showQuantizedimage("face.jpg")
# rose image
showQuantizedimage("rose-512.bmp")



# Display the effects of quantization using ‘face’ and ‘rose’ image.