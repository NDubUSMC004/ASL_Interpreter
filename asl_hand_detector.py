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

# Variables for handling hands off-screen
hands_off_frame_count = 0  # Counter for frames with no hands detected
off_screen_reset_limit = 2 * confirmation_threshold  # Limit for off-screen frames before resetting

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

    # Check if hand landmarks are detected
    if landmarks:
        if hands_off_frame_count >= off_screen_reset_limit:
            # Reset the state only if hands were off-screen long enough before returning
            state_manager.reset_state()

        # Reset the hands-off screen counter now that hands are back
        hands_off_frame_count = 0

        # Update the letter state with the detected letter
        state_manager.update_letter(new_letter)
    else:
        # Increment counter when hands are off-screen
        hands_off_frame_count += 1

    # Display the current word on the screen
    current_word = state_manager.get_word()
    display_word(frame, current_word)

    # Show the frame
    cv2.imshow('ASL Hand Detector', frame)
    # Reset state when 'r' is pressed
    if cv2.waitKey(1) & 0xFF == ord("r"):
        state_manager.reset_state()
    # Close program when 'esc' is pressed
    elif cv2.waitKey(1) & 0xFF == 27:
        break

capture.release()
cv2.destroyAllWindows()
