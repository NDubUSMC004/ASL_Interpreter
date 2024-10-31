def is_letter_q(landmarks, handedness):
    
    ''' Q: Index finger and thumb straight down. Other fingers curled towards wrist and higher than finger/thumb tips'''
    
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
    wrist = landmarks["wrist"]

    is_right_hand = handedness == "Right"
    
    # Index extended down
    index_down = (
        index_2.y < index_tip.y and
        middle_2.y < index_tip.y and
        ring_2.y < index_tip.y and
        pinky_2.y < index_tip.y
    )

    # Thumb extended down
    thumb_down = (
        index_2.y < thumb_tip.y and
        middle_2.y < thumb_tip.y and
        ring_2.y < thumb_tip.y and
        pinky_2.y < thumb_tip.y
    )

    # Index above other fingers
    # Other fingers are curved towards wrist
    fingers_towards_wrist = (
        abs(middle_tip.x - wrist.x) < abs(middle_2.x - wrist.x) and
        abs(ring_tip.x - wrist.x) < abs(ring_2.x - wrist.x) and
        abs(pinky_tip.x - wrist.x) < abs(pinky_2.x - wrist.x)
    )


    return index_down and thumb_down and fingers_towards_wrist