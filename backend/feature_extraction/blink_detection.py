import cv2
import numpy as np
import mediapipe as mp

if not hasattr(mp, "solutions"):
    raise Exception("Mediapipe not loaded properly")

mp_face_mesh = mp.solutions.face_mesh

# Eye landmark indices
LEFT_EYE = [33, 160, 158, 133, 153, 144]
RIGHT_EYE = [362, 385, 387, 263, 373, 380]

def eye_aspect_ratio(landmarks, eye_indices, w, h):
    pts = [(int(landmarks[i].x * w), int(landmarks[i].y * h)) for i in eye_indices]

    # vertical distances
    v1 = np.linalg.norm(np.array(pts[1]) - np.array(pts[5]))
    v2 = np.linalg.norm(np.array(pts[2]) - np.array(pts[4]))

    # horizontal distance
    h_dist = np.linalg.norm(np.array(pts[0]) - np.array(pts[3]))

    ear = (v1 + v2) / (2.0 * h_dist)
    return ear


def detect_blink(image):
    h, w, _ = image.shape

    with mp_face_mesh.FaceMesh(static_image_mode=True) as face_mesh:
        results = face_mesh.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

        if not results.multi_face_landmarks:
            return 0  # no face detected

        landmarks = results.multi_face_landmarks[0].landmark

        left_ear = eye_aspect_ratio(landmarks, LEFT_EYE, w, h)
        right_ear = eye_aspect_ratio(landmarks, RIGHT_EYE, w, h)

        avg_ear = (left_ear + right_ear) / 2.0

        # threshold
        if avg_ear < 0.21:
            return 1  # blink detected
        else:
            return 0