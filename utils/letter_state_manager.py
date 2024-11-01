class LetterStateManager:
    def __init__(self, confirmation_threshold):
        """
        Initializes the LetterStateManager with a threshold for confirming a detected letter.
        
        Args:
            confirmation_threshold (int): The number of consistent detections required to confirm a letter.
        """
        self.confirmation_threshold = confirmation_threshold
        self.reset_state()  # Initialize all state variables

    def reset_state(self):
        """
        Resets the internal state of the letter detection system.
        
        Attributes reset:
            - current_letter: The letter currently being detected.
            - detection_count: Counter for consecutive detections of a new letter.
            - same_letter_count: Counter for consecutive detections of the same letter.
            - last_letter: The last confirmed letter.
            - awaiting_new_letter: Boolean to pause detection until a new letter appears.
            - word: List storing confirmed letters, forming the current word.
        """
        self.current_letter = None
        self.detection_count = 0
        self.same_letter_count = 0
        self.last_letter = None
        self.awaiting_new_letter = False
        self.word = []

    def update_letter(self, new_letter):
        """
        Updates the state based on the detected letter, handling consecutive detections,
        confirmation of letters, and spacing.

        Args:
            new_letter (str): The detected letter from the current frame.
        """
        # Check if system is waiting for a new letter after a pause or space addition
        if self.awaiting_new_letter:
            if new_letter != self.last_letter:
                # A new letter has been detected, reset detection variables
                self.awaiting_new_letter = False
                self.detection_count = 1  # Start counting detections for the new letter
                self.current_letter = None
                self.same_letter_count = 0
            else:
                # Still seeing the last letter, so reset counters without adding it
                self.detection_count = 0
                self.same_letter_count = 0
        else:
            if new_letter == self.current_letter:
                # Increment same_letter_count for consecutive detections of the current letter
                self.same_letter_count += 1
                self.detection_count = 0  # Reset detection count since the letter hasn't changed

                # Add space if the same letter is seen consistently beyond the threshold
                if self.same_letter_count >= 2 * self.confirmation_threshold:
                    if self.word and self.word[-1] != ' ':
                        self.word.append(' ')  # Only add space if the last letter isn't a space
                    self.same_letter_count = 0  # Reset counter after adding space
                    self.awaiting_new_letter = True  # Enter pause state, waiting for a new letter
                    self.last_letter = self.current_letter
                    self.current_letter = None
                    self.detection_count = 0
            else:
                # A new letter is detected, reset same_letter_count and increment detection count
                self.same_letter_count = 0
                self.detection_count += 1

                # Confirm new letter if detected consistently up to the confirmation threshold
                if self.detection_count >= self.confirmation_threshold:
                    self.current_letter = new_letter
                    self.detection_count = 0  # Reset detection count after confirming the letter

                    # Append the confirmed letter to the word if it is not an Easter egg case
                    if self.current_letter:
                        if self.current_letter == "That is rude!":  # Easter egg case: reset word
                            self.word = []  # Clear text on screen if the user flips off the camera
                        self.word.append(self.current_letter)  # Add confirmed letter to the word
                        self.last_letter = self.current_letter  # Update last confirmed letter

    def get_word(self):
        """
        Returns the current word as a string, formed by the confirmed letters.
        
        Returns:
            str: The current word constructed from the detected letters.
        """
        return ''.join(self.word)
