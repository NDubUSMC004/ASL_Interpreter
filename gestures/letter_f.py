def is_letter_f(landmarks, handedness):
    
    ''' F: Index finger down touching thumb, other fingers straight up. Hand facing forwards'''
    
    if not landmarks:
        return False

    thumb_tip = landmarks["thumb_tip"]
    index_tip = landmarks["index_tip"]
    middle_tip = landmarks["middle_tip"]
    ring_tip = landmarks["ring_tip"]
    pinky_tip = landmarks["pinky_tip"]
    thumb_2 = landmarks["thumb_2"]
    index_2 = landmarks["index_2"]
    middle_2 = landmarks["middle_2"]
    ring_2 = landmarks["ring_2"]
    pinky_2 = landmarks["pinky_2"]
    
    # Outside 3 fingers straight up
    non_index_fingers_pointed_up = (
        middle_tip.y < middle_2.y and
        ring_tip.y < ring_2.y and
        pinky_tip.y < pinky_2.y
    )
    
    # index finger pointing down
    index_is_down = (
        index_2.y < index_tip.y
    )

    # Thumb is curved upwards
    thumb_curved_up = (
        thumb_tip.y < thumb_2.y
    )

    # Thumb meets fingers
    thumb_meets_fingers = (
        abs(thumb_tip.y - index_tip.y) < 0.07
    )

    return non_index_fingers_pointed_up and index_is_down and thumb_curved_up and thumb_meets_fingers