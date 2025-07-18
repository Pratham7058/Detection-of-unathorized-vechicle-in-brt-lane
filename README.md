
# 🚗 Detection of Unauthorized Vehicles in BRT Lanes  

## 📌 Overview  
This project aims to build a system that **detects unauthorized vehicles in Bus Rapid Transit (BRT) lanes** using **YOLOv8, Computer Vision, and Optical Character Recognition (OCR)**. The system **identifies vehicles, extracts their license plate numbers, and cross-references them with a database of permitted vehicles**. Unauthorized vehicles are automatically flagged for further action.  

### 📄 Research Paper Publication  
This project has been published in IEEE Xplore. You can read the full paper here:  
🔗 **[Detection of Unauthorized Vehicles in BRT Lanes](https://ieeexplore.ieee.org/document/10895734)**  
 

---

## ✨ Features  
✅ **Real-time License Plate Detection** using **YOLOv8**  
✅ **OCR-Based Plate Extraction** using **EasyOCR**  
✅ **Database Cross-Verification** to identify unauthorized vehicles  
✅ **Automated Flagging** of Blacklisted Vehicles  

---

## 🛠️ Technology Stack  
| Technology       | Purpose                                              |  
|-----------------|-----------------------------------------------------|  
| **YOLOv8**       | Object detection for vehicles and license plates    |  
| **EasyOCR**      | Extracting text from detected license plates        |  
| **OpenCV**       | Image processing and enhancement                   |  
| **Python**       | Backend development and automation                 |  

---

## 📂 Project Workflow  
1️⃣ **Vehicle & License Plate Detection** → **YOLOv8** detects vehicles and license plates in BRT lanes.  
2️⃣ **License Plate Text Extraction** → **EasyOCR** extracts the plate number from the license plate.  
3️⃣ **Database Cross-Checking** → The extracted plate number is matched against an **authorized vehicle database**.  
4️⃣ **Unauthorized Vehicle Flagging** → **Blacklisted vehicles** are identified and logged automatically.  

---

## 🚀 Performance Evaluation  
- ✅ **Accuracy of License Plate Detection** and Extraction.  
- ✅ **Success Rate of Identifying Blacklisted Vehicles**.  
- ✅ **Efficiency of Real-time Processing**.  

---

## 📸 Sample Output  

### 🔍 **License Plate Detection UI**  
The system captures video input and detects vehicles along with their license plates.  
**License Plate Detector UI**  
![Screenshot 2025-03-10 170919](https://github.com/user-attachments/assets/4f78a930-6372-4eec-96f1-99b5e357ff38)

### 📋 **Authorized Vehicles Database**  
A CSV file stores **authorized license plate numbers** that are permitted in the BRT lane.  
**Authorized Vehicles Database**  
![Screenshot 2025-03-10 170924](https://github.com/user-attachments/assets/51ebec93-e147-405d-aba1-f67feba56d4e)

### 🚫 **Unauthorized Vehicles Log**  
A separate CSV file stores **unauthorized vehicle Car ID and License Plate Number**.  
**Unauthorized Vehicles Log**  
![Screenshot 2025-03-10 170927](https://github.com/user-attachments/assets/33c8513b-fb2b-4052-b7f1-836a47972e1d)

---

## 🏗️ Future Enhancements  
🔹 **Integration with Live CCTV Feeds** for Real-time Tracking.  
🔹 **Deployment on Edge Devices** like Raspberry Pi for Faster Processing.  
🔹 **Development of a Dashboard** for Analytics and Reporting.  

---

## 🤝 Contributors  
- 🚀 **Pratham Mali**
---

✅ **This project was developed with the aim of improving public transportation security by identifying unauthorized vehicles in BRT lanes.**  
