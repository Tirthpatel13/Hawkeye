import cv2
import mediapipe as m
c = cv2.VideoCapture(0)
while True:
    _, frame = c.read()
    frame = cv2.flip(frame, 1)
    cv2.imshow('Hawkeye', frame)
    cv2.waitKey(1)
