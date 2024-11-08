import cv2
import mediapipe as mp
import pyautogui
c = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_w, screen_h = pyautogui.size()
while True:
    _, frame = c.read()
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    o= face_mesh.process(rgb_frame)
    landmark = o.multi_face_landmarks
    frame_h, frame_w, _ = frame.shape
    if landmark:
        landmarks = landmark[0].landmark
        for id, landmark in enumerate(landmarks[474:478]):
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 0))
            if id == 1:
                screen_x = screen_w * landmark.x
                screen_y = screen_h * landmark.y
                pyautogui.moveTo(screen_x, screen_y)
        left = [landmarks[145], landmarks[159]]#145 is upper eyelesses and 159 is lower eyelesses
        for landmark in left:
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 255))
    if (left[0].y - left[1].y) < 0.004:
        pyautogui.click()
        pyautogui.sleep(1)
    cv2.imshow('Hawkeye', frame)
    cv2.waitKey(1)