import cv2
import mediapipe as mp
import numpy as np
import time
import pyautogui 

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(refine_landmarks=True, max_num_faces=1, min_detection_confidence=0.5, min_tracking_confidence=0.5)

cap = cv2.VideoCapture(0)

# define indices for left and right eye landmarks based on MediaPipe's face mesh model
LEFT_EYE_INDICES = [33, 133, 160, 159, 158, 144, 153, 145, 246]
RIGHT_EYE_INDICES = [362, 263, 387, 386, 385, 373, 380, 374, 466]

# initialize variables to store eye positions and calibration status
locked_left_eye = None
locked_right_eye = None
calibration_done = False
initial_left_eye_centroid = None
initial_right_eye_centroid = None

calibration_time = 5  
start_time = time.time()

# capture frames from webcam
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    h, w, _ = frame.shape

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = face_mesh.process(rgb_frame)

    if results.multi_face_landmarks:

        for face_landmarks in results.multi_face_landmarks:

            #  get positions of left and right eye landmarks
            left_eye = [(int(landmark.x * w), int(landmark.y * h)) for i, landmark in enumerate(face_landmarks.landmark) if i in LEFT_EYE_INDICES]
            right_eye = [(int(landmark.x * w), int(landmark.y * h)) for i, landmark in enumerate(face_landmarks.landmark) if i in RIGHT_EYE_INDICES]

            for point in left_eye:
                cv2.circle(frame, point, 2, (0, 255, 0), -1)
            for point in right_eye:
                cv2.circle(frame, point, 2, (0, 255, 0), -1)

            if not calibration_done:

                left_x, left_y, left_w, left_h = cv2.boundingRect(np.array(left_eye))
                right_x, right_y, right_w, right_h = cv2.boundingRect(np.array(right_eye))

                initial_left_eye_centroid = (left_x + left_w // 2, left_y + left_h // 2)
                initial_right_eye_centroid = (right_x + right_w // 2, right_y + right_h // 2)

                elapsed_time = time.time() - start_time
                cv2.putText(frame, f"Open your eyes wide! Calibration in progress...", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
                cv2.putText(frame, f"Time remaining: {int(calibration_time - elapsed_time)}s", (50, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)

                if elapsed_time >= calibration_time:
                    locked_left_eye = (left_x, left_y, left_w, left_h)
                    locked_right_eye = (right_x, right_y, right_w, right_h)
                    calibration_done = True
                    cv2.putText(frame, "Calibration complete!", (50, 110), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

            if calibration_done:
                current_left_eye_centroid = np.mean(left_eye, axis=0).astype(int)
                current_right_eye_centroid = np.mean(right_eye, axis=0).astype(int)

                # define thresholds for scrolling actions 
                scroll_up_threshold = 5  
                scroll_down_threshold = 5  

                # determine scrolling direction 
                if current_left_eye_centroid[1] - initial_left_eye_centroid[1] > scroll_down_threshold or current_right_eye_centroid[1] - initial_right_eye_centroid[1] > scroll_down_threshold:
                    pyautogui.scroll(-10)  
                    cv2.putText(frame, "Scrolling down!", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

                elif current_left_eye_centroid[1] - initial_left_eye_centroid[1] < -scroll_up_threshold or current_right_eye_centroid[1] - initial_right_eye_centroid[1] < -scroll_up_threshold:
                    pyautogui.scroll(10)  
                    cv2.putText(frame, "Scrolling up!", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    
    cv2.namedWindow("Eye Tracking and Scrolling", cv2.WINDOW_NORMAL)
    cv2.imshow("Eye Tracking and Scrolling", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

if __name__ == "__main__":
    cap.release()
    cv2.destroyAllWindows()

