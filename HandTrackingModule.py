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
        self.result = None  # Initialize result as None

    def find_Hands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.result = self.hands.process(imgRGB) 
        
        if self.result.multi_hand_landmarks: 
            for handlandm in self.result.multi_hand_landmarks:
                if draw:
                    self.HandDraw.draw_landmarks(img, handlandm, self.mpHands.HAND_CONNECTIONS)
        return img

    def findPosition(self, img, handnumber=0, draw=True):
        lmlist = []
        if self.result and self.result.multi_hand_landmarks: 
            myHand = self.result.multi_hand_landmarks[handnumber]
            for id, lm in enumerate(myHand.landmark):
                height, weight, channel = img.shape 
                cx, cy = int(lm.x*weight), int(lm.y*height)
                lmlist.append([id, cx, cy])
                if draw:  
                    cv2.circle(img, (cx, cy), 10, (255, 0, 255), cv2.FILLED)
        return lmlist


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
        lmlist = detector.findPosition(img)
        if len(lmlist) != 0:
            print(lmlist[4])

        

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