import cv2
import mediapipe as mp
import numpy as np
import pickle

cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
Hands = mpHands.Hands()
draw = mp.solutions.drawing_utils
# Media File uses RGB Format 

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

size = (frame_width, frame_height)

# Below VideoWriter object will create
# a frame of above defined The output
# is stored in 'filename.avi' file.
# Comment out if you want to the video.
# result = cv2.VideoWriter('demo.avi',cv2.VideoWriter_fourcc(*'MJPG'),10, size)

while True:
    success, img = cap.read()
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = Hands.process(rgb)

    if results.multi_hand_landmarks:
        with open('./model/model_pkl', 'rb') as f:
            lr = pickle.load(f)
        for id, hands in enumerate(results.multi_hand_landmarks):
            draw.draw_landmarks(img, hands, mpHands.HAND_CONNECTIONS)

            x_cor = []
            y_cor = []
            z_cor = []


            def coord(x_cor, y_cor, z_cor, hands):
                for i in range(0, 21):
                    x_cor.append(hands.landmark[i].x)
                    y_cor.append(hands.landmark[i].y)
                    z_cor.append(hands.landmark[i].z)
                return x_cor, y_cor, z_cor


            x_cor, y_cor, z_cor = coord(x_cor, y_cor, z_cor, hands)
            total_cor = x_cor + y_cor + z_cor

            digit = lr.predict([total_cor])

            digit = str(digit)
            print(digit)
            cv2.putText(img, str(digit), (255, 255), cv2.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0), thickness=2)

    # result.write(img)
    cv2.imshow("img", img)

    if cv2.waitKey(1) == ord('q'):
        break
