Sign Language Interpreter

A real-time American Sign Language (ASL) interpreter that uses computer vision to recognize hand gestures and translate them into readable text.
📌 Project Overview
The Sign Language Interpreter project aims to bridge the communication gap by providing a real-time translation system for American Sign Language. This interpreter uses computer vision techniques to detect and interpret ASL fingerspelling gestures, translating them into readable English text for seamless interaction. This project combines the power of machine learning and image processing to enhance accessibility for the Deaf and Hard-of-Hearing communities.

🎯 Features
Real-time Hand Tracking: Utilizes computer vision to track hand positions dynamically.
ASL Alphabet Recognition: Recognizes and translates individual ASL letters into text.
Persistent Display: Retains the displayed word on-screen until hands return to continue detection.
User-Friendly Interface: Simple, intuitive setup and real-time feedback.
📦 Installation
Prerequisites
Python 3.7+ is required.
Install the following dependencies:
OpenCV
Mediapipe (for hand landmark detection)
Any other dependencies in requirements.txt
Steps
Clone this repository:

bash
Copy code
git clone https://github.com/NDubUSMC004/sign_language_interpreter.git
Navigate into the project directory:

bash
Copy code
cd sign_language_interpreter
Install the dependencies:

bash
Copy code
pip install -r requirements.txt
Set Up Hand Landmarker Model: Ensure the hand_landmarker.task file is in the correct directory. Update the path if necessary in asl_hand_detector.py:

python
Copy code
hand_landmarker = mp.tasks.HandLandmarker.create_from_model_path(
    'C:\\Users\\Kaleb Turner\\OneDrive\\Desktop\\Python_Project\\utils\\hand_landmarker.task'
)
🚀 Usage
Open a terminal in the project directory.
Run the ASL hand detector script:
bash
Copy code
python asl_hand_detector.py
Allow the application to access your webcam for live gesture detection.
The interpreter will display detected ASL letters as text on the screen. The word remains on the screen until hands leave and return to the frame.
Keyboard Shortcuts (if any)
ESC - Exit the application
R - Reset the display text
Additional shortcuts can be added here as needed
📂 Project Structure
asl_hand_detector.py: Main script for hand gesture recognition and ASL translation.
utils/: Contains additional helper files and the hand landmark model (hand_landmarker.task).
requirements.txt: Lists all dependencies required for the project.
👷‍♂️ How It Works
Hand Detection: The script uses Mediapipe’s hand landmark detection model to identify hand positions in real-time.
Feature Extraction: Key points in hand positions are extracted and analyzed to identify distinct ASL letter gestures.
Text Display: Identified letters are compiled and displayed as text. Persistent display logic ensures that the last recognized word remains visible until the interpreter continues.
🔨 Future Improvements
Add Word Recognition: Extend the interpreter to recognize whole words or phrases.
Non-Manual Signs: Incorporate facial expressions or body language, vital components in ASL.
UI Enhancements: Develop a more user-friendly graphical interface for easier interaction.
Support for Other Sign Languages: Expand the project to support other sign languages (BSL, ISL, etc.).
🛠 Troubleshooting
Camera Not Detected: Make sure your webcam is connected and accessible.
Model Path Error: Ensure hand_landmarker.task is in the specified location or update the path in asl_hand_detector.py.
Slow Performance: Try reducing the resolution of the webcam feed or optimizing Mediapipe settings.
📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

📬 Contact
For questions or feedback, please feel free to reach out to Kaleb at your-email@example.com or create an issue in this repository.
