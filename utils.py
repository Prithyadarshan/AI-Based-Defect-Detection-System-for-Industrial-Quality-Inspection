import cv2

from config import *

def preprocess_image(image):

    image = cv2.resize(image, IMAGE_SIZE)

    image = image.astype("float32") / 255.0

    return image