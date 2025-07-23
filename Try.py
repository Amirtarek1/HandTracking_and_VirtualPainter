# # import cv2
# # import numpy as np 
# # import time 
# # import os 

# # folderpath = "Colorsandsize"
# # myList = os.listdir(folderpath)
# # print(myList)


# # cap = cv2.VideoCapture(0)
# # cap.set(3,1024)
# # cap.set(4,1024)

# # while True:
# #     success , img = cap.read()

# #     cv2.imread("Image" , img)
# #     cv2.waitKey(1)


# # import cv2
# # import mediapipe as mp
# # import numpy as np
# # import os

# # class HandDrawingApp:
# #     def __init__(self):
# #         # Initialize MediaPipe hands
# #         self.mp_hands = mp.solutions.hands
# #         self.hands = self.mp_hands.Hands(
# #             static_image_mode=False,
# #             max_num_hands=1,
# #             min_detection_confidence=0.7,
# #             min_tracking_confidence=0.5
# #         )
# #         self.mp_drawing = mp.solutions.drawing_utils
        
# #         # Drawing settings
# #         self.drawing_color = (0, 255, 0)  # Default green
# #         self.pen_size = 5
# #         self.drawing_mode = True  # True for drawing, False for erasing
        
# #         # Color palette (BGR format)
# #         self.colors = {
# #             'red': (0, 0, 255),
# #             'green': (0, 255, 0),
# #             'blue': (255, 0, 0),
# #             'yellow': (0, 255, 255),
# #             'purple': (128, 64, 128)
# #         }
        
# #         # UI button regions (x, y, width, height) - Adjusted to match your image
# #         self.control_buttons = {
# #             'eraser': (50, 50, 100, 50),
# #             'clear': (160, 50, 100, 50)
# #         }
        
# #         self.pen_size_buttons = {
# #             '5': (50, 150, 100, 30),
# #             '10': (50, 190, 100, 30),
# #             '15': (50, 230, 100, 30),
# #             '20': (50, 270, 100, 30)
# #         }
        
# #         # Drawing canvas
# #         self.canvas = None
# #         self.prev_x, self.prev_y = None, None
        
# #     def load_background(self, bg_path):
# #         """Load and resize background image"""
# #         if os.path.exists(bg_path):
# #             bg = cv2.imread(bg_path)
# #             return cv2.resize(bg, (800, 600))
# #         else:
# #             # Create a simple background if file doesn't exist
# #             bg = np.ones((600, 800, 3), dtype=np.uint8) * 240
# #             self.draw_ui_elements(bg)
# #             return bg
    
# #     def draw_ui_elements(self, img):
# #         """Draw UI elements on the image to match Colors.png"""
# #         # Draw control buttons
# #         cv2.rectangle(img, (50, 50), (150, 100), (200, 200, 200), -1)
# #         cv2.rectangle(img, (50, 50), (150, 100), (0, 0, 0), 2)
# #         cv2.putText(img, 'Eraser', (60, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)
        
# #         cv2.rectangle(img, (160, 50), (260, 100), (200, 200, 200), -1)
# #         cv2.rectangle(img, (160, 50), (260, 100), (0, 0, 0), 2)
# #         cv2.putText(img, 'Clear', (180, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)
        
# #         # Draw pen label and size buttons
# #         cv2.putText(img, 'Pen', (60, 140), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)
        
# #         sizes = ['5', '10', '15', '20']
# #         for i, size in enumerate(sizes):
# #             y = 150 + i * 40
# #             cv2.rectangle(img, (50, y), (150, y + 30), (150, 150, 150), -1)
# #             cv2.rectangle(img, (50, y), (150, y + 30), (0, 0, 0), 2)
# #             cv2.putText(img, size, (90, y + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)
    
# #     def is_point_in_rect(self, point, rect):
# #         """Check if point is inside rectangle"""
# #         x, y = point
# #         rx, ry, rw, rh = rect
# #         return rx <= x <= rx + rw and ry <= y <= ry + rh
    
# #     def handle_ui_interaction(self, finger_tip):
# #         """Handle interaction with UI elements"""
# #         x, y = finger_tip
        
# #         # Check control buttons
# #         if self.is_point_in_rect((x, y), self.control_buttons['eraser']):
# #             self.drawing_mode = False
# #             print("Eraser mode activated")
# #             return True
        
# #         if self.is_point_in_rect((x, y), self.control_buttons['clear']):
# #             self.canvas = np.zeros((600, 800, 3), dtype=np.uint8)
# #             print("Canvas cleared")
# #             return True
        
# #         # Check pen size buttons
# #         for size, rect in self.pen_size_buttons.items():
# #             if self.is_point_in_rect((x, y), rect):
# #                 self.pen_size = int(size)
# #                 print(f"Pen size set to: {size}")
# #                 return True
        
# #         return False
    
# #     def process_frame(self, frame):
# #         """Process each frame for hand detection and drawing"""
# #         frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
# #         results = self.hands.process(frame_rgb)
        
# #         if results.multi_hand_landmarks:
# #             for hand_landmarks in results.multi_hand_landmarks:
# #                 # Get index finger tip coordinates
# #                 index_finger_tip = hand_landmarks.landmark[8]
# #                 h, w, _ = frame.shape
# #                 finger_x = int(index_finger_tip.x * w)
# #                 finger_y = int(index_finger_tip.y * h)
                
# #                 # Check if interacting with UI
# #                 ui_interaction = self.handle_ui_interaction((finger_x, finger_y))
                
# #                 # Draw if not interacting with UI and in drawing area
# #                 if not ui_interaction and finger_x > 200:  # Right side of UI area
# #                     if self.prev_x is not None and self.prev_y is not None:
# #                         if self.drawing_mode:
# #                             cv2.line(self.canvas, (self.prev_x, self.prev_y), 
# #                                    (finger_x, finger_y), self.drawing_color, self.pen_size)
# #                         else:
# #                             # Eraser mode
# #                             cv2.circle(self.canvas, (finger_x, finger_y), 
# #                                      self.pen_size * 2, (0, 0, 0), -1)
                    
# #                     self.prev_x, self.prev_y = finger_x, finger_y
# #                 else:
# #                     self.prev_x, self.prev_y = None, None
                
# #                 # Draw hand landmarks
# #                 self.mp_drawing.draw_landmarks(frame, hand_landmarks, 
# #                                              self.mp_hands.HAND_CONNECTIONS)
                
# #                 # Draw finger tip indicator
# #                 cv2.circle(frame, (finger_x, finger_y), 10, (255, 0, 255), -1)
# #         else:
# #             self.prev_x, self.prev_y = None, None
        
# #         return frame
    
# #     def run(self):
# #         """Main application loop"""
# #         cap = cv2.VideoCapture(0)
        
# #         if not cap.isOpened():
# #             print("Error: Could not open webcam")
# #             return
        
# #         # Set camera resolution
# #         cap.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
# #         cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)
        
# #         # Initialize canvas
# #         self.canvas = np.zeros((600, 800, 3), dtype=np.uint8)
        
# #         # Load background (use None if you want to draw UI elements programmatically)
# #         try:
# #             background = self.load_background('Colors.png')
# #         except:
# #             background = np.ones((600, 800, 3), dtype=np.uint8) * 240
# #             self.draw_ui_elements(background)
        
# #         print("Virtual Painter Started!")
# #         print("Controls:")
# #         print("- Point with index finger to draw (right side of screen)")
# #         print("- Touch 'Eraser' to switch to eraser mode")
# #         print("- Touch 'Clear' to clear the canvas")
# #         print("- Touch numbers to change brush size")
# #         print("- Press 'q' to quit")
        
# #         while True:
# #             ret, frame = cap.read()
# #             if not ret:
# #                 break
            
# #             # Flip frame horizontally for mirror effect
# #             frame = cv2.flip(frame, 1)
            
# #             # Resize frame to match background
# #             frame = cv2.resize(frame, (800, 600))
            
# #             # Process frame for hand detection
# #             frame = self.process_frame(frame)
            
# #             # Combine background, canvas, and camera feed
# #             # Create a semi-transparent overlay
# #             overlay = background.copy()
            
# #             # Add canvas drawings to overlay
# #             mask = np.any(self.canvas != [0, 0, 0], axis=-1)
# #             overlay[mask] = self.canvas[mask]
            
# #             # Blend with camera feed
# #             alpha = 0.7  # Transparency of overlay
# #             result = cv2.addWeighted(frame, 1-alpha, overlay, alpha, 0)
            
# #             # Display current mode and settings
# #             mode_text = "Drawing" if self.drawing_mode else "Eraser"
# #             cv2.putText(result, f"Mode: {mode_text}", (10, 550), 
# #                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
# #             cv2.putText(result, f"Size: {self.pen_size}", (10, 580), 
# #                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            
# #             cv2.imshow('Virtual Painter', result)
            
# #             if cv2.waitKey(1) & 0xFF == ord('q'):
# #                 break
        
# #         cap.release()
# #         cv2.destroyAllWindows()

# # if __name__ == "__main__":
# #     app = HandDrawingApp()
# #     app.run()



#  to release a video 
# import cv2

# cam = cv2.VideoCapture(0)
# frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
# frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT)) 

# codec = cv2.VideoWriter_fourcc(*"mp4v")
# # out = cv2.VideoWriter("output.mp4",codec,20.0 , ( frame_width , frame_height))

# while True :
#     ret , frame = cam.read()

#     # out.write(frame)

#     cv2.imshow("Camera" , frame)

#     if cv2.waitKey(1) == ord("q"):
#         break

# cam.release()
# # out.release()
# cv2.destroyAllWindows()

# open camera
# import cv2

# cam = cv2.VideoCapture(0)

# while True :
#     ret , frame = cam.read()


#     cv2.imshow("Camera" , frame)

#     if cv2.waitKey(1) == ord("q"):
#         break

# cam.release()
# cv2.destroyAllWindows()

