
import cv2
import mediapipe as mp
from utils.letter_dictionary import get_letter_dict
from utils.display_text import display_word
from utils.hand_processing import process_hand_landmarks
from utils.letter_state_manager import LetterStateManager

# Initialize MediaPipe Hands and other required components
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils
capture = cv2.VideoCapture(0)
letter_dict = get_letter_dict()

# Configuration variable to toggle landmark drawing
draw_landmarks = False

# Initialize the letter state manager
confirmation_threshold = 15
state_manager = LetterStateManager(confirmation_threshold)
hands_off_screen = False

while capture.isOpened():
    ret, frame = capture.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect hand landmarks and determine letter
    new_letter, landmarks = process_hand_landmarks(frame_rgb, hands, letter_dict)

    # Draw landmarks on the frame if enabled
    if draw_landmarks and landmarks:
        for hand_landmarks in landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp.solutions.hands.HAND_CONNECTIONS)

    # Update state variables if hand is detected
    if landmarks:
        if hands_off_screen:  # Hands have returned after leaving screen
            state_manager.reset_state()
            hands_off_screen = False

        # Update the letter state
        state_manager.update_letter(new_letter)
    else:
        # Set flag for hands leaving the screen
        hands_off_screen = True

    # Display the current word on the screen
    current_word = state_manager.get_word()
    display_word(frame, current_word)

    # Show the frame
    cv2.imshow('ASL Hand Detector', frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

capture.release()
cv2.destroyAllWindows()