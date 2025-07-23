# import cv2
# import numpy as np 
# import time 
# import os 
# import mediapipe as mp 


# class HandDetector():
#     def __init__(self , mode = False ,maxhands =2 , detectionconf= 0.5 , trackingconf = 0.5 ):
#         self.mode = mode
#         self.maxhands = maxhands
#         self.detectionconf = detectionconf
#         self.trackingconf = trackingconf
        
#         self.mpHands = mp.solutions.hands 
#         self.hands =  self.mpHands.Hands(self.mode,self.maxhands,
#             self.detectionconf,self.trackingconf )
#         self.HandDraw = mp.solutions.drawing_utils

        

#     def find_Hands(self , img , flag_draw=True):
            
#         imgRGB = cv2.cvtColor(img , cv2.COLOR_BGR2RGB)

#         result = self.hands.process(imgRGB)


#         if result.multi_hand_landmarks : 
#             for handlandm in result.multi_hand_landmarks:
#                 if flag_draw:
#                     self.HandDraw.draw_landmarks(img, handlandm , self.mpHands.HAND_CONNECTIONS)

#         return img
    


# #  for  id , lm in enumerate(handlandm.landmark):
# #                     # print(id , lm )
# #                     height , weight , channel = img.shape 
# #                     # To Find The Position
# #                     cx , cy = int(lm.x*weight) , int(lm.y*height)
# #                     print(id,cx,cy)

# #                     # if id == 0 : 
# #                     #     cv2.circle(img , (cx , cy) , 5 , (255 , 0 , 255) , cv2.FILLED)




# def main():
    
#     pTime = 0 
#     cTime = 0 
#     cam = cv2.VideoCapture(0)
#     detector = HandDetector()

#     while True :
#         success , img = cam.read()
#         img = detector.find_Hands(img)
#         img = cv2.flip(img, 1)


#         cTime = time.time()
#         fps = 1/(cTime - pTime)
#         pTime = cTime 

#         cv2.putText(img,str(int(fps)) , (10,70) , cv2.FONT_HERSHEY_PLAIN,
#                     3,(255,0,255),3)

#         cv2.imshow("Camera" , img)

#         if cv2.waitKey(1) == ord("q"):
#             break

#     cam.release()
#     cv2.destroyAllWindows()


# if __name__ == "__main__":
#     main()


import cv2
import numpy as np 
import time 
import os 
import mediapipe as mp 

class HandDetector():
    def __init__(self, mode=False, maxhands=2, detectionconf=0.5, trackingconf=0.5):
        self.mode = mode
        self.maxhands = maxhands
        self.detectionconf = detectionconf
        self.trackingconf = trackingconf
        
        self.mpHands = mp.solutions.hands 
        self.hands = self.mpHands.Hands(
            static_image_mode=self.mode,
            max_num_hands=self.maxhands,
            min_detection_confidence=self.detectionconf,
            min_tracking_confidence=self.trackingconf
        )
        self.HandDraw = mp.solutions.drawing_utils

    def find_Hands(self, img, flag_draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        result = self.hands.process(imgRGB)

        if result.multi_hand_landmarks: 
            for handlandm in result.multi_hand_landmarks:
                if flag_draw:
                    self.HandDraw.draw_landmarks(img, handlandm, self.mpHands.HAND_CONNECTIONS)
        return img

def main():
    pTime = 0 
    cTime = 0 
    cam = cv2.VideoCapture(0)
    detector = HandDetector()

    while True:
        success, img = cam.read()
        if not success:
            break
            
        img = detector.find_Hands(img)
        img = cv2.flip(img, 1)

        cTime = time.time()
        fps = 1/(cTime - pTime)
        pTime = cTime 

        cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN,
                    3, (255,0,255), 3)

        cv2.imshow("Camera", img)

        if cv2.waitKey(1) == ord("q"):
            break

    cam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()