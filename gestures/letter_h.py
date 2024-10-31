def is_letter_h(landmarks, handedness):
    
    ''' H: knuckles facing forward. Index and middle finger straight and horizontal. Other fingers curled to palm. Thumb hidden'''
    
    if not landmarks:
        return False

    index_tip = landmarks["index_tip"]
    middle_tip = landmarks["middle_tip"]
    ring_tip = landmarks["ring_tip"]
    pinky_tip = landmarks["pinky_tip"]
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
    middle_horiz = (
        (middle_tip.x < middle_2.x if is_right_hand
        else middle_tip.x > middle_2.x)
        and
        abs(middle_tip.y - middle_2.y) < 0.1
    )

    # Index above middle finger
    index_above_middle= (
        index_2.y < middle_2.y
    )

    # Non index fingers curled to palm
    if is_right_hand:
        non_index_curled = (
            ring_2.x < ring_tip.x and
            pinky_2.x < pinky_tip.x
        )
    else:
        non_index_curled = (
            ring_2.x > ring_tip.x and
            pinky_2.x > pinky_tip.x
        )


    return index_horiz and middle_horiz and index_above_middle and non_index_curled