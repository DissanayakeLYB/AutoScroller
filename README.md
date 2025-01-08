# AutoScroller 👁️

This project implements an eye-tracking system using Python and MediaPipe to scroll a page based on eye movements. This is accomplished by detecting the eyes, calibrating their size and position, and allowing scroll both up and down based on the vertical movement of the eyes.

---

## Features

- **Real-time Eye Detection** - Detects left and right eyes and separates the iris (black region) from the sclera (white region).

- **Calibration Mode** - Captures the initial eye size and position with user interaction to lock reference points.

- **Scroll Control** - Scrolls the screen up or down based on the detected eye movements relative to the calibrated position.

- **Efficient Tracking** - Optimized for one face at a time to avoid false detections.

---

## Technologies Used

- **Python**: Programming language for the implementation.
- **OpenCV**: Library for real-time computer vision.
- **MediaPipe**: Framework for face and eye detection.
- **PyAutoGUI**: Library to simulate scrolling actions on the screen.
---
## Prerequisites

Before running the project, ensure you have the following dependencies installed.

- Python 3.7 or higher
- OpenCV: `pip install opencv-python`
- MediaPipe: `pip install mediapipe`
- NumPy: `pip install numpy`
- PyAutoGUI: `pip install pyautogui`

---

## How It Works

1. **Initialization**:
   - The program initializes the webcam and sets up MediaPipe to apply the mesh detection for the eyes.
   
2. **Calibration**:
   - The user is prompted to open their eyes wide during a calibration phase, which is a 5 second window.
   - During calibration, the system determines the size and position of the eyes and locks them as a reference.

3. **Tracking**:
   - After calibration, the system tracks the eyes in real time.
   - It detects vertical movement of the eyes relative to the reference position.

4. **Scroll Control**:
   - If the eyes move downward significantly, the window which the mouse cursor is on scrolls down.
   - If the eyes move upward significantly, the window which the mouse cursor is on scrolls up.
----
## Usage

1. Clone the repository:
   ```bash
   https://github.com/DissanayakeLYB/AutoScroller.git
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the script:
   ```bash
   python AutoScroller.py
   ```

4. Follow the on-screen instructions for calibration.
   - Open your eyes wide until calibration completes.
   - After calibration, move your eyes up or down to trigger scrolling.

5. Press `q` to exit the application.

----

## Customization

- **Calibration Time**:
  - Adjust the calibration time by modifying the `calibration_time` variable in the script.

- **Scrolling Sensitivity**:
  - Modify the `scroll_up_threshold` and `scroll_down_threshold` variable to adjust how much vertical movement triggers scrolling.

----


## Contributions
Contributions are welcome! Please open an issue or submit a pull request for any improvements or features you want to add.

---

## License

This project is licensed under the  [MIT LICENSE](https://github.com/DissanayakeLYB/AutoScroller/blob/main/LICENSE).

---

Happy scrolling peeps! 😊
