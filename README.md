
# Gesture-Based PPT Reader

Control your PowerPoint or Google Slides presentations using simple hand gestures detected in real-time via webcam. This project uses **Python**, **OpenCV**, **Mediapipe**, and **PyAutoGUI** to create a seamless hands-free experience.

---

## Features

- 🎥 Real-time webcam feed with gesture detection.
- ✋ Show **Open Palm** → **Next Slide**.
- ✊ Show **Fist** → **Previous Slide**.
- 🖱️ Simulates keyboard events to work with any presentation software.
- 🧠 Lightweight and works offline.

---

## Technologies Used

- Python 3.x
- OpenCV
- Mediapipe
- PyAutoGUI

---

## Installation

1. **Clone or download** the repository:

   ```bash
   git clone https://github.com/yourusername/gesture-ppt-reader.git
   cd gesture-ppt-reader
   ```

2. **Install dependencies**:

   ```bash
   pip install opencv-python mediapipe pyautogui
   ```

---

## Usage

1. Open your presentation (PowerPoint, Google Slides, etc.) in full-screen mode.
2. Run the script:

   ```bash
   python main.py
   ```

3. After a 5-second delay, the script auto-switches to your presentation.
4. Use gestures:
   - ✋ **Open Palm (all fingers up)** → **Next Slide**.
   - ✊ **Fist (no fingers up)** → **Previous Slide**.

5. Press **‘q’** to quit the application.

---


---

## File Structure

- `main.py` – Main script to run gesture detection and slide control.
- `hand_detector.py` – Custom hand detection module using Mediapipe.
- `requirements.txt` – (You can create this to list dependencies.)

---

## Notes

- Make sure your hand is clearly visible with good lighting.
- The system uses **10 fingers detected** for palm and **0 fingers** for fist.
- The program includes a **1-second cooldown** to prevent accidental double triggers.

---

