# UTF-8 Будет здесь!
import pygame
import pygame.midi

from config import ColorRGB, Sizes, Variables, Change


class Key:
    def __init__(self, COLLISION_RECT, DRAW_RECT, number, shiftTone):
        self.COLLISION_RECT = COLLISION_RECT
        self.DRAW_RECT = DRAW_RECT

        self.number = number
        self.tone = number + shiftTone
        try:
            self.keyboardKey = Variables.KEYS[number]
        except IndexError:
            self.keyboardKey = None
        # print(self.keyboardKey)

        self.strKey = ''
        self.strNote = ''
        self.strOctave = ''

    def setKey(self, key=''):
        self.key = key
        self.nameNote = Change.nameNotes[self.tone % 12]
        if self.tone % 12 == 0:
            self.octave = 'C' + str(self.tone // 12)
        else:
            self.octave = ''
pass # class Key

class WhiteKey(Key):
    def __init__(self, COLLISION_RECT, DRAW_RECT, number, shiftTone):
        Key.__init__(self, COLLISION_RECT, DRAW_RECT, number, shiftTone)
pass # class WhiteKey

class BlackKey(Key):
    def __init__(self, COLLISION_RECT, DRAW_RECT, number, shiftTone):
        Key.__init__(self, COLLISION_RECT, DRAW_RECT, number, shiftTone)

    FONT_SIZE_KEY = 0.6

    def setShiftY(self, num, width):
        match num:
            case 0:
                self.COLLISION_RECT.x -= width * 0.15
                self.DRAW_RECT.x -= width * 0.15
            case 1:
                self.COLLISION_RECT.x += width * 0.15
                self.DRAW_RECT.x += width * 0.15
            case 3:
                self.COLLISION_RECT.x -= width * 0.25
                self.DRAW_RECT.x -= width * 0.25
            case 4:
                pass
            case 5:
                self.COLLISION_RECT.x += width * 0.25
                self.DRAW_RECT.x += width * 0.25
            case _:
                print('ЧЗХ_2, тут не тот параметр')
                exit(0)
pass # class BlackKey


class Keyboard:
    # Colors
    BG = ColorRGB.KEYBOARD_BG
    SCENE_BG = ColorRGB.BG
    KEY_UP_WHITE = ColorRGB.KEY_UP_WHITE
    KEY_DOWN_WHITE = ColorRGB.KEY_DOWN_WHITE
    KEY_UP_BLACK = ColorRGB.KEY_UP_BLACK
    KEY_DOWN_BLACK = ColorRGB.KEY_DOWN_BLACK

    # Configuration
    HEIGHT = 0.25
    KEY_SEP_VERTICAL = 0.065
    KEY_SEP_HORIZONTAL = 0.05
    KEY_BLACK_COLLISION_WIDTH = 0.65
    KEY_BLACK_COLLISION_HEIGHT = 0.7
    RECT = pygame.Rect(0, 0, 0, 0)
    FONT_BLACK_SIZE_NAME = 0.5

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

        font155 = pygame.font.Font("CodecPro-Regular.ttf", 155)
        textPoint = font155.render("+1", True, (0, 0, 0))
        #screen.blit(textPoint, (pointsStart + 25, menuHeight + widthWall + 80))

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
        shiftTone = Variables.MIDI_TONE
        number = 0
        noteInOctave = self.countWhiteLeft

        self.overlayWhite = pygame.Surface((self.KEY_WHITE_COLLISION_WIDTH - 2 * self.KEY_SEP_VERTICAL,
            self.KEY_WHITE_COLLISION_HEIGHT - 2 * self.KEY_SEP_HORIZONTAL), pygame.SRCALPHA)
        self.overlayWhite.fill((*self.KEY_DOWN_WHITE, 128))
        self.overlayBlack = pygame.Surface((self.KEY_BLACK_COLLISION_WIDTH - 2 * self.KEY_SEP_VERTICAL,
            self.KEY_BLACK_COLLISION_HEIGHT - 2 * self.KEY_SEP_HORIZONTAL), pygame.SRCALPHA)
        self.overlayBlack.fill((*self.KEY_DOWN_BLACK, 128))

        fontOctave = pygame.font.Font("BuilderMono-Regular.otf", int(self.KEY_WHITE_COLLISION_WIDTH - 2 * self.KEY_SEP_VERTICAL))
        # textOctave = fontOctave.render(self.octave, True, (0, 0, 0))
        # # screen.blit(textPoint, (pointsStart + 25, menuHeight + widthWall + 80))

        for i in range(Variables.COUNT_WHITE_KEYS):
            whiteKey = WhiteKey(
                pygame.Rect(self.RECT.x + i * self.KEY_WHITE_COLLISION_WIDTH, self.RECT.y + 0,
                            self.KEY_WHITE_COLLISION_WIDTH, self.KEY_WHITE_COLLISION_HEIGHT),
                pygame.Rect(self.RECT.x + i * self.KEY_WHITE_COLLISION_WIDTH + self.KEY_SEP_VERTICAL, self.RECT.y + self.KEY_SEP_HORIZONTAL,
                            self.KEY_WHITE_COLLISION_WIDTH - 2 * self.KEY_SEP_VERTICAL, self.KEY_WHITE_COLLISION_HEIGHT - 2 * self.KEY_SEP_HORIZONTAL),
            number, shiftTone)
            self.whiteKeys.append(whiteKey)

            if Change.addToneAndBlack[noteInOctave]:
                if i + 1 == Variables.COUNT_WHITE_KEYS:
                    break
                number += 1

                blackKey = BlackKey(
                    pygame.Rect(
                        self.RECT.x + (i + 1) * self.KEY_WHITE_COLLISION_WIDTH - self.KEY_BLACK_COLLISION_WIDTH / 2, self.RECT.y + 0,
                        self.KEY_BLACK_COLLISION_WIDTH, self.KEY_BLACK_COLLISION_HEIGHT),
                    pygame.Rect(self.RECT.x + (i + 1) * self.KEY_WHITE_COLLISION_WIDTH - self.KEY_BLACK_COLLISION_WIDTH / 2 + self.KEY_SEP_VERTICAL, self.RECT.y + self.KEY_SEP_HORIZONTAL,
                                self.KEY_BLACK_COLLISION_WIDTH - 2 * self.KEY_SEP_VERTICAL, self.KEY_BLACK_COLLISION_HEIGHT - 2 * self.KEY_SEP_HORIZONTAL),
                number, shiftTone)
                blackKey.setShiftY(noteInOctave, self.KEY_BLACK_COLLISION_WIDTH)
                self.blackKeys.append(blackKey)

            noteInOctave = (noteInOctave + 1) % 7
            number += 1
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
            else:
                if (tone in self.plaingNotes):
                    self.plaingNotes.remove(tone)
                    self.turntable.note_off(tone, 127)

        for i in range(Variables.COUNT_WHITE_KEYS):
            tone = self.whiteKeys[i].tone

            if (self.isWhiteKeys[i][0] or self.isWhiteKeys[i][1]):
                if not (tone in self.plaingNotes):
                    self.plaingNotes.add(tone)
                    self.turntable.note_on(tone, 127)
            else:
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
            print('ЧЗХ_1 , тут не тот параметр')
            exit(0)

        if not self.isMouseDown:
            return

        cX, cY = pygame.mouse.get_pos()
        if not self.RECT.collidepoint(cX, cY): # Если не коллайдер клавиш
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
    
    def procKeyboard(self): # Обработка клавиш клавиатуры
        keys = pygame.key.get_pressed()

        for i in range(Variables.COUNT_WHITE_KEYS):
            if self.whiteKeys[i].keyboardKey == None: # Выходим, если у клавиши нет кнопки
                continue

            if keys[self.whiteKeys[i].keyboardKey]: # Клавиша нажата
                self.isWhiteKeys[i][1] = True
                continue
            elif self.isWhiteKeys[i][1] == True: # Если не нажата, но числится нажатой
                self.isWhiteKeys[i][1] = False

        for i in range(Variables.COUNT_BLACK_KEYS):
            if self.blackKeys[i].keyboardKey == None: # Выходим, если у клавиши нет кнопки
                continue

            if keys[self.blackKeys[i].keyboardKey]: # Клавиша нажата
                self.isBlackKeys[i][1] = True
                continue
            elif self.isBlackKeys[i][1] == True: # Если не нажата, но числится нажатой
                self.isBlackKeys[i][1] = False

    pass # procKeyboard

    def procEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
                self.procKeyboard()
            elif event.type == pygame.KEYUP:
                self.procKeyboard()

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
            pygame.draw.rect(self.screen, self.KEY_UP_WHITE, self.whiteKeys[i].DRAW_RECT)
            # if self.whiteKeys[i].octave:
            #     print()
            if (self.isWhiteKeys[i][0] or self.isWhiteKeys[i][1]):  # Нажатие
                rect = self.whiteKeys[i].DRAW_RECT
                self.screen.blit(self.overlayWhite, (rect.x, rect.y))

        for i in range(Variables.COUNT_BLACK_KEYS):
            pygame.draw.rect(self.screen, self.KEY_UP_BLACK, self.blackKeys[i].DRAW_RECT)
            if (self.isBlackKeys[i][0] or self.isBlackKeys[i][1]):  # Нажатие
                rect = self.blackKeys[i].DRAW_RECT
                self.screen.blit(self.overlayBlack, (rect.x, rect.y))
    pass # draw

pass # class Keyboard
