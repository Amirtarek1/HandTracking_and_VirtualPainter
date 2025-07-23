
###### to try 

import cv2
import mediapipe as mp
import time
import HandTrackingModule as htm

pTime = 0
cTime = 0
cap = cv2.VideoCapture(0)  # Changed from 1 to 0 (default camera)
detector = htm.HandDetector()

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    if not success:
        print("Failed to grab frame")
        break  # or continue to try again
    
    # Check if image is not empty
    if img is None:
        print("Empty frame received")
        continue
        
    try:
        img = detector.find_Hands(img, draw=False)
        lmList = detector.findPosition(img, draw=False)  
        if len(lmList) != 0:
            print(lmList[4])
    except Exception as e:
        print(f"Error in processing: {e}")
        continue

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 255), 3)

    cv2.imshow("Hand Tracking", img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()