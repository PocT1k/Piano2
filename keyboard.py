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

    def setNote(self, note):
        self.note = note
pass # class WhiteKey

class BlackKey:
    pass
pass # class BlackKey


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
    plaingNotes = {}
    whiteKeys = []
    isWhiteKeys = [[False, False]] * Variables.COUNT_WHITE_KEYS

    def __init__(self, screen):
        #midi
        pygame.midi.init()
        self.turntable = pygame.midi.Output(0)
        self.turntable.set_instrument(Variables.MIDI_INSTRUMENT)

        self.screen = screen
        self.init()
    pass # __init__

    def initWhiteKeys(self):
        for i in range(Variables.COUNT_WHITE_KEYS):
            self.whiteKeys.append(WhiteKey(
                pygame.Rect(i * self.KEY_COLLISION_WIDTH, self.RECT.y, self.KEY_COLLISION_WIDTH,
                            self.RECT.height),
                pygame.Rect(i * self.KEY_COLLISION_WIDTH + self.KEY_SEP, self.RECT.y + self.KEY_SEP,
                            self.KEY_WIDTH, self.KEY_HEIGHT)))

            self.whiteKeys[i].setNote(Variables.MIDI_TONE + i)

    pass # initWhiteKeys

    def init(self):
        self.HEIGHT *= Sizes.SCREEN_HEIGHT
        self.RECT = pygame.Rect(0, Sizes.SCREEN_HEIGHT - self.HEIGHT, Sizes.SCREEN_WIDTH, self.HEIGHT)

        self.KEY_COLLISION_WIDTH = Sizes.SCREEN_WIDTH / Variables.COUNT_WHITE_KEYS
        self.KEY_SEP *= self.KEY_COLLISION_WIDTH / 2
        self.KEY_WIDTH = self.KEY_COLLISION_WIDTH - 2 * self.KEY_SEP
        self.KEY_HEIGHT = self.HEIGHT - 2 * self.KEY_SEP

        self.initWhiteKeys()
    pass # calc

    def procNotes(self):
        for i in range(Variables.COUNT_WHITE_KEYS):
            if (self.isWhiteKeys[i][0] or self.isWhiteKeys[i][1]):

                if i in self.plaingNotes:
                    pass
        if False:
            self.turntable.note_on(46, 127)
    pass # playNotes

    def procMouse(self, msg):
        if msg == 'up':
            self.isMouseDown = False
            for i in range(Variables.COUNT_WHITE_KEYS): self.isWhiteKeys[i][0] = False
            return
        if msg == 'down':
            self.isMouseDown = True
        elif msg == 'motion':
            pass
        else:
            print('ЧЗХ, тут не тот параметр')
            exit(0)
        
        cX, cY = pygame.mouse.get_pos()
        if (not self.RECT.collidepoint(cX, cY)): # Если не коллайдер клавиш
            for i in range(Variables.COUNT_WHITE_KEYS): self.isWhiteKeys[i][0] = False
            return

        for i in range(Variables.COUNT_WHITE_KEYS):
            if (self.whiteKeys[i].COLLISION_RECT.collidepoint(cX, cY)):
                self.isWhiteKeys[i][0] = True
                print(123) # TODO
            else:
                self.isWhiteKeys[i][0] = False
    pass # procMouse
    
    def procKeyboard(self):
        pass
    pass # procKeyboard

    def procEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.procMouse('down')
            elif event.type == pygame.MOUSEBUTTONUP:
                self.procMouse('up')
            elif event.type == pygame.MOUSEMOTION:
                self.procMouse('motion')
        return True
    pass # procEvents

    def draw(self):
        pygame.draw.rect(self.screen, self.BG, self.RECT)
        
        for i in range(Variables.COUNT_WHITE_KEYS):
            if (self.isWhiteKeys[i][0] or self.isWhiteKeys[i][1]): print('Ура!')
            if (self.isWhiteKeys[i][0] or self.isWhiteKeys[i][1]):
                pygame.draw.rect(self.screen, self.KEY_DOWN_WHITE, self.whiteKeys[i].DRAW_RECT)
            else:
                pygame.draw.rect(self.screen, self.KEY_UP_WHITE, self.whiteKeys[i].DRAW_RECT)
    pass # draw

pass # class Keyboard
