import cv2

header_path = "C:/HandTrackingProject/Colorsandsize/Colors.png"
header = cv2.imread(header_path)

# Check if the image is loaded properly
if header is None:
    raise FileNotFoundError(f"Image not found at {header_path}")

# Start camera
cam = cv2.VideoCapture(0)
cam.set(3, 1280)  # Width
cam.set(4, 720)   # Height

# Resize header to fit the frame width
header_height = 125
header_resized = cv2.resize(header, (1280, header_height))

while True:

    # 1. import image
    ret, frame = cam.read()
    frame = cv2.flip(frame, 1) 

    

    if not ret:
        print("Failed to grab frame")
        break





    # Overlay the header on the top part of the frame
    frame[0:125, 0:1280] = header_resized
    cv2.imshow("Camera with Background", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cam.release()
cv2.destroyAllWindows()