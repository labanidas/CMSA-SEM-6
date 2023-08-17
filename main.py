from PIL import Image
import face_recognition
import cv2

def compatible_image(path):
    # check if square in shape
    image = Image.open(path)
    # check if single face detected in the image
    image = face_recognition.load_image_file(path)
    face_locations = face_recognition.face_locations(image)
    # Check if only a single face is detected
    if len(face_locations) != 1:
        print("No face detected")
        return False

    return True

def resize_image(path):
    image_path = path

    square_crop_around_face(path)


    image = Image.open(image_path)
    # Resize the image to 216x216 dimensions
    resized_image = image.resize((216, 216))
    resized_image.save(path)



def square_crop_around_face(path):
    # Load the image
    image = cv2.imread(path)

    # Find face locations in the image
    face_locations = face_recognition.face_locations(image)

    if len(face_locations) == 0:
        print("No face found in the image.")
        return

    # Assume the first face is the one we want to crop around
    top, right, bottom, left = face_locations[0]

    # Calculate the width and height of the face
    face_width = right - left
    face_height = bottom - top

    # Calculate the size of the square crop
    crop_size = max(face_width, face_height)

    # Calculate the center of the face
    center_x = (left + right) // 2
    center_y = (top + bottom) // 2

    # Calculate the coordinates for the square crop
    crop_left = max(center_x - crop_size // 2, 0)
    crop_top = max(center_y - crop_size // 2, 0)
    crop_right = min(center_x + crop_size // 2, image.shape[1])
    crop_bottom = min(center_y + crop_size // 2, image.shape[0])

    # Crop the image
    cropped_image = image[crop_top:crop_bottom, crop_left:crop_right]

    # Save the cropped image
    cv2.imwrite(path, cropped_image)

    print("Square crop around face complete. Cropped image saved to:", path)


