### Basic
# import cv2
# import numpy as np 
# import time 
# import os 
# import mediapipe as mp 


# cam = cv2.VideoCapture(0)

# mpHands = mp.solutions.hands 

# hands =  mpHands.Hands()

# HandDraw = mp.solutions.drawing_utils

# pTime = 0 
# cTime = 0 

# while True :
#     success , img = cam.read()
#     img = cv2.flip(img, 1)

#     imgRGB = cv2.cvtColor(img , cv2.COLOR_BGR2RGB)

#     result = hands.process(imgRGB)


#     if result.multi_hand_landmarks : 
#         for handlandm in result.multi_hand_landmarks:
#             for  id , lm in enumerate(handlandm.landmark):
#                 # print(id , lm )
#                 height , weight , channel = img.shape 
#                 # To Find The Position
#                 cx , cy = int(lm.x*weight) , int(lm.y*height)
#                 print(id,cx,cy)

#                 # if id == 0 : 
#                 #     cv2.circle(img , (cx , cy) , 5 , (255 , 0 , 255) , cv2.FILLED)



#             HandDraw.draw_landmarks(img, handlandm , mpHands.HAND_CONNECTIONS)



#     cTime = time.time()
#     fps = 1/(cTime - pTime)
#     pTime = cTime 

#     cv2.putText(img,str(int(fps)) , (10,70) , cv2.FONT_HERSHEY_PLAIN,
#                 3,(255,0,255),3)

#     cv2.imshow("Camera" , img)

#     if cv2.waitKey(1) == ord("q"):
#         break

# cam.release()
# cv2.destroyAllWindows()
