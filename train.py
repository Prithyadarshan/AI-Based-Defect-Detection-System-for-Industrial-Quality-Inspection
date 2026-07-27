import os
import tensorflow as tf

from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import (
    ModelCheckpoint,
    EarlyStopping,
    ReduceLROnPlateau
)

from config import *
from model import build_model
from preprocess import train_generator, validation_generator

# ==========================
# Create model directory
# ==========================

os.makedirs(MODEL_DIR, exist_ok=True)

# ==========================
# Build Model
# ==========================

model = build_model()

# ==========================
# Compile Model
# ==========================

model.compile(
    optimizer=Adam(learning_rate=LEARNING_RATE),
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)

# ==========================
# Callbacks
# ==========================

checkpoint = ModelCheckpoint(
    MODEL_PATH,
    monitor="val_accuracy",
    save_best_only=True,
    verbose=1
)

early_stop = EarlyStopping(
    monitor="val_loss",
    patience=5,
    restore_best_weights=True
)

reduce_lr = ReduceLROnPlateau(
    monitor="val_loss",
    factor=0.2,
    patience=3,
    verbose=1
)

# ==========================
# Train Model
# ==========================

history = model.fit(
    train_generator,
    validation_data=validation_generator,
    epochs=EPOCHS,
    callbacks=[
        checkpoint,
        early_stop,
        reduce_lr
    ]
)

print("\nTraining Completed Successfully!")

# ==========================
# Save Final Model
# ==========================

model.save(MODEL_PATH)

print(f"Model Saved at: {MODEL_PATH}")