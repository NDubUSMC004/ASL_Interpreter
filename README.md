# Sign Language Interpreter

A real-time American Sign Language (ASL) interpreter that uses computer vision to recognize hand gestures and translate them into readable text.

## 📌 Project Overview

The **Sign Language Interpreter** project aims to bridge the communication gap by providing a real-time translation system for American Sign Language. This interpreter uses computer vision techniques to detect and interpret ASL fingerspelling gestures, translating them into readable English text for seamless interaction. This project combines the power of machine learning and image processing to enhance accessibility for the Deaf and Hard-of-Hearing communities.

## 🎯 Features

- **Real-time Hand Tracking**: Utilizes computer vision to track hand positions dynamically.
- **ASL Alphabet Recognition**: Recognizes and translates individual ASL letters into text.

## 📦 Installation

### Prerequisites
1. Python 3.7+ is required.
2. Install the following dependencies:
   - OpenCV
   - Mediapipe

## 🚀 Usage

Open a terminal in the project directory.
Run the ASL hand detector script:
```bash
python asl_hand_detector.py
```
Allow the application to access your webcam for live gesture detection.
The interpreter will display detected ASL letters as text on the screen. The word remains on the screen until hands leave and return to the frame.
### Keyboard Shortcuts 
- ESC - Exit the application
- R - Reset the display text

## 📂 Project Structure

- asl_hand_detector.py: Main script for hand gesture recognition and ASL translation.
- utils/: Contains additional helper files and the hand landmark model 

## 👷‍♂️ How It Works

Hand Detection: The script uses Mediapipe’s hand landmark detection model to identify hand positions in real-time.
Feature Extraction: Key points in hand positions are extracted and analyzed to identify distinct ASL letter gestures.
Text Display: Identified letters are compiled and displayed as text. Persistent display logic ensures that the last recognized word remains visible until the interpreter continues.

## 🔨 Future Improvements

- **Extend to Full ASL Interpretation**: Expand the project beyond letter recognition to interpret full ASL signs, allowing it to recognize entire words, phrases, and more complex sentence structures.
- **Add Word Recognition**: Extend the interpreter to recognize whole words or phrases, providing a smoother and more practical user experience.
- **Non-Manual Signs**: Incorporate facial expressions and body language, which are integral parts of ASL, to support a more complete and accurate translation.
- **UI Enhancements**: Develop a more user-friendly graphical interface for easier interaction and accessibility.

## 🛠 Troubleshooting

- Camera Not Detected: Make sure your webcam is connected and accessible.
- Slow Performance: Try reducing the resolution of the webcam feed or optimizing Mediapipe settings.

## 📬 Contact
For questions or feedback, please feel free to reach out to Kaleb at turnerkaleb4@gmail.com or create an issue in this repository.

