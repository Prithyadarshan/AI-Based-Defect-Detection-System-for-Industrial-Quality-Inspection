import tensorflow as tf

from tensorflow.keras.models import Sequential

from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.layers import BatchNormalization
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Dropout

from config import *


def build_model():

    model = Sequential()

    model.add(
        Conv2D(
            32,
            (3, 3),
            activation="relu",
            input_shape=(IMAGE_HEIGHT, IMAGE_WIDTH, CHANNELS)
        )
    )

    model.add(BatchNormalization())

    model.add(MaxPooling2D())

    model.add(
        Conv2D(
            64,
            (3, 3),
            activation="relu"
        )
    )

    model.add(BatchNormalization())

    model.add(MaxPooling2D())

    model.add(
        Conv2D(
            128,
            (3, 3),
            activation="relu"
        )
    )

    model.add(BatchNormalization())

    model.add(MaxPooling2D())

    model.add(Flatten())

    model.add(Dense(256, activation="relu"))

    model.add(Dropout(0.5))

    model.add(Dense(NUM_CLASSES, activation="softmax"))

    return model