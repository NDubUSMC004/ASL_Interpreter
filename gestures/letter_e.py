def is_letter_e(landmarks, handedness):
        
    ''' E: All fingers curl down, thumb across palm and lower than fingers, hand facing forwards'''
    
    if not landmarks:
        return False

    thumb_tip = landmarks["thumb_tip"]
    index_tip = landmarks["index_tip"]
    middle_tip = landmarks["middle_tip"]
    ring_tip = landmarks["ring_tip"]
    pinky_tip = landmarks["pinky_tip"]
    index_3 = landmarks["index_3"]
    middle_3 = landmarks["middle_3"]
    ring_3 = landmarks["ring_3"]
    pinky_3 = landmarks["pinky_3"]
    index_1 = landmarks["index_1"]
    pinky_1 = landmarks["pinky_1"]

    fingers_curled_down = (
        index_3.y < index_tip.y and
        middle_3.y < middle_tip.y and
        ring_3.y < ring_tip.y and
        pinky_3.y < pinky_tip.y 
    )
    
    thumb_across_palm = (
        index_1.x < thumb_tip.x < pinky_1.x or # left hand
        pinky_1.x < thumb_tip.x < index_1.x # right hand
    )

    thumb_below_fingers = (
        index_tip.y < thumb_tip.y and
        middle_tip.y < thumb_tip.y and
        ring_tip.y < thumb_tip.y and
        pinky_tip.y < thumb_tip.y
    )

    hand_is_not_sideways = (
        abs(index_tip.x - index_1.x) < 0.1
    )

    return (
       fingers_curled_down and thumb_across_palm and thumb_below_fingers and hand_is_not_sideways
    )