import cv2
import numpy as np

from tensorflow.keras.models import load_model

from config import *

# =====================
# Load Model
# =====================

model = load_model(MODEL_PATH)

# =====================
# Image Path
# =====================

IMAGE_PATH = "../sample_images/sample.jpg"

# =====================
# Read Image
# =====================

image = cv2.imread(IMAGE_PATH)

if image is None:
    print("Image not found.")
    exit()

original = image.copy()

# =====================
# Preprocess
# =====================

image = cv2.resize(image, IMAGE_SIZE)

image = image.astype("float32") / 255.0

image = np.expand_dims(image, axis=0)

# =====================
# Prediction
# =====================

prediction = model.predict(image)

index = np.argmax(prediction)

confidence = prediction[0][index] * 100

label = CLASSES[index]

print("-------------------------")
print("Inspection Result")
print("-------------------------")
print("Detected :", label)
print(f"Confidence : {confidence:.2f}%")