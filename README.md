# HUMANEX – Verifying Life Beyond Pixels

HUMANEX is a real-time human verification system designed to determine whether an interacting entity is a **real human or a synthetic AI system**.

Unlike traditional identity verification systems, HUMANEX focuses on **liveness and behavioral verification**, ensuring that the entity interacting with a system exhibits natural human behavior.

---

## Problem Statement

With the rise of:
- Deepfake videos
- AI-generated avatars
- Voice cloning
- Automated bots

it has become increasingly difficult to distinguish between real humans and synthetic entities.

Traditional methods like CAPTCHA, OTP, or static facial recognition fail to guarantee **true human presence**.

---

## Solution

HUMANEX uses **multi-frame behavioral analysis** to verify human presence in real-time.

Instead of relying on static inputs, the system analyzes:

- Eye blink patterns
- Head movement
- Temporal behavior across frames

This makes it significantly harder for synthetic systems to spoof.

---

## Key Features

- Real-time webcam-based verification
- Multi-frame analysis (not single image)
- Blink detection (biological signal)
- Head movement detection (behavioral signal)
- Dynamic challenge-based verification
- Human probability scoring system

---

## How It Works

1. User opens the system
2. A random challenge is generated:
   - Blink your eyes
   - Move your head
3. Multiple frames are captured
4. Backend processes:
   - Blink detection
   - Head movement detection
5. System evaluates response
6. Outputs:
   - Human Verified 
   - Suspicious 

---

## Core Idea

HUMANEX is based on the principle that:

> “Human behavior is naturally inconsistent and difficult to replicate artificially.”

By analyzing **temporal behavioral signals**, the system moves beyond traditional static verification methods.

---

## System Architecture
```
User (Webcam Input)
        │
        ▼
Frontend (React + WebRTC)
        │
        ▼
Frame Capture (Multi-frame)
        │
        ▼
API Call (FastAPI Backend)
        │
        ▼
Processing Layer
   ├── Biological Signals (Blink)
   ├── Behavioral Signals (Head Movement)
        │
        ▼
Decision Engine
        │
        ▼
Human Score + Status
        │
        ▼
Frontend Display (Verified / Suspicious)
```

---

---

## Tech Stack

### Frontend
- React.js
- JavaScript
- WebRTC

### Backend
- FastAPI
- Python

### Computer Vision
- OpenCV
- MediaPipe

---

## Project Status

Functional prototype:

- Real-time verification working  
- Frontend ↔ Backend integration complete  
- Challenge-based system implemented  

---

## Future Work

- Audio-based verification (speech + breathing patterns)
- Behavioral entropy analysis
- Reaction time measurement
- Machine learning-based classifier
- Cloud deployment (Docker + Kubernetes)

---

## Use Cases

- FinTech authentication
- Online exam proctoring
- Bot detection systems
- Secure digital interactions

---

## Key Insight

> HUMANEX shifts verification from *“Who are you?”*  
> to *“Are you truly human?”*