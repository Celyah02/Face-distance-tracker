import cv2
import time
import serial
# --- Connect to Arduino ---
arduino = serial.Serial(port='COM6', baudrate=9600, timeout=1)
time.sleep(2)
print("[INFO] Connected to Arduino :white_check_mark:")
# --- Setup Face Detection ---
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0)
frame_center = int(cap.get(3) // 2)
direction = "CENTER"
cooldown = 0
print("[INFO] Real-Time Face Tracker Started (Press 'q' to quit)")
while True:
    ret, frame = cap.read()
    if not ret:
        print("[ERROR] Camera not accessible.")
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)
    if len(faces) > 0:
        x, y, w, h = max(faces, key=lambda f: f[2]*f[3])
        cx = x + w // 2
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.circle(frame, (cx, y + h // 2), 4, (255, 0, 0), -1)
        offset = cx - frame_center
        threshold = 30
        # small cooldown for stable communication
        if time.time() - cooldown > 0.08:
            if offset > threshold:
                direction = "RIGHT"
                step_angle = min(6 + abs(offset)//30, 20)  # faster and smoother
                arduino.write(f"rotate {step_angle}\n".encode())
                print(f"[→] rotate {step_angle}")
                cooldown = time.time()
            elif offset < -threshold:
                direction = "LEFT"
                step_angle = -min(6 + abs(offset)//30, 20)
                arduino.write(f"rotate {step_angle}\n".encode())
                print(f"[←] rotate {step_angle}")
                cooldown = time.time()
            else:
                direction = "CENTER"
        cv2.putText(frame, direction, (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)
    else:
        cv2.putText(frame, "NO FACE DETECTED", (30, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
    cv2.imshow("Face-Controlled Stepper", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
arduino.close()
cv2.destroyAllWindows()