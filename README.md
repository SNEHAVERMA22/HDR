# Hand Gesture Recognition and Classification

📷🤚🔢 A Python project that captures custom hand gestures through the webcam, trains a gesture classification model, and recognizes the gestures in real-time.

## Prerequisites

🐍 Python 3.x

## Installation

1. Clone the repository or download the code.

2. Install the required libraries from requirements.txt



## Usage

1. Ensure your webcam is connected to your computer.

2. Run the Jupyter notebook `Gesture_Training.ipynb`.

3. Specify the hand gesture labels you want to train the model on. These can be any gestures you want to recognize, such as 'thumbs_up', 'peace_sign', or 'wave'.

4. A video window will open, displaying your webcam feed.

5. Perform each hand gesture multiple times in front of the camera, following the instructions on the screen. Each gesture will be recorded and associated with the corresponding label.

6. Press the 'q' key to move on to the next gesture or to exit the recording process.

7. The recorded gesture coordinates and labels will be saved in a CSV file named `coords.csv`.

8. Run the Jupyter notebook `Gesture_Recognition.ipynb`.

9. The notebook will load the recorded gesture data from `coords.csv` and train a gesture classification model.

10. Once the model is trained, it will be saved in a pickle file named `model_pkl`.

11. The notebook will open a new video window showing your webcam feed.

12. The trained model will analyze the hand gestures in real-time and predict the corresponding label for each gesture.

13. The predicted labels will be displayed on the video screen.

14. Press the 'q' key to stop the gesture recognition process and exit the video window.

## Customization

- Feel free to customize the hand gesture labels by modifying the list in the `Gesture_Training.ipynb` notebook. Add or remove labels according to your desired gestures.

- You can modify and experiment with the classification model and its hyperparameters in the `Gesture_Recognition.ipynb` notebook to improve the accuracy of the gesture recognition.

- If you have multiple cameras, you can change the camera index value in the code to select a different camera for capturing video.


## Acknowledgments

🙏 This project utilizes the following libraries and technologies:

- OpenCV for video capture and display.
- Mediapipe for hand tracking and landmark detection.
- NumPy for numerical operations.
- Pandas for handling the recorded gesture data.
- Matplotlib for visualization.
- Scikit-learn for training and evaluating the gesture classification model.

Please note that this README assumes basic knowledge of Python and the mentioned libraries.

Enjoy recognizing hand gestures! 🤗✌️