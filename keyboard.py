# UTF-8 Будет здесь!
import pygame
import pygame.midi

from config import ColorRGB
from config import Sizes
from config import Variables


class WhiteKey:
    def __init__(self, COLLISION_RECT, DRAW_RECT):
        self.COLLISION_RECT = COLLISION_RECT
        self.DRAW_RECT = DRAW_RECT

class BlackKey:
    pass


class Keyboard:
    BG = ColorRGB.KEYBOARD_BG
    SCENE_BG = ColorRGB.BG
    KEY_UP_WHITE = ColorRGB.KEY_UP_WHITE
    KEY_DOWN_WHITE = ColorRGB.KEY_DOWN_WHITE

    HEIGHT = 0.25
    KEY_WIDTH = 0.0
    KEY_HEIGHT = 0.0
    KEY_SEP = 0.065
    RECT = pygame.Rect(0, 0, 0, 0)

    isMouseDown = False
    whiteKeys = []
    isWhiteKeys = [[False, False]] * Variables.COUNT_WHITE_KEYS

    def __init__(self, scene):
        #midi
        pygame.midi.init()
        turntable = pygame.midi.Output(0)
        turntable.set_instrument(Variables.MIDI_INSTRUMENT)

        Keyboard.scene = scene
    pass

    def calc(self):
        Keyboard.HEIGHT *= Sizes.SCREEN_HEIGHT
        Keyboard.RECT = pygame.Rect(0, Sizes.SCREEN_HEIGHT - Keyboard.HEIGHT, Sizes.SCREEN_WIDTH, Keyboard.HEIGHT)

        Keyboard.KEY_COLLISION_WIDTH = Sizes.SCREEN_WIDTH / Variables.COUNT_WHITE_KEYS
        Keyboard.KEY_SEP *= Keyboard.KEY_COLLISION_WIDTH / 2
        Keyboard.KEY_WIDTH = Keyboard.KEY_COLLISION_WIDTH - 2 * Keyboard.KEY_SEP
        Keyboard.KEY_HEIGHT = Keyboard.HEIGHT - 2 * Keyboard.KEY_SEP

        whiteKeys = Keyboard.whiteKeys
        for i in range(Variables.COUNT_WHITE_KEYS):
            whiteKeys.append(WhiteKey(
                pygame.Rect(i * Keyboard.KEY_COLLISION_WIDTH, Keyboard.RECT.y, Keyboard.KEY_COLLISION_WIDTH,
                            Keyboard.RECT.height),
                pygame.Rect(i * Keyboard.KEY_COLLISION_WIDTH + Keyboard.KEY_SEP, Keyboard.RECT.y + Keyboard.KEY_SEP,
                            Keyboard.KEY_WIDTH, Keyboard.KEY_HEIGHT)))
            whiteKeys[i].TONE = Variables.MIDI_TONE + i

    pass
pass # Keyboard