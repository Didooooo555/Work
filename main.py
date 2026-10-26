print("start")

try:
    import cv2
    print("cv2 ok", cv2.__version__)
except Exception as e:
    print("cv2 FAIL:", e)

try:
    import mediapipe as mp
    print("mediapipe ok", mp.__version__)
except Exception as e:
    print("mediapipe FAIL:", e)

print("done")
input("Press Enter...")

