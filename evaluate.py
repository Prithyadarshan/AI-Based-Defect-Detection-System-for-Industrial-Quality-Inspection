from tensorflow.keras.models import load_model

from sklearn.metrics import (
    classification_report,
    confusion_matrix
)

import numpy as np

from preprocess import test_generator
from config import *

# ==========================
# Load Model
# ==========================

model = load_model(MODEL_PATH)

# ==========================
# Predict
# ==========================

predictions = model.predict(test_generator)

predicted_classes = np.argmax(predictions, axis=1)

true_classes = test_generator.classes

# ==========================
# Accuracy
# ==========================

loss, accuracy = model.evaluate(test_generator)

print("\nTest Accuracy")

print(accuracy)

# ==========================
# Classification Report
# ==========================

print("\nClassification Report\n")

print(
    classification_report(
        true_classes,
        predicted_classes,
        target_names=CLASSES
    )
)

# ==========================
# Confusion Matrix
# ==========================

print("\nConfusion Matrix\n")

print(
    confusion_matrix(
        true_classes,
        predicted_classes
    )
)