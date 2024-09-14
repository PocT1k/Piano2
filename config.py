# UTF-8 Будет здесь!
import pygame


class ColorRGB:
    BG = (200, 230, 255)
    KEYBOARD_BG = (0, 0, 0)
    KEY_UP_WHITE = (255, 255, 255)
    KEY_DOWN_WHITE = (175, 175, 175)
    KEY_UP_BLACK = (15, 15, 15)
    # KEY_DOWN_BLACK = (63, 63, 63)
    KEY_DOWN_BLACK = (143, 143, 143)

class Sizes:
    SCREEN_WIDTH, SCREEN_HEIGHT = 500, 300
    # SCREEN_WIDTH, SCREEN_HEIGHT = 0, 0

class Variables:
    COUNT_WHITE_KEYS = 28
    COUNT_WHITE_KEYS_IDENT = 0
    OCTAVE = 3
    MIDI_TONE = 0
    MIDI_INSTRUMENT = 2

    # not init
    COUNT_BLACK_KEYS = 0

class Change:
    countBlackKeysL = [0, 0, 1, 2, 3, 3, 4, 5]
    countBlackKeysR = [0, 0, 1, 2, 2, 3, 4, 5]
    addToneOrBlack = [1, 1, 0, 1, 1, 1, 0]

