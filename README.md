# 🔐 Facial Recognition Attendance System

## 🚀 Project Overview
The **Facial Recognition Attendance System** is a cutting-edge solution designed to automate student attendance tracking in educational institutions. It leverages facial recognition technology to replace traditional roll-call methods, ensuring efficiency, security, and accuracy in monitoring attendance.

## 🏆 Why This Project?
- 📈 **Growing Popularity of Online Learning**: With a 32% increase in Coursera registrations by 2021, online courses require better attendance solutions.
- 🎯 **Challenges in Attendance Monitoring**: Instructors struggle with tracking student participation accurately.
- 🔒 **Need for Secure Authentication**: Preventing fraudulent attendance is crucial in online education.

## ✨ Key Features
### ✅ **Facial Recognition-Based Attendance**
- 📷 Captures live video/images of students.
- 🔍 Matches them against a registered database.
- 📌 Marks attendance in real time.

### 🗂 **Efficient Record Management**
- 📝 Stores attendance data securely in an **Excel (CSV) database**.
- 📊 Provides an easy-to-navigate interface for students and professors.

### 🎭 **User-Friendly Interface**
- Simple registration with face capture.
- Automatic attendance logging and real-time updates.

## 📜 Workflow
### 🔹 **1. Registration**
- Users enter their **ID & Name**.
- The system captures **up to 50 images** per student for training (stored in the `TrainingImage` folder).

### 🔹 **2. Model Training**
- Users click "Train Image" to convert facial images into a numerical model.
- This enables the system to recognize faces accurately.

### 🔹 **3. Automatic Attendance**
- Users enter the **subject name** and click "Automatic Attendance".
- The system identifies faces and records attendance in a **CSV file**.

### 🔹 **4. Attendance Viewing**
- Clicking "View Attendance" displays attendance records in a tabular format.

## 🛠 Tools & Technologies
### 🐍 **Python Libraries Used**
- **Pandas** 🟡 - For data manipulation and storage.
- **NumPy** 🔵 - For numerical computations.
- **OpenCV (cv2)** 📷 - For image and video processing.
- **Tkinter** 🖥️ - For creating the graphical user interface.
- **Pillow (PIL)** 🖼️ - For image processing and enhancement.
- **OS Module** 📂 - For file and directory management.

## 🔧 Setup & Installation
### 📌 Prerequisites
- **Python 3.7+**
- Required libraries (`pip install pandas numpy opencv-python tkinter pillow`)

### 📥 Installation Steps
1. Clone the repository:
   ```sh
   git clone https://github.com/becherzribi/Facial-Recognition-Attendance.git
   ```
2. Navigate to the project folder:
   ```sh
   cd Facial-Recognition-Attendance
   ```
3. Run the system:
   ```sh
   python main.py
   ```

## 📩 Contact
📌 **Becher Zribi**
- ✉️ Email: [zribibecher.tn@gmail.com](mailto:zribibecher.tn@gmail.com)
- 🔗 LinkedIn: [Becher Zribi](https://www.linkedin.com/in/becher-zribi/)
- 🖥 GitHub Repository: [Facial Recognition Attendance](https://github.com/becherzribi/Attendance-Management-system-using-face-recognition)

---
**🎯 Facial Recognition Attendance System - 2025**
