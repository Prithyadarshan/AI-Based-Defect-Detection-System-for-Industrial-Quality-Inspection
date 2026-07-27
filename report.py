import csv
import os
from datetime import datetime

from config import *

os.makedirs(REPORT_DIR, exist_ok=True)

def save_report(image_name, defect, confidence):

    file_exists = os.path.exists(REPORT_FILE)

    with open(REPORT_FILE, "a", newline="") as file:

        writer = csv.writer(file)

        if not file_exists:

            writer.writerow(
                [
                    "Image",
                    "Defect",
                    "Confidence",
                    "Timestamp"
                ]
            )

        writer.writerow(
            [
                image_name,
                defect,
                f"{confidence:.2f}",
                datetime.now()
            ]
        )

    print("Inspection report updated.")