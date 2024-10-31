class LetterStateManager:
    def __init__(self, confirmation_threshold):
        self.confirmation_threshold = confirmation_threshold
        self.reset_state()  # Initialize all state variables

    def reset_state(self):
        """Resets the state variables to their initial values."""
        self.current_letter = None
        self.detection_count = 0
        self.same_letter_count = 0
        self.last_letter = None
        self.awaiting_new_letter = False
        self.word = []

    def update_letter(self, new_letter):
        """
        Updates the letter state based on detection count and confirmation threshold.

        Args:
            new_letter: The detected letter from the current frame.
        """
        if self.awaiting_new_letter:
            if new_letter != self.last_letter:
                self.awaiting_new_letter = False  # User changed the letter
                self.detection_count = 1  # Start counting detections for new_letter
                self.current_letter = None  # Reset current_letter
                self.same_letter_count = 0
            else:
                # Still the same letter, do nothing
                self.detection_count = 0
                self.same_letter_count = 0
        else:
            if new_letter == self.current_letter:
                self.same_letter_count += 1
                self.detection_count = 0  # Reset detection count since the letter hasn't changed
                if self.same_letter_count >= 3 * self.confirmation_threshold:
                    if self.word and self.word[-1] != ' ':  # Only add space if last letter is not space
                        self.word.append(' ')
                    self.same_letter_count = 0  # Reset same_letter_count after adding space
                    self.awaiting_new_letter = True  # Wait for a new letter
                    self.last_letter = self.current_letter
                    self.current_letter = None
                    self.detection_count = 0
            else:
                self.same_letter_count = 0  # Reset same_letter_count since letter changed
                self.detection_count += 1
                if self.detection_count >= self.confirmation_threshold:
                    self.current_letter = new_letter
                    self.detection_count = 0  # Reset detection count
                    if self.current_letter:
                        if self.current_letter == "That is rude!": # Easter egg... user flipped off camera
                            self.word = [] # Reset any text on screen
                        self.word.append(self.current_letter)
                        self.last_letter = self.current_letter
                        

    def get_word(self):
        """Returns the current word as a string."""
        return ''.join(self.word)
