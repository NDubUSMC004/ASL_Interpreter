from utils.landmarks import update_landmarks

def process_hand_landmarks(frame, hands, letter_dict):
    """
    Processes hand landmarks in the RGB frame and returns detected letters and landmarks.

    Args:
        frame: The RGB frame for processing.
        hands: MediaPipe hands solution instance.
        letter_dict: Dictionary mapping letters to identifying functions.

    Returns:
        Tuple containing the letter detected and multi-hand landmarks.
    """
    results = hands.process(frame)
    new_letter = None

    if results.multi_hand_landmarks:
        for hand_landmarks, handedness_label in zip(results.multi_hand_landmarks, results.multi_handedness):
            # Get right vs left hand label
            handedness = handedness_label.classification[0].label
            landmark_points = update_landmarks(hand_landmarks.landmark)

            # Check for specific hand letter using the dictionary
            for letter, check_function in letter_dict.items():
                if check_function(landmark_points, handedness):
                    new_letter = letter
                    break

    return new_letter, results.multi_hand_landmarks
