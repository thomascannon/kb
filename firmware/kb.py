from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners.keypad import KeysScanner

import board

_KEY_CFG_LEFT = [
    board.D13, board.D28, board.D12, board.D29, board.D0,
    board.D22, board.D14, board.D26, board.D4,  board.D27,
    board.D21, board.D23, board.D7,  board.D20, board.D6,
    board.D16, board.D9,  board.D8,
]

class KMKKeyboard(_KMKKeyboard):
    data_pin = board.D1

    coord_mapping = [
        00, 01, 02, 03, 04,    22, 21, 20, 19, 18,
        05, 06, 07, 08, 09,    27, 26, 25, 24, 23,
        10, 11, 12, 13, 14,    32, 31, 30, 29, 28,
                15, 16, 17,    35, 34, 33
    ]

    def __init__(self):
        self.matrix = KeysScanner(_KEY_CFG_LEFT)