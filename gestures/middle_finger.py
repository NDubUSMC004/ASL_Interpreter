def is_middle_finger(landmarks, handedness):
    
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

    thumb_is_up = (
        thumb_tip.y < index_tip.y and
        thumb_tip.y < pinky_tip.y and
        thumb_tip.y < ring_tip.y
    )

    middle_is_up = (
        middle_tip.y < index_tip.y and
        middle_tip.y < ring_tip.y and
        middle_tip.y < pinky_tip.y
    )

    fingers_curled = (
        index_2.y < index_tip.y and
        ring_2.y < ring_tip.y
    )

    pinky_inside = (
        pinky_tip.x < index_2.x if is_right_hand
        else pinky_tip.x > index_2.x
    )

    return thumb_is_up and middle_is_up and fingers_curled and pinky_inside