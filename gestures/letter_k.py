def is_letter_k(landmarks, handedness):
    
    ''' K: Index and Middle finger up, other fingers down. Thumb between index and middle finger pointing up'''
    
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

    is_right_hand = handedness == "Right"
    
    # index tip higher than all knuckle 2(y increases down!)
    index_is_up = (
        index_tip.y < index_2.y and
        index_tip.y < ring_2.y and
        index_tip.y < pinky_2.y
    )

    # index tip higher than all knuckle 2(y increases down!)
    middle_is_up = (
        middle_tip.y < middle_2.y and
        middle_tip.y < ring_2.y and
        middle_tip.y < pinky_2.y
    )

    # Other fingers are curved downwards
    other_fingers_are_down = (
        ring_2.y < ring_tip.y and
        pinky_2.y < pinky_tip.y
    )

    # Thumb is up
    thumb_is_up = (
        thumb_tip.y < thumb_2.y
    )

    # Thumb between fingers
    thumb_between_fingers = (
       (index_tip.x <  thumb_tip.x < middle_tip.x) if is_right_hand
       else (middle_tip.x <  thumb_tip.x < index_tip.x)
    )

    return index_is_up and middle_is_up and other_fingers_are_down and thumb_is_up and thumb_between_fingers