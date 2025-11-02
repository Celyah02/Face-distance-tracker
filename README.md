# 🤖 Face Direction & Speed Tracker using OpenCV

### 🧠 Project by: FURAHA NIYONGIRA Celia  
**Field:** Intelligent Systems & Robotics  
**Date:** 2025  
**Repository:** Face_Direction_Tracker_Project  

---

## 🎯 Objective

This project demonstrates how to use **OpenCV** to detect a **human face** in real time, track its **movement direction (Left, Right, Up, Down)**, and calculate the **movement speed in pixels per second**.

The system visually overlays:
- A **green bounding box** around the detected face
- **Direction text** (Left, Right, Up, Down)
- **Speed (px/s)** on the live video feed

---

## 🧩 Features

✅ Real-time face detection via OpenCV Haar Cascade  
✅ Dynamic direction tracking between consecutive frames  
✅ Speed estimation based on pixel displacement per second  
✅ Overlay visualization (text + bounding box)  
✅ Well-documented, readable, and modular code structure  

---

## 🧠 How It Works (Logic Flow)

| Step | Operation | Description |
|------|------------|--------------|
| 1️⃣ | **Frame Capture** | Webcam feed captures live video frames. |
| 2️⃣ | **Preprocessing** | Each frame converted to grayscale for faster detection. |
| 3️⃣ | **Face Detection** | Haar Cascade locates the face rectangle `(x, y, w, h)`. |
| 4️⃣ | **Center Calculation** | Center = `(x + w/2, y + h/2)` gives face midpoint. |
| 5️⃣ | **Tracking** | Compare center positions between current & previous frame. |
| 6️⃣ | **Direction Decision** | Based on displacement `(dx, dy)`: determines Left/Right/Up/Down. |
| 7️⃣ | **Speed Computation** | Uses Euclidean distance & time delta → `speed = distance / Δt`. |
| 8️⃣ | **Display Overlay** | Direction and speed are displayed on live video. |

---

## ⚙️ Technologies Used

| Tool | Purpose |
|------|----------|
| **Python 3.x** | Core programming language |
| **OpenCV (cv2)** | Image & video processing |
| **time module** | Measuring frame intervals for speed |
| **Git & GitHub** | Version control and collaboration |


### 🧩 Step 1 — Install Dependencies
Make sure you have Python 3.x and OpenCV installed:

1.pip install opencv-python
2.Step 2 — Run the Script
3.Execute the main script in your terminal:
python face_direction_tracker.py
❌ Step 4 — Exit
To close the live webcam window, press:

🧠 Working Logic (Step-by-Step):

1.Capture Frame: The webcam captures each video frame in real-time.
2.Convert to Grayscale: Makes detection faster and easier for OpenCV.
3.Face Detection: Haar Cascade identifies the bounding box of your face.
4.Calculate Center: Compute (cx, cy) — the midpoint of the face box.
5.Compare Frames: Measure how much the center moved since the last frame.
6.Compute Direction:

If cx₂ > cx₁ → Face moved Right

If cx₂ < cx₁ → Face moved Left

If cy₂ > cy₁ → Face moved Down

If cy₂ < cy₁ → Face moved Up

7.Compute Speed: Calculate pixels moved per second.

8.Overlay Results: Display direction and speed text on the live feed.

🧮 Formula for Speed
Speed
=
(
𝑑
𝑥
)
2
+
(
𝑑
𝑦
)
2
Δ
𝑡
Speed= 
Δt
(dx) 
2
 +(dy) 
2
 
Where:

dx = cx₂ - cx₁ → horizontal movement

dy = cy₂ - cy₁ → vertical movement

Δt → time difference between frames

📊 Example Output
When you move your face, the terminal and live video display:
Direction: Left
Speed: 120.54 px/s
✅ A green rectangle surrounds your face and updates continuously.

📈 Visualization Overview
Frame	Detected Face	Computed Center	Output
Frame 1	Yes	(320, 240)	—
Frame 2	Yes	(380, 240)	Direction: Right, Speed: 60 px/s
Frame 3	Yes	(380, 280)	Direction: Down, Speed: 40 px/s

🧠 What I Learned:

From this project, I developed practical understanding of:
🧩 How OpenCV detects and tracks moving objects
🧮 How to measure position change for motion detection
⏱️ How to calculate speed based on time intervals
🧠 The concept of direction vectors in computer vision

🚀 Future Improvements:
Improvement and Description
🔹 Use Mediapipe or Dlib	For more accurate face landmarks
🔹 Add 3D Head Pose Estimation	Estimate angles (pitch, yaw, roll)
🔹 Integrate with servo motors	Make a robot head follow user movement
🔹 Data Logging	Save motion data for ML training or analytics
🔹 Optimize frame rate	Use multi-threading for smoother tracking

📘 References & Learning Materials:
1.OpenCV Official Documentation
2.PyImageSearch Tutorials
3.Real-Time Object Tracking (LearnOpenCV)

# 🤖 Face Direction & Speed Tracker using OpenCV

### 👨‍🎓 By: FURAHA NIYONGIRA Celia
**Field:** Intelligent Systems & Robotics  
**Year:** 2025  

---


