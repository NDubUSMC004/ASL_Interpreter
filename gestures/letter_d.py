def is_letter_d(landmarks, handedness):
    
    ''' D: Index finger up, other fingers down touching thumb. Hand could be forwards or sideways'''
    
    if not landmarks:
        return False

    thumb_tip = landmarks["thumb_tip"]
    index_tip = landmarks["index_tip"]
    middle_tip = landmarks["middle_tip"]
    ring_tip = landmarks["ring_tip"]
    pinky_tip = landmarks["pinky_tip"]
    index_1 = landmarks["index_1"]
    thumb_2 = landmarks["thumb_2"]
    index_2 = landmarks["index_2"]
    middle_2 = landmarks["middle_2"]
    ring_2 = landmarks["ring_2"]
    pinky_2 = landmarks["pinky_2"]

    is_right_hand = handedness == "Right"
    
    # index tip higher than all knuckle 2(y increases down!)
    index_is_up = (
        index_tip.y < index_2.y and
        index_tip.y < middle_2.y and
        index_tip.y < ring_2.y and
        index_tip.y < pinky_2.y
    )

    # Other fingers are curved downwards
    fingers_curved_down = (
        middle_2.y < middle_tip.y and
        ring_2.y < ring_tip.y and
        pinky_2.y < pinky_tip.y
    )

    # Thumb is curved upwards
    thumb_curved_up = (
        thumb_tip.y < thumb_2.y
    )

    # thumb across palm
    thumb_across_palm = (
        index_1.x < thumb_tip.x if is_right_hand
        else thumb_tip.x < index_1.x
    )

    # Thumb meets fingers
    thumb_meets_fingers = (
        abs(thumb_tip.y - middle_tip.y) < 0.07
    )

    return index_is_up and fingers_curved_down and thumb_curved_up and thumb_across_palm and thumb_meets_fingers