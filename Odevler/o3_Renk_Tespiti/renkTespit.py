import cv2
import numpy as np

def nothing(x):
    pass

cv2.namedWindow("Trackbars", cv2.WINDOW_AUTOSIZE)
cv2.namedWindow("Canli Takip", cv2.WINDOW_AUTOSIZE)


cv2.moveWindow("Trackbars", 100, 50)     
cv2.moveWindow("Canli Takip", 100, 320)   


cv2.createTrackbar("H_min", "Trackbars", 0, 179, nothing)
cv2.createTrackbar("H_max", "Trackbars", 100, 179, nothing)
cv2.createTrackbar("S_min", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("S_max", "Trackbars", 100, 255, nothing)
cv2.createTrackbar("V_min", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("V_max", "Trackbars", 100, 255, nothing)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    frame = cv2.resize(frame, (500, 360))
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos("H_min", "Trackbars")
    h_max = cv2.getTrackbarPos("H_max", "Trackbars")
    s_min = cv2.getTrackbarPos("S_min", "Trackbars")
    s_max = cv2.getTrackbarPos("S_max", "Trackbars")
    v_min = cv2.getTrackbarPos("V_min", "Trackbars")
    v_max = cv2.getTrackbarPos("V_max", "Trackbars")

    
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(hsv_frame, lower, upper)

    
    mask_3ch = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
 
    combined_view = np.hstack((frame, mask_3ch))

    cv2.imshow("Canli Takip", combined_view)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
