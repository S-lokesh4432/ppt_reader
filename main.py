import cv2
import pyautogui
import time
from hand_detector import HandDetector

cap = cv2.VideoCapture(0)
detector = HandDetector()
prev_action = None
last_action_time = 0

print("Switching to PowerPoint in 5 seconds...")
time.sleep(5)
pyautogui.hotkey('alt', 'tab')
time.sleep(1)

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    fingers = detector.fingersUp()
    current_time = time.time()

    if fingers:
        finger_count = fingers.count(1)

        if finger_count == 10 and prev_action != "next" and current_time - last_action_time > 1:
            print("✅ Open Palm → Next Slide")
            pyautogui.press("down")
            prev_action = "next"
            last_action_time = current_time

        elif finger_count == 0 and prev_action != "prev" and current_time - last_action_time > 1:
            print("✅ Fist → Previous Slide")
            pyautogui.press("up")
            prev_action = "prev"
            last_action_time = current_time

        elif finger_count not in [0, 5]:
            prev_action = None  # Reset for other gestures

    else:
        prev_action = None  # Reset if no hand detected

    cv2.imshow("Gesture Slide Control", img)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
