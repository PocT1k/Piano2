# UTF-8 Будет здесь!
import pygame

from config import ColorRGB
from config import Variables


class WhiteKey:
    def __init__(self, COLLISION_RECT, DRAW_RECT):
        self.COLLISION_RECT = COLLISION_RECT
        self.DRAW_RECT = DRAW_RECT

class BlackKey:
    pass


class Keyboard:
    isMouseDown = False

    BG = ColorRGB.KEYBOARD_BG
    SCENE_BG = ColorRGB.BG
    KEY_UP_WHITE = ColorRGB.KEY_UP_WHITE
    KEY_DOWN_WHITE = ColorRGB.KEY_DOWN_WHITE

    HEIGHT = 0.25
    KEY_WIDTH = 0.0
    KEY_HEIGHT = 0.0
    KEY_SEP = 0.05
    RECT = pygame.Rect(0, 0, 0, 0)

    whiteKeys = []
    isWhiteKeys = [0] * Variables.COUNT_WHITE_KEYS
