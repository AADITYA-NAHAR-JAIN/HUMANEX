from feature_extraction.head_pose import get_head_movement
from feature_extraction.blink_detection import detect_blink

from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from pydantic import BaseModel

import base64
import cv2
import numpy as np

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class FrameData(BaseModel):
    frames: list[str]
    challenge: str

@app.get("/")
def root():
    return {
        "status": "HUMANEX backend running",
        "message": "Use POST /verify"
    }

@app.post("/verify")
def verify(frame: FrameData):

    if frame.challenge not in ["blink", "move"]:
        return {
            "human_score": 40,
            "blink_score": None,
            "movement_count": None,
            "status": "Invalid challenge"
        }

    if not frame.frames:
        return {
            "human_score": 0,
            "blink_count": 0,
            "movement_count": 0,
            "status": "No input provided"
        }

    blink_count = 0
    movement_count = 0
    prev_face = None
    prev_center = None
    challenge = frame.challenge

    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    for img_str in frame.frames:
        try:
            if "," not in img_str:
                continue

            image_data = img_str.split(",")[1]
            img_bytes = base64.b64decode(image_data)

            np_arr = np.frombuffer(img_bytes, np.uint8)
            img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

            if img is None:
                continue

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            faces = face_cascade.detectMultiScale(gray, 1.3, 5)

            if len(faces) > 0:
                (x, y, w, h) = faces[0]
                current_face = (x, y)

                if prev_face is not None:
                    dx = abs(current_face[0] - prev_face[0])
                    dy = abs(current_face[1] - prev_face[1])

                    if dx > 10 or dy > 10:
                        movement_count += 1  

                prev_face = current_face

            blink = detect_blink(img)
            blink_count += blink
            prev_center, movement = get_head_movement(img, prev_center)
            movement_count += movement

        except Exception as e:
            print("Error processing frame:", e)
            continue

    print("FINAL -> Blink:", blink_count, "Movement:", movement_count)

    if challenge == "blink":
        if blink_count >= 1:
            score = 95
            status = "Human Verified"
        else:
            score = 40
            status = "Blink not detected"

    elif challenge == "move":
        if movement_count >= 1:
            score = 95
            status = "Human Verified"
        else:
            score = 40
            status = "No movement detected"

    else:
        score = 40
        status = "Invalid challenge"

    return {
        "human_score": score,
        "blink_count": blink_count if challenge == "blink" else None,
        "movement_count": movement_count if challenge == "move" else None,
        "status": status
    }