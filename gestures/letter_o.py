def is_letter_o(landmarks, handedness):
    
    ''' O: Fingers and thumb curved in shape of 'O' with fingers above thumb, the hand is sideways, and the thumb does not meet fingers'''
    
    if not landmarks:
        return False

    thumb_tip = landmarks["thumb_tip"]
    index_tip = landmarks["index_tip"]
    middle_tip = landmarks["middle_tip"]
    ring_tip = landmarks["ring_tip"]
    pinky_tip = landmarks["pinky_tip"]
    index_1 = landmarks["index_1"]
    index_2 = landmarks["index_2"]
    middle_2 = landmarks["middle_2"]
    ring_2 = landmarks["ring_2"]
    
    # Fingers are above thumb (y increases down!)
    fingers_above_thumb = (
        index_tip.y < thumb_tip.y and
        middle_tip.y < thumb_tip.y and
        ring_tip.y < thumb_tip.y and
        pinky_tip.y < thumb_tip.y
    )

    # 2nd knuckly higher than tip (Fingers are slightly curved towards the palm)
    # I find that in practice the pinky does not always follow this rule, so lets ignore it 
    fingers_curved = (
        index_2.y < index_tip.y and
        middle_2.y < middle_tip.y and
        ring_2.y < ring_tip.y
    )

    # The hand is sideways
    hand_is_sideways = (
        abs(index_tip.x - index_1.x) > 0.1
    )

    # Thumb does not meets fingers
    thumb_meets_fingers = (
        abs(thumb_tip.y - middle_tip.y) < 0.05
    )
    
    return fingers_above_thumb and fingers_curved and hand_is_sideways and thumb_meets_fingers