from tensorflow.keras.preprocessing.image import ImageDataGenerator

from config import *

train_datagen = ImageDataGenerator(

    rescale=1 / 255,

    rotation_range=20,

    zoom_range=0.2,

    horizontal_flip=True,

    width_shift_range=0.2,

    height_shift_range=0.2,

    fill_mode="nearest"

)

validation_datagen = ImageDataGenerator(

    rescale=1 / 255

)

train_generator = train_datagen.flow_from_directory(

    TRAIN_DIR,

    target_size=IMAGE_SIZE,

    batch_size=BATCH_SIZE,

    class_mode="categorical"

)

validation_generator = validation_datagen.flow_from_directory(

    VALIDATION_DIR,

    target_size=IMAGE_SIZE,

    batch_size=BATCH_SIZE,

    class_mode="categorical"

)

test_generator = validation_datagen.flow_from_directory(

    TEST_DIR,

    target_size=IMAGE_SIZE,

    batch_size=BATCH_SIZE,

    class_mode="categorical",

    shuffle=False

)