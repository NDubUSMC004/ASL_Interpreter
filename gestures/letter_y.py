def is_letter_y(landmarks, handedness):
    
    ''' Y: Pinky pointed up, other fingers folded down, thumb away from index'''
    
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

    # Thumb is away from index (distinguish from 'I')
    thumb_away_from_index = (
        abs(thumb_tip.x - index_2.x) > 0.075
    )

    # Pinky is on the outside of the hand
    pinky_outside = (
        pinky_tip.x > index_2.x if is_right_hand
        else pinky_tip.x < index_2.x
    )

    return pinky_is_up and fingers_curled and thumb_away_from_index and pinky_outside