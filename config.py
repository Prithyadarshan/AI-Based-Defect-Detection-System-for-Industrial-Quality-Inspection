import os

# ==========================
# Base Directory
# ==========================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ==========================
# Dataset Paths
# ==========================

TRAIN_DIR = os.path.join(BASE_DIR, "dataset", "train")
VALIDATION_DIR = os.path.join(BASE_DIR, "dataset", "validation")
TEST_DIR = os.path.join(BASE_DIR, "dataset", "test")

# ==========================
# Model Path
# ==========================

MODEL_DIR = os.path.join(BASE_DIR, "models")

MODEL_PATH = os.path.join(
    MODEL_DIR,
    "inspection_model.keras"
)

# ==========================
# Reports
# ==========================

REPORT_DIR = os.path.join(BASE_DIR, "reports")

REPORT_FILE = os.path.join(
    REPORT_DIR,
    "inspection_report.csv"
)

# ==========================
# Image Parameters
# ==========================

IMAGE_SIZE = (224, 224)

IMAGE_HEIGHT = 224

IMAGE_WIDTH = 224

CHANNELS = 3

# ==========================
# Training Parameters
# ==========================

BATCH_SIZE = 32

EPOCHS = 20

LEARNING_RATE = 0.001

# ==========================
# Infrastructure Classes
# ==========================

CLASSES = [
    "Crack",
    "Corrosion",
    "Pothole",
    "Spalling",
    "Normal"
]

NUM_CLASSES = len(CLASSES)