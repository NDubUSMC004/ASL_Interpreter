def is_letter_t(landmarks, handedness):
    
    ''' T: All fingers folded down, thumb sticking up between index and middle finger'''
    
    if not landmarks:
        return False

    thumb_tip = landmarks["thumb_tip"]
    index_tip = landmarks["index_tip"]
    middle_tip = landmarks["middle_tip"]
    ring_tip = landmarks["ring_tip"]
    pinky_tip = landmarks["pinky_tip"]
    index_2 = landmarks["index_2"]
    middle_2 = landmarks["middle_2"]
    ring_2 = landmarks["ring_2"]
    pinky_2 = landmarks["pinky_2"]
    pinky_3 = landmarks["pinky_3"]

    is_right_hand = handedness == "Right"

    # Finger 2nd knuckles are higher than fingertips (fingers curled )
    fingers_curled = (
        index_2.y < index_tip.y and
        middle_2.y < middle_tip.y and
        ring_2.y < ring_tip.y and
        pinky_2.y < pinky_tip.y
    )


    thumb_between_index_middle = (
        thumb_tip.y < index_tip.y and
        thumb_tip.y < middle_tip.y and
        (
            (index_2.x < thumb_tip.x < middle_2.x) if is_right_hand
            else (middle_2.x < thumb_tip.x < index_2.x)
        )
    )

    return fingers_curled and thumb_between_index_middle