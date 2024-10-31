def is_letter_g(landmarks, handedness):
    
    ''' G: knuckles facing forward. Index finger and thumb straight and horizontal. Other fingers curled to palm'''
    
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
    
    # Index extended horizontally
    index_horiz = (
        (index_tip.x < index_2.x if is_right_hand
        else index_tip.x > index_2.x)
        and
        abs(index_tip.y - index_2.y) < 0.1
    )

    # Thumb extended horizontally
    thumb_horiz = (
        (thumb_tip.x < thumb_2.x if is_right_hand
        else thumb_tip.x > thumb_2.x)
        and
        abs(thumb_tip.y - thumb_2.y) < 0.1
    )

    # Index above other fingers
    index_above_others = (
        index_2.y < middle_2.y
    )

    # Thumb above other fingers
    thumb_above_others = (
        thumb_tip.y < ring_2.y
    )

    # Non index fingers curled to palm
    if is_right_hand:
        non_index_curled = (
            middle_2.x < middle_tip.x and
            ring_2.x < ring_tip.x and
            pinky_2.x < pinky_tip.x
        )
    else:
        non_index_curled = (
            middle_2.x > middle_tip.x and
            ring_2.x > ring_tip.x and
            pinky_2.x > pinky_tip.x
        )


    return index_horiz and thumb_horiz and index_above_others and thumb_above_others and non_index_curled