import cv2
import numpy as np

cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    
    for (x, y, w, h) in faces:
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]

        eyes = eye_cascade.detectMultiScale(roi_gray)

        for (ex, ey, ew, eh) in eyes:
            eye_region = roi_color[ey:ey + eh, ex:ex + ew]
            eye_gray = cv2.cvtColor(eye_region, cv2.COLOR_BGR2GRAY)

            blurred_eye = cv2.GaussianBlur(eye_gray, (15, 15), 0)

            circles = cv2.HoughCircles(blurred_eye, cv2.HOUGH_GRADIENT, 1, minDist=30, param1=50, param2=30, minRadius=5, maxRadius=20)
            
            if circles is not None:
                circles = np.round(circles[0, :]).astype("int")

                for (cx, cy, r) in circles:
                    cv2.circle(eye_region, (cx, cy), r, (0, 255, 0), 2)
                    cv2.circle(eye_region, (cx, cy), 2, (0, 0, 255), 3)

            cv2.rectangle(frame, (x + ex, y + ey), (x + ex + ew, y + ey + eh), (255, 0, 0), 2)

    cv2.imshow("Eye Tracking", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
