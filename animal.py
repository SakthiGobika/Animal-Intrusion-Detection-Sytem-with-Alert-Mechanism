import os
import cv2
import torch
import threading
import pygame
from ultralytics import YOLO
import pyttsx3
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

# ----------- Configurations -----------
MODEL_PATH = "yolov8x.pt"  # Make sure this file is present
TARGET_CLASS = "bear"  # Change to "teddy bear" if needed
AUDIO_PATH = r"C:\Users\sakth\Downloads\sound.mp3"  # Update if necessary

EMAIL_SENDER = "sakthigobika4780@gmail.com"
EMAIL_PASSWORD = "lzcz gvyb rahy ldpz"
EMAIL_RECEIVER = "msprabu12345@gmail.com"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

# ----------- Initialize -----------
model = YOLO(MODEL_PATH)

pygame.mixer.init()
pygame.mixer.music.load(AUDIO_PATH)

email_sent = False  # Track if email has been sent


# ----------- Functions -----------
def speak_text(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1)
    engine.say(text)
    engine.runAndWait()


def play_audio():
    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.play()
        tts_thread = threading.Thread(target=speak_text, args=(TARGET_CLASS,))
        tts_thread.start()


def send_email():
    subject = "🚨 ALERT: Bear Detected!"
    body = "The YOLOv8 model has detected a bear in the camera feed."

    msg = MIMEMultipart()
    msg["From"] = EMAIL_SENDER
    msg["To"] = EMAIL_RECEIVER
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        context = ssl.create_default_context()
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls(context=context)
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())
        print("✅ Email sent successfully!")
    except Exception as e:
        print("❌ Failed to send email:", e)


# ----------- Main Loop -----------
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    results = model.predict(frame, device="cuda" if torch.cuda.is_available() else "cpu", conf=0.5)
    detected = False

    for result in results:
        boxes = result.boxes
        for box in boxes:
            cls = int(box.cls[0])
            label = model.names[cls]
            conf = float(box.conf[0])
            x1, y1, x2, y2 = map(int, box.xyxy[0])

            # Draw bounding box and label
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            label_text = f"{label} ({conf:.2f})"
            cv2.putText(frame, label_text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX,
                        0.6, (0, 255, 0), 2)

            # Check for target object
            if label.lower() == TARGET_CLASS.lower():
                detected = True
                print(f"🧸 Detected: {label} with confidence {conf:.2f}")

    # If detected, play sound and send email once
    if detected:
        if not pygame.mixer.music.get_busy():
            threading.Thread(target=play_audio, daemon=True).start()

        if not email_sent:
            threading.Thread(target=send_email, daemon=True).start()
            email_sent = True
    else:
        email_sent = False

    # Show frame
    cv2.imshow("YOLOv8 Object Detection", frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("❎ Exiting...")
        break

cap.release()
cv2.destroyAllWindows()