# IoT26-HW06

## Project Overview
This project demonstrates a **Car Plate Recognition System** using **Raspberry Pi** and **Node-RED**.  
By using the OpenALPR (Automatic License Plate Recognition) API, the system can detect and recognize vehicle license plates from images captured by the Raspberry Pi camera.

---

## Objective
- Build a car plate recognition system using Raspberry Pi and Node-RED
- Use OpenALPR API for automatic license plate recognition
- Practice image processing and IoT workflow integration
- Learn Node-RED dashboard and API communication

---

## Hardware Setup
- Raspberry Pi 5
- Raspberry Pi Camera Module
- microSD Card
- Power Supply
- Wi-Fi / Ethernet Connection

---

## Software Requirements
- Raspberry Pi OS
- Node-RED
- OpenALPR API
- Web Browser for Dashboard Access

---

## Installation Process

### 1. Install Node-RED
Update Raspberry Pi and install Node-RED.

```bash
bash <(curl -sL https://raw.githubusercontent.com/node-red/linux-installers/master/deb/update-nodejs-and-nodered)
```

Enable Node-RED service:

```bash
sudo systemctl enable nodered.service
```

Start Node-RED:

```bash
node-red-start
```

---

### 2. Access Node-RED Dashboard
Open browser and access:

```bash
http://<RaspberryPi_IP_Address>:1880
```

---

### 3. Configure OpenALPR API
- Create OpenALPR account
- Get API Secret Key
- Configure API request in Node-RED flow

---

### 4. Connect Raspberry Pi Camera
Enable camera interface:

```bash
sudo raspi-config
```

Navigate to:

```text
Interface Options → Camera → Enable
```

Reboot Raspberry Pi.

---

## Node-RED Workflow
The workflow performs:
1. Capture image from Raspberry Pi camera
2. Send image to OpenALPR API
3. Receive plate recognition result
4. Display detected plate number on dashboard


<img height="400" src="https://github.com/user-attachments/assets/372d5327-5b97-4f98-9a22-ee1839b125e8" />



---

## Example API Request

```javascript
msg.headers = {
    "content-type": "application/json"
};

msg.payload = {
    secret_key: "YOUR_OPENALPR_SECRET_KEY",
    image_url: "IMAGE_URL"
};

return msg;
```

---

## 🧪 Recognition Result Example

```json
{
  "results": [
    {
      "plate": "12ABC345",
      "confidence": 89.5
    }
  ]
}
```

---

## 📸 Result
- Successfully connected Raspberry Pi with Node-RED
- Sent vehicle image to OpenALPR API
- Detected and displayed car plate number

<img height="400" src="https://github.com/user-attachments/assets/173b2573-ed50-47b7-b082-50ac444cd9fe" />




---

## 🛠️ Reference
Tutorial followed:

- https://randomnerdtutorials.com/car-plate-recognition-system-with-raspberry-pi-and-node-red/

---

## 📂 Repository- Notion
https://www.notion.so/Team-F-34f502a3cc6c80aa8522e0026b441b93

---

## 💡 What I Learned
- How to use Node-RED with Raspberry Pi
- Basics of API communication
- Image-based license plate recognition
- IoT automation using Node-RED workflows
- Integrating external AI services into Raspberry Pi projects
