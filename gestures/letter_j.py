def is_letter_j(landmarks, handedness):
    
    ''' J: Pinky pointed up on inside of hand, other fingers folded down, thumb straight up, thumb close to index'''
    
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

    is_right_hand = handedness == "Right"
    
    # thumb tip higher than non-pinky fingertips (y increases down!)
    thumb_is_up = (
        thumb_tip.y < index_tip.y and
        thumb_tip.y < middle_tip.y and
        thumb_tip.y < ring_tip.y
    )

    # Pinky pointed up
    pinky_is_up = (
        pinky_tip.y < index_tip.y and
        pinky_tip.y < middle_tip.y and
        pinky_tip.y < ring_tip.y
    )

    # Finger 2nd knuckles are higher than fingertips
    fingers_curled = (
        index_2.y < index_tip.y and
        middle_2.y < middle_tip.y and
        ring_2.y < ring_tip.y
    )

    # Thumb is close to index (distinguish from 'Y')
    thumb_close_to_index = (
        abs(thumb_tip.x - index_2.x) < 0.075
    )

    # Pinky is on the outside of the hand (distinguish from 'J')
    pinky_inside = (
        pinky_tip.x < index_2.x if is_right_hand
        else pinky_tip.x > index_2.x
    )

    return thumb_is_up and pinky_is_up and fingers_curled and thumb_close_to_index and pinky_inside