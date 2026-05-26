# IoT26-HW06

## Project Overview
This project demonstrates a **Car Detection System** using **Raspberry Pi** and **YOLO (You Only Look Once)** object detection model.  
The system detects cars in real time through the Raspberry Pi camera and displays the detection results on the monitor.

By running YOLO on Raspberry Pi, users can experience lightweight AI-based object detection in an IoT environment.

---

## Objective
- Build a real-time car detection system using Raspberry Pi
- Install and run YOLO object detection model
- Detect vehicles through Raspberry Pi camera input
- Practice AI-based computer vision on edge devices
- Learn Raspberry Pi AI and IoT integration

---

## Hardware Setup
- Raspberry Pi 5
- Raspberry Pi Camera Module
- microSD Card
- Power Supply
- HDMI Monitor
- Wi-Fi / Ethernet Connection

---

## Software Requirements
- Raspberry Pi OS
- Python 3
- Ultralytics YOLO
- OpenCV
- Picamera2

---

## Installation Process

### 1. Update Raspberry Pi

```bash
sudo apt update && sudo apt upgrade -y
```

---

### 2. Install Required Packages

```bash
sudo apt install python3-pip -y
```

Install YOLO and OpenCV:

```bash
pip install ultralytics opencv-python
```

Install Picamera2:

```bash
sudo apt install python3-picamera2 -y
```

---

### 3. Enable Raspberry Pi Camera

```bash
sudo raspi-config
```

Navigate to:

```text
Interface Options → Camera → Enable
```

Reboot Raspberry Pi.

---

### 4. Run YOLO Car Detection

Example Python code:

```python
from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    results = model(frame)

    annotated_frame = results[0].plot()

    cv2.imshow("YOLO Car Detection", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```

---

## System Workflow
The workflow performs:

1. Capture real-time video from Raspberry Pi camera
2. Process image using YOLO model
3. Detect cars in the frame
4. Display detection results on monitor

<img height="400" src="https://github.com/user-attachments/assets/372d5327-5b97-4f98-9a22-ee1839b125e8" />


---

## Detection Result Example

```text
Detected Objects:
- car
- truck
- bus
```

---

## 📸 Result
- Successfully installed YOLO on Raspberry Pi
- Connected Raspberry Pi camera successfully
- Detected cars in real time using YOLO
- Displayed object detection results on monitor

<img height="400" src="https://github.com/user-attachments/assets/6646c0df-1df1-4d70-b499-59d4ab5a56aa" />


---

## 🛠️ Reference

- https://docs.ultralytics.com/guides/raspberry-pi/
- https://www.raspberrypi.com/news/object-detection-with-ultralytics-yolo26-on-the-raspberry-pi/
- https://core-electronics.com.au/guides/raspberry-pi/getting-started-with-yolo-object-and-animal-recognition-on-the-raspberry-pi/
- https://www.youtube.com/watch?v=XKIm_R_rIeQ

---

## Repository - Notion
https://www.notion.so/Team-F-34f502a3cc6c80aa8522e0026b441b93

---

## What I Learned
- How to install and run YOLO on Raspberry Pi
- Basics of real-time object detection
- Using OpenCV with Raspberry Pi camera
- AI-based computer vision on edge devices
- Integrating AI into IoT systems
