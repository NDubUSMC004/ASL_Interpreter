def is_letter_p(landmarks, handedness):
    
    ''' P: Index Horizonal and Middle finger down, other fingers curled towards wrist. Thumb between index and middle finger pointing horizontal'''
    
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
    middle_3 = landmarks["middle_3"]
    wrist = landmarks["wrist"]

    is_right_hand = handedness == "Right"
    
    # index tip higher than all knuckle 2(y increases down!)
    index_is_horiz = (
        index_tip.x < index_2.x if is_right_hand
        else index_2.x < index_tip.x
    )

    # index tip higher than all knuckle 2(y increases down!)
    middle_is_down = (
        index_2.y < middle_tip.y and 
        middle_2.y < middle_tip.y
    )

    # Other fingers are curved towards wrist
    fingers_towards_wrist = (
        abs(ring_tip.x - wrist.x) < abs(ring_2.x - wrist.x) and
        abs(pinky_tip.x - wrist.x) < abs(pinky_2.x - wrist.x)
    )

    # Thumb is up
    thumb_between_fingers = (
        index_2.y < thumb_tip.y and
        middle_3.y < middle_tip.y
    )

    return index_is_horiz and middle_is_down and fingers_towards_wrist and thumb_between_fingers and thumb_between_fingers