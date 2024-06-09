from kb import KMKKeyboard

from kmk.keys import KC
from kmk.modules.holdtap import HoldTap, HoldTapRepeat
from kmk.modules.layers import Layers
from kmk.modules.dynamic_sequences import DynamicSequences
from kmk.modules.capsword import CapsWord
from kmk.modules.split import Split, SplitSide

# home row mods
def hrm(tap, hold):
    return KC.HT(tap, hold, prefer_hold=False, tap_interrupted=True,
                 tap_time=200, repeat=HoldTapRepeat.TAP)

# thumb layer taps
def tlt(layer, tap):
    return KC.LT(layer, tap, prefer_hold=True, repeat=HoldTapRepeat.TAP)

keyboard = KMKKeyboard()
layers = Layers()
holdtap = HoldTap()
dynamic_sequences = DynamicSequences()
capsword = CapsWord()
split = Split(data_pin=keyboard.data_pin, use_pio=True)

keyboard.modules = [layers, holdtap, dynamic_sequences, capsword, split]

_______ = KC.TRNS
xxxxxxx = KC.NO

SQ_REC = KC.RECORD_SEQUENCE()
SQ_PLY = KC.PLAY_SEQUENCE()
SQ_STP = KC.STOP_SEQUENCE()

# thumb cluster keys
LS_TAB  = KC.HT(KC.TAB, KC.LSFT, prefer_hold=True)
RS_ESC  = KC.HT(KC.ESC, KC.RSFT, prefer_hold=True)

LT_NVSP = tlt(1, KC.SPC)    # navigation or space
LT_SYET = tlt(2, KC.ENT)    # symbols or enter
LT_NUBS = tlt(3, KC.BSPC)   # numbers or backspace
LT_FKDL = tlt(4, KC.DEL)    # function keys or delete

# home row mods (pinky -> pointer = GUI, ALT, CTRL, SHIFT)
HM_ST = hrm(KC.T, KC.LSFT)
HM_CS = hrm(KC.S, KC.LCTL)
HM_AR = hrm(KC.R, KC.LALT)
HM_GA = hrm(KC.A, KC.LGUI)
HM_SN = hrm(KC.N, KC.RSFT)
HM_CE = hrm(KC.E, KC.LCTL)
HM_AI = hrm(KC.I, KC.LALT)
HM_GO = hrm(KC.O, KC.LGUI)

# special nav keys
LA_LEFT = KC.LALT(KC.LEFT)
LC_LEFT = KC.LCTRL(KC.LEFT)
LA_RGHT = KC.LALT(KC.RGHT)
LC_RGHT = KC.LCTRL(KC.RGHT)

keyboard.keymap = [
    # base colemak dh
    [
        KC.Q,    KC.W,    KC.F,    KC.P,    KC.B,       KC.J,    KC.L,    KC.U,    KC.Y,    KC.QUOT,
        HM_GA,   HM_AR,   HM_CS,   HM_ST,   KC.G,       KC.M,    HM_SN,   HM_CE,   HM_AI,   HM_GO,
        KC.Z,    KC.X,    KC.C,    KC.D,    KC.V,       KC.K,    KC.H,    KC.COMM, KC.DOT,  KC.SLSH,
                          LS_TAB,  LT_NVSP, LT_NUBS,    LT_FKDL, LT_SYET, RS_ESC
    ],
    # navigation
    [
        SQ_REC,  SQ_STP,  SQ_PLY,  xxxxxxx, xxxxxxx,    KC.PGUP, LA_LEFT, KC.UP,   LA_RGHT, xxxxxxx,
        KC.LGUI, KC.LALT, KC.LCTL, KC.LSFT, KC.TG(3),   KC.PGDN, KC.LEFT, KC.DOWN, KC.RGHT, xxxxxxx,
        xxxxxxx, xxxxxxx, xxxxxxx, KC.CW,   xxxxxxx,    KC.HOME, LC_LEFT, xxxxxxx, LC_RGHT, KC.END,
                          _______, _______, _______,    _______, _______, _______
    ],
    # symbols
    [
        KC.AT,   KC.EXLM, KC.LABK, KC.RABK, KC.BSLS,    KC.SCLN, KC.AMPR, KC.PIPE, KC.DLR,  KC.CIRC,
        KC.LBRC, KC.RBRC, KC.LCBR, KC.RCBR, KC.EQL,     KC.HASH, KC.LPRN, KC.RPRN, KC.TILD, KC.GRAVE,
        KC.SLSH, KC.ASTR, KC.PLUS, KC.MINS, KC.COLN,    KC.PERC, KC.UNDS, KC.COMM, KC.DOT,  KC.SLSH,
                          _______, _______, _______,    _______, _______, _______
    ],
    # numbers
    [
        xxxxxxx, KC.HASH, KC.DLR,  xxxxxxx, xxxxxxx,    KC.MINS, KC.N7,   KC.N8,   KC.N9,   KC.SLSH,
        KC.LGUI, KC.LALT, KC.LCTL, KC.LSFT, KC.TG(3),   KC.PLUS, KC.N4,   KC.N5,   KC.N6,   KC.ASTR,
        xxxxxxx, KC.LPRN, KC.RPRN, KC.DOT,  KC.COMM,    KC.N0,   KC.N1,   KC.N2,   KC.N3,   KC.DOT,
                          _______, _______, _______,    KC.UNDS, _______, KC.EQL
    ],
    # function keys
    [
        KC.F9,   KC.F10,  KC.F11,  KC.F12,  xxxxxxx,    xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx,
        KC.F5,   KC.F6,   KC.F7,   KC.F8,   xxxxxxx,    xxxxxxx, KC.LSFT, KC.LCTL, KC.LALT, KC.LGUI,
        KC.F1,   KC.F2,   KC.F3,   KC.F4,   xxxxxxx,    xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx,
                          _______, _______, _______,    _______, _______, _______
    ],
]

if __name__ == '__main__':
    keyboard.go()
