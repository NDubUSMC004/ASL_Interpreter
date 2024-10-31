import cv2

def display_word(frame, word, position=(10, 50), font_scale=1, thickness=2, padding=10):
    """
    Display the word on the screen with a background rectangle.

    Args:
        frame: The current video frame.
        word: The current word to be displayed.
        position: Tuple of x, y coordinates for the text position.
        font_scale: Font scale for the displayed text.
        thickness: Thickness of the text.
        padding: Padding around the text.
    """
    word_text = ''.join(word)
    text_size, _ = cv2.getTextSize(word_text, cv2.FONT_HERSHEY_COMPLEX, font_scale, thickness)
    text_width, text_height = text_size
    x, y = position

    # Get frame dimensions
    frame_height, frame_width, _ = frame.shape

    # Adjust x position if the text goes beyond the frame width
    if x + text_width + padding > frame_width:
        x = frame_width - text_width - padding

    # Draw a filled rectangle as a background
    cv2.rectangle(frame, (x - padding, y - text_height - padding), 
                  (x + text_width + padding, y + padding), 
                  (0, 0, 0), -1)  # Black rectangle

    # Overlay the text on top of the rectangle
    cv2.putText(frame, word_text, (x, y), cv2.FONT_HERSHEY_COMPLEX, font_scale, (255, 255, 255), thickness)
