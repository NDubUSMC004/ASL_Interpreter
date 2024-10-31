def is_letter_m(landmarks, handedness):
    
    ''' M: Fingers folded down, thumb under first three fingers, above pinky'''
    
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

    # Finger 2nd knuckles are higher than fingertips
    fingers_curled = (
        index_2.y < index_tip.y and
        middle_2.y < middle_tip.y and
        ring_2.y < ring_tip.y and
        pinky_2.y < pinky_tip.y
    )

    # thumb tip higher than pinky (y increases down!)
    thumb_above_pinky = (
        thumb_tip.y < pinky_3.y
    )

    thumb_under_ring = (
        ring_2.y < thumb_tip.y and
        (
            (ring_tip.x < thumb_tip.x) if is_right_hand
            else (thumb_tip.x < ring_tip.x)
        )
    )

    return fingers_curled and thumb_above_pinky and thumb_under_ring