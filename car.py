from ultralytics import YOLO
import subprocess
import os

# 1. Take a photo using Raspberry Pi Camera
image_name = "car.jpg"

print("Taking a photo...")
subprocess.run(["rpicam-still", "-o", image_name, "--nopreview"])

# 2. Check if the image was saved
if not os.path.exists(image_name):
    print("Error: Image was not saved.")
    exit()

print(f"Photo saved as {image_name}")

# 3. Load YOLO11 nano model
print("Loading YOLO model...")
model = YOLO("yolo11n.pt")

# 4. Run object detection
print("Running YOLO detection...")
results = model.predict(source=image_name, save=True)

print("Detection finished.")
print("Result image is saved in runs/detect/predict folder.")