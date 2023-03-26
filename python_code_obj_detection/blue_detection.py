# Importing the modules
import cv2
import numpy as np
import serial

# Creating a serial object to communicate with COM3 port
ser = serial.Serial('COM3', 9600)

# Creating a video capture object to read from webcam
cap = cv2.VideoCapture(0)

# Defining the lower and upper limits of blue color in HSV format
blue_lower = np.array([100, 150, 0], np.uint8)
blue_upper = np.array([140, 255, 255], np.uint8)

# Looping until the user presses ESC key
while True:
    # Reading a frame from the webcam
    ret, frame = cap.read()

    # Converting the frame from BGR to HSV format
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Creating a mask for blue color using the HSV limits
    blue_mask = cv2.inRange(hsv, blue_lower, blue_upper)

    # Finding the contours of blue objects in the mask
    contours, hierarchy = cv2.findContours(blue_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Drawing the contours on the original frame
    cv2.drawContours(frame, contours, -1, (0, 255, 0), 2)

    # Looping through each contour
    for cnt in contours:
        # Calculating the area of the contour
        area = cv2.contourArea(cnt)

        # Ignoring small contours
        if area > 500:
            # Finding the centroid of the contour
            M = cv2.moments(cnt)
            cx = int(M['m10'] / M['m00'])
            cy = int(M['m01'] / M['m00'])

            # Drawing a circle at the centroid
            cv2.circle(frame, (cx, cy), 5, (0, 0, 255), -1)

            # Sending the x and y coordinates of the centroid to COM3 port as a string
            ser.write(f'{cx},{cy}\n'.encode())

    # Showing the frame with contours and centroids
    cv2.imshow('Frame', frame)

    # Waiting for a key press for 10 ms
    key = cv2.waitKey(10)

    # Breaking the loop if ESC key is pressed
    if key == 27:
        break

# Releasing the video capture object and closing all windows
cap.release()
cv2.destroyAllWindows()

