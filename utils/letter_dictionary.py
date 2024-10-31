from gestures.letter_a import is_letter_a
from gestures.letter_b import is_letter_b
from gestures.letter_c import is_letter_c
from gestures.letter_d import is_letter_d
from gestures.letter_e import is_letter_e
from gestures.letter_f import is_letter_f
from gestures.letter_g import is_letter_g
from gestures.letter_h import is_letter_h
from gestures.letter_i import is_letter_i
from gestures.letter_j import is_letter_j
from gestures.letter_k import is_letter_k
from gestures.letter_l import is_letter_l
from gestures.letter_m import is_letter_m
from gestures.letter_n import is_letter_n
from gestures.letter_o import is_letter_o
from gestures.letter_p import is_letter_p
from gestures.letter_q import is_letter_q
from gestures.letter_y import is_letter_y

from gestures.middle_finger import is_middle_finger

def get_letter_dict():
    """
    Returns a dictionary mapping each letter to its detection function.
    """
    return {
        "A": is_letter_a,
        "B": is_letter_b,
        "C": is_letter_c,
        "D": is_letter_d,
        "E": is_letter_e,
        "F": is_letter_f,
        "G": is_letter_g,
        "H": is_letter_h,
        "I": is_letter_i,
        "J": is_letter_j,
        "K": is_letter_k,
        "L": is_letter_l,
        "M": is_letter_m,
        "N": is_letter_n,
        "O": is_letter_o,
        "P": is_letter_p,
        "Q": is_letter_q,
        "Y": is_letter_y,

        "That is rude!": is_middle_finger
    }