# UTF-8 Будет здесь!
import pygame
import pygame.midi

from config import ColorRGB
from config import Sizes
from config import Variables
from config import Change


class Key:
    def __init__(self, COLLISION_RECT, DRAW_RECT):
        self.COLLISION_RECT = COLLISION_RECT
        self.DRAW_RECT = DRAW_RECT

    def setTone(self, tone):
        self.tone = tone
        self.octave = ''
pass # class Key

class WhiteKey(Key):
    def __init__(self, COLLISION_RECT, DRAW_RECT):
        Key.__init__(self, COLLISION_RECT, DRAW_RECT)
pass # class WhiteKey

class BlackKey(Key):
    def __init__(self, COLLISION_RECT, DRAW_RECT):
        Key.__init__(self, COLLISION_RECT, DRAW_RECT)
pass # class BlackKey


class Keyboard:
    BG = ColorRGB.KEYBOARD_BG
    SCENE_BG = ColorRGB.BG
    KEY_UP_WHITE = ColorRGB.KEY_UP_WHITE
    KEY_DOWN_WHITE = ColorRGB.KEY_DOWN_WHITE
    KEY_UP_BLACK = ColorRGB.KEY_UP_BLACK
    KEY_DOWN_BLACK = ColorRGB.KEY_DOWN_BLACK

    HEIGHT = 0.25
    KEY_SEP_VERTICAL = 0.065
    KEY_SEP_HORIZONTAL = 0.05
    KEY_BLACK_COLLISION_WIDTH = 0.65
    KEY_BLACK_COLLISION_HEIGHT = 0.6
    RECT = pygame.Rect(0, 0, 0, 0)

    isMouseDown = False
    plaingNotes = set()
    blackKeys = []
    whiteKeys = []

    def __init__(self, screen):
        pygame.midi.init()
        self.turntable = pygame.midi.Output(0)
        self.turntable.set_instrument(Variables.MIDI_INSTRUMENT)
        self.screen = screen

        self.calcCountKeys()
        self.isWhiteKeys = [[False, False] for _ in range(Variables.COUNT_WHITE_KEYS)]
        self.isBlackKeys = [[False, False] for _ in range(Variables.COUNT_BLACK_KEYS)]
        self.init()
    pass # __init__

    def calcCountKeys(self):
        self.countWhiteLeft = 7 - Variables.COUNT_WHITE_KEYS_IDENT
        if self.countWhiteLeft == 7:
            self.countWhiteLeft = 0
        self.countWhiteMiddle = (Variables.COUNT_WHITE_KEYS - self.countWhiteLeft) // 7
        self.countWhiteRight = (Variables.COUNT_WHITE_KEYS - self.countWhiteLeft) % 7
        if self.countWhiteLeft >= Variables.COUNT_WHITE_KEYS:
            self.countWhiteLeft = Variables.COUNT_WHITE_KEYS
            self.countWhiteMiddle, self.countWhiteRight = 0, 0
        # print(self.countWhiteLeft, self.countWhiteMiddle, self.countWhiteRight)

        Variables.COUNT_BLACK_KEYS = Change.countBlackKeysL[self.countWhiteLeft] + self.countWhiteMiddle * 5 + Change.countBlackKeysR[self.countWhiteRight]
        # print(Variables.COUNT_BLACK_KEYS)

        Variables.MIDI_TONE = Variables.OCTAVE * 12 - self.countWhiteLeft - Change.countBlackKeysL[self.countWhiteLeft]
        # print(Variables.MIDI_TONE)
    pass # calcCountKeys

    def initKeys(self):
        tone = Variables.MIDI_TONE
        noteInOctave = self.countWhiteLeft

        ib = 0
        for iw in range(Variables.COUNT_WHITE_KEYS):
            self.whiteKeys.append(WhiteKey(
                pygame.Rect(self.RECT.x + iw * self.KEY_WHITE_COLLISION_WIDTH, self.RECT.y + 0,
                            self.KEY_WHITE_COLLISION_WIDTH, self.KEY_WHITE_COLLISION_HEIGHT),
                pygame.Rect(self.RECT.x + iw * self.KEY_WHITE_COLLISION_WIDTH + self.KEY_SEP_VERTICAL, self.RECT.y + self.KEY_SEP_HORIZONTAL,
                            self.KEY_WHITE_COLLISION_WIDTH - 2 * self.KEY_SEP_VERTICAL, self.KEY_WHITE_COLLISION_HEIGHT - 2 * self.KEY_SEP_HORIZONTAL) ))
            self.whiteKeys[iw].setTone(tone)

            if Change.addTone[noteInOctave]:
                if iw + 1 == Variables.COUNT_WHITE_KEYS:
                    break
                tone += 1
                self.blackKeys.append(BlackKey(
                    pygame.Rect(self.RECT.x + (iw + 1) * self.KEY_WHITE_COLLISION_WIDTH - self.KEY_BLACK_COLLISION_WIDTH / 2, self.RECT.y + 0,
                                self.KEY_BLACK_COLLISION_WIDTH, self.KEY_BLACK_COLLISION_HEIGHT),
                    pygame.Rect(self.RECT.x + (iw + 1) * self.KEY_WHITE_COLLISION_WIDTH - self.KEY_BLACK_COLLISION_WIDTH / 2 + self.KEY_SEP_VERTICAL, self.RECT.y + self.KEY_SEP_HORIZONTAL,
                                self.KEY_BLACK_COLLISION_WIDTH - 2 * self.KEY_SEP_VERTICAL, self.KEY_BLACK_COLLISION_HEIGHT - 2 * self.KEY_SEP_HORIZONTAL) ))
                self.blackKeys[ib].setTone(tone)
                ib += 1

            noteInOctave = (noteInOctave + 1) % 7
            tone += 1
    pass # initWhiteKeys

    def init(self):
        self.HEIGHT *= Sizes.SCREEN_HEIGHT
        self.RECT = pygame.Rect(0, Sizes.SCREEN_HEIGHT - self.HEIGHT, Sizes.SCREEN_WIDTH, self.HEIGHT)

        self.KEY_WHITE_COLLISION_WIDTH = Sizes.SCREEN_WIDTH / Variables.COUNT_WHITE_KEYS
        self.KEY_WHITE_COLLISION_HEIGHT = self.HEIGHT

        self.KEY_BLACK_COLLISION_WIDTH *= self.KEY_WHITE_COLLISION_WIDTH
        self.KEY_BLACK_COLLISION_HEIGHT *= self.KEY_WHITE_COLLISION_HEIGHT

        self.KEY_SEP_VERTICAL *= self.KEY_WHITE_COLLISION_WIDTH / 2
        self.KEY_SEP_HORIZONTAL *= self.HEIGHT / 2

        self.initKeys()
    pass # calc

    def procNotes(self):
        for i in range(Variables.COUNT_BLACK_KEYS):
            tone = self.blackKeys[i].tone

            if (self.isBlackKeys[i][0] or self.isBlackKeys[i][1]):
                if not (tone in self.plaingNotes):
                    self.plaingNotes.add(tone)
                    self.turntable.note_on(tone, 127)
            else: # not (self.isBlackKeys[i][0] or self.isBlackKeys[i][1])
                if (tone in self.plaingNotes):
                    self.plaingNotes.remove(tone)
                    self.turntable.note_off(tone, 127)

        for i in range(Variables.COUNT_WHITE_KEYS):
            tone = self.whiteKeys[i].tone

            if (self.isWhiteKeys[i][0] or self.isWhiteKeys[i][1]):
                if not (tone in self.plaingNotes):
                    self.plaingNotes.add(tone)
                    self.turntable.note_on(tone, 127)
            else: # not (self.isWhiteKeys[i][0] or self.isWhiteKeys[i][1])
                if (tone in self.plaingNotes):
                    self.plaingNotes.remove(tone)
                    self.turntable.note_off(tone, 127)
    pass # playNotes

    def procMouse(self, msg):
        if msg == 'up':
            self.isMouseDown = False
            for i in range(Variables.COUNT_WHITE_KEYS): self.isWhiteKeys[i][0] = False
            for i in range(Variables.COUNT_BLACK_KEYS): self.isBlackKeys[i][0] = False
            return
        elif msg == 'down':
            self.isMouseDown = True
        elif msg == 'motion':
            pass
        else:
            print('ЧЗХ, тут не тот параметр')
            exit(0)

        if (not self.isMouseDown):
            return

        cX, cY = pygame.mouse.get_pos()
        if (not self.RECT.collidepoint(cX, cY)): # Если не коллайдер клавиш
            for i in range(Variables.COUNT_WHITE_KEYS): self.isWhiteKeys[i][0] = False
            for i in range(Variables.COUNT_BLACK_KEYS): self.isBlackKeys[i][0] = False
            return

        isBlack = False
        for i in range(Variables.COUNT_BLACK_KEYS):
            if (self.blackKeys[i].COLLISION_RECT.collidepoint(cX, cY)):
                if (self.isMouseDown):
                    self.isBlackKeys[i][0] = True
                    isBlack = True
                    continue
            self.isBlackKeys[i][0] = False

        if isBlack:
            for i in range(Variables.COUNT_WHITE_KEYS): self.isWhiteKeys[i][0] = False
            return

        for i in range(Variables.COUNT_WHITE_KEYS):
            if (self.whiteKeys[i].COLLISION_RECT.collidepoint(cX, cY)):
                if (self.isMouseDown):
                    self.isWhiteKeys[i][0] = True
                    continue
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
            if (self.isWhiteKeys[i][0] or self.isWhiteKeys[i][1]):
                pygame.draw.rect(self.screen, self.KEY_DOWN_WHITE, self.whiteKeys[i].DRAW_RECT)
            else:
                pygame.draw.rect(self.screen, self.KEY_UP_WHITE, self.whiteKeys[i].DRAW_RECT)

        for i in range(Variables.COUNT_BLACK_KEYS):
            if (self.isBlackKeys[i][0] or self.isBlackKeys[i][1]):
                pygame.draw.rect(self.screen, self.KEY_DOWN_BLACK, self.blackKeys[i].DRAW_RECT)
            else:
                pygame.draw.rect(self.screen, self.KEY_UP_BLACK, self.blackKeys[i].DRAW_RECT)
    pass # draw

pass # class Keyboard
