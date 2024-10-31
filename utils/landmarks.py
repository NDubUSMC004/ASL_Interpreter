def update_landmarks(hand_landmarks):
    landmark_points = {
        "wrist": hand_landmarks[0],
        "thumb_1": hand_landmarks[1],
        "thumb_2": hand_landmarks[2],
        "thumb_3": hand_landmarks[3],
        "thumb_tip": hand_landmarks[4],
        "index_1": hand_landmarks[5],
        "index_2": hand_landmarks[6],
        "index_3": hand_landmarks[7],
        "index_tip": hand_landmarks[8],
        "middle_1": hand_landmarks[9],
        "middle_2": hand_landmarks[10],
        "middle_3": hand_landmarks[11],
        "middle_tip": hand_landmarks[12],
        "ring_1": hand_landmarks[13],
        "ring_2": hand_landmarks[14],
        "ring_3": hand_landmarks[15],
        "ring_tip": hand_landmarks[16],
        "pinky_1": hand_landmarks[17],
        "pinky_2": hand_landmarks[18],
        "pinky_3": hand_landmarks[19],
        "pinky_tip": hand_landmarks[20]
    }
    return landmark_points