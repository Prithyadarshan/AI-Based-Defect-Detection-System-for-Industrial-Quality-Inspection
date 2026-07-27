import cv2
import numpy as np

from tensorflow.keras.models import load_model

from config import *

model = load_model(MODEL_PATH)

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()

    if not ret:
        break

    img = cv2.resize(frame, IMAGE_SIZE)

    img = img.astype("float32") / 255.0

    img = np.expand_dims(img, axis=0)

    prediction = model.predict(img, verbose=0)

    index = np.argmax(prediction)

    confidence = prediction[0][index] * 100

    label = CLASSES[index]

    color = (0,255,0)

    if label != "Normal":
        color = (0,0,255)

    text = f"{label} ({confidence:.1f}%)"

    cv2.putText(
        frame,
        text,
        (20,40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        color,
        2
    )

    cv2.imshow("Infrastructure Inspection", frame)

    key = cv2.waitKey(1)

    if key == 27:
        break

cap.release()

cv2.destroyAllWindows()