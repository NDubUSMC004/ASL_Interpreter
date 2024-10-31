def is_letter_b(landmarks, handedness):
        
    ''' B: All fingers straight up, thumb across palm'''
    
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
    index_1 = landmarks["index_1"]
    pinky_1 = landmarks["pinky_1"]

    fingers_pointed_up = (
        index_tip.y < index_2.y and
        middle_tip.y < middle_2.y and
        ring_tip.y < ring_2.y and
        pinky_tip.y < pinky_2.y
    )
    
    thumb_across_palm = (
        index_1.x < thumb_tip.x < pinky_1.x or # left hand
        pinky_1.x < thumb_tip.x < index_1.x # right hand
    )

    return (
       fingers_pointed_up and thumb_across_palm
    )