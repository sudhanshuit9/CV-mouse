import cv2
import mediapipe as mp
import pyautogui

cap = cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()
index_y = 2
while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape
    rbg_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rbg_frame)
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame,hand)
            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x*frame_width)
                y = int(landmark.y*frame_height)

                #print(id)
                if id == 8:

                    #print("Inside IF ")

                    cv2.circle(img=frame,  center=(x,y),  radius=10,  color=(0,255,255))
                    index_x = screen_width/frame_width*x
                    index_y = screen_height/frame_height*y
                    pyautogui.moveTo(index_x, index_y)

                    #Reconize thumb movements

                    thumb_x = screen_width / frame_width * x
                    thumb_y = screen_height / frame_height * y

                    print("Thumb_X",thumb_x)

                    print("Thumb_Y", thumb_y)

                    print('outside', abs(index_y - thumb_y))

                    if abs(index_y - thumb_y) < 20:
                        print("Inside IF Index Y ")
                        pyautogui.click()
                        print("Click")

                        pyautogui.size()

                    """
                    if id == 4:
                        print(" IF ID 4 ")
                        cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                        thumb_x = screen_width/frame_width*x
                        thumb_y = screen_height/frame_height*y
                        print('outside', abs(index_y - thumb_y))
                        if abs(index_y - thumb_y) < 20:
                            print("Inside IF Index Y ")
                            #pyautogui.click()
                            #pyautogui.size(1)
                    """
    cv2.imshow('Virtual Mouse', frame)
    cv2.waitKey(1)

