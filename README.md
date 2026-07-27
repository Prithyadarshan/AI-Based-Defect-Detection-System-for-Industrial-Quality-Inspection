# AI-Based Infrastructure Defect Detection System

## Overview

AI-Based Infrastructure Defect Detection System is a deep learning-based computer vision application developed using Python, TensorFlow, and OpenCV to automate the inspection of infrastructure surfaces. The system identifies structural defects such as cracks in concrete surfaces by analyzing images and classifying them as **Crack (Defective)** or **Normal (Non-Defective)**.

The project aims to reduce manual inspection efforts, improve inspection accuracy, and provide a cost-effective solution for monitoring the condition of roads, bridges, buildings, tunnels, and other civil infrastructure. It also supports real-time inspection through webcam-based detection.



## Features

- AI-powered infrastructure defect detection
- Automatic classification of Crack and Normal surfaces
- Deep Learning CNN-based image classification
- Image preprocessing and augmentation
- Real-time webcam inspection
- Prediction confidence score
- Model evaluation with accuracy metrics
- Automatic trained model saving
- Easy-to-use project structure
- Modular Python implementation



## Technologies Used

- Python
- TensorFlow
- Keras
- OpenCV
- NumPy
- Pandas
- Matplotlib
- Pillow
- Scikit-learn



# Project Structure

```text
AI_Infrastructure_Inspection/
│
├── dataset/
│   ├── train/
│   │   ├── Crack/
│   │   └── Normal/
│   │
│   ├── validation/
│   │   ├── Crack/
│   │   └── Normal/
│   │
│   └── test/
│       ├── Crack/
│       └── Normal/
│
├── models/
│
├── reports/
│
├── sample_images/
│   ├── crack1.jpg
│   ├── crack2.jpg
│   ├── crack3.jpg
│   ├── normal1.jpg
│   └── normal2.jpg
│
├── src/
│   ├── config.py
│   ├── model.py
│   ├── preprocess.py
│   ├── train.py
│   ├── predict.py
│   ├── evaluate.py
│   ├── webcam.py
│   ├── report.py
│   └── utils.py
│
├── requirements.txt
└── README.md
```



# Project Modules

## Dataset

Contains the training, validation, and testing datasets organized into Crack and Normal classes. Images are automatically loaded during model training using TensorFlow's ImageDataGenerator.



## Model

Implements a Convolutional Neural Network (CNN) for defect classification. The network learns image features from concrete surface images and predicts whether an input image contains a structural crack.



## Image Preprocessing

Performs preprocessing operations including:

- Image resizing
- Pixel normalization
- Data augmentation
- Batch generation
- Image loading

These preprocessing techniques improve the robustness and accuracy of the trained model.



## Model Training

The training module:

- Loads the dataset
- Builds the CNN architecture
- Trains the model
- Validates performance
- Saves the best trained model automatically

The trained model is stored in the **models** directory.



## Prediction

Allows users to classify a single infrastructure image.

The system:

- Reads the input image
- Preprocesses it
- Loads the trained model
- Predicts the defect class
- Displays the prediction with confidence score



## Model Evaluation

Evaluates the trained model using the test dataset and reports:

- Test Accuracy
- Test Loss
- Classification Performance



## Webcam Inspection

Supports real-time infrastructure inspection using a webcam.

The captured frames are continuously analyzed and classified as:

- Crack
- Normal

The prediction result is displayed directly on the webcam feed.



## Report Generation

Stores prediction results for future analysis.

Each report contains:

- Image Name
- Prediction
- Confidence Score
- Timestamp

Reports are generated in CSV format inside the **reports** directory.



## Sample Images

Contains sample infrastructure images used for testing the prediction module.

Example images include:

- crack1.jpg
- crack2.jpg
- crack3.jpg
- normal1.jpg
- normal2.jpg



# Dataset Information

The project uses the **Concrete Crack Images Dataset**, a publicly available dataset consisting of concrete surface images categorized into:

- Crack (Positive)
- Normal (Negative)

The dataset is divided into:

- Training Dataset
- Validation Dataset
- Testing Dataset



# How to Run the Project

## Step 1

Download or clone the repository.



## Step 2

Open the project folder.



## Step 3

Install the required dependencies.

```bash
pip install -r requirements.txt
```



## Step 4

Train the model.

```bash
python src/train.py
```

The trained model will be saved inside:

```
models/
```



## Step 5

Evaluate the trained model.

```bash
python src/evaluate.py
```



## Step 6

Predict a single image.

```bash
python src/predict.py
```



## Step 7

Run real-time webcam inspection.

```bash
python src/webcam.py
```



# Expected Output

The system classifies an input image as:

```
Prediction : Crack

Confidence : 98.42%
```

or

```
Prediction : Normal

Confidence : 97.81%
```

During webcam inspection, the detected class is displayed live on the video feed.



# Applications

- Road Surface Inspection
- Bridge Crack Detection
- Building Structural Inspection
- Tunnel Infrastructure Monitoring
- Smart City Infrastructure Maintenance
- Industrial Concrete Inspection
- Construction Site Quality Assessment
- Preventive Infrastructure Maintenance



# Future Enhancements

- Multi-class defect detection (Crack, Corrosion, Pothole, Spalling)
- Object Detection using YOLOv8
- Mobile application integration
- Drone-based infrastructure inspection
- Cloud deployment
- Real-time dashboard with analytics
- Automated maintenance report generation
- IoT sensor integration for smart infrastructure monitoring



# Purpose of the Project

The objective of this project is to automate infrastructure inspection using Artificial Intelligence and Computer Vision techniques. By replacing manual visual inspection with deep learning-based image analysis, the system helps improve inspection speed, accuracy, and consistency while supporting early detection of structural defects to enhance public safety and reduce maintenance costs.



# Author

**PRITHYADARSHAN T**

Computer Science and Engineering (Artificial Intelligence & Machine Learning)

**GitHub:** https://github.com/prithyadarshan

**LinkedIn:** https://www.linkedin.com/in/prithyadarshan-thiyagarajan-379a4b2a3
