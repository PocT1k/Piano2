# UTF-8 Будет здесь!
import pygame
import pygame.midi
import time

from config import ColorRGB, Sizes, Variables, Change


class Key:
    def __init__(self, COLLISION_RECT, DRAW_RECT, number, shiftTone):
        self.COLLISION_RECT = COLLISION_RECT
        self.DRAW_RECT = DRAW_RECT

        self.BORDER_RADIUS_FALL = int(COLLISION_RECT.width * 0.2)

        self.FALL_SEP = int(COLLISION_RECT.width * 0.1)
        self.FALL_L = self.COLLISION_RECT.left + self.FALL_SEP
        self.FALL_W = self.COLLISION_RECT.width - 2 * self.FALL_SEP

        self.number = number
        self.tone = number + shiftTone
        try:
            self.keyboardKey = Variables.KEYS_PIANO[number]
        except IndexError:
            self.keyboardKey = None
        # print(self.keyboardKey)

        self.falls = []  # Массив падающих прямоугольников для ноты
        self.numOctave = self.tone // 12 + 1

        # Key
        self.strKey = Variables.KEYS_NAMES[self.keyboardKey]
        self.sizeFontKey = int(self.DRAW_RECT.width / 2)
        self.fontKey = pygame.font.SysFont("Verdana", self.sizeFontKey)
        # Octave
        self.strOctave = 'C' + str(self.numOctave) if self.tone % 12 == 0 else None
pass  # class Key


class WhiteKey(Key):
    def __init__(self, COLLISION_RECT, DRAW_RECT, number, shiftTone):
        Key.__init__(self, COLLISION_RECT, DRAW_RECT, number, shiftTone)

        # Note font and text
        self.strName = Change.namesNotes[Variables.NAME_NOTE][self.tone % 12]
        self.sizeFontName = int(self.DRAW_RECT.width / (1.8 * min(2, len(self.strName))))
        self.fontName = pygame.font.SysFont("Verdana", self.sizeFontName)
        self.textName = self.fontName.render(self.strName, True, ColorRGB.ALMOST_BLACK)
        # Name Rect
        self.NAME_RECT = pygame.Rect(0, 0, COLLISION_RECT.width * 0.65, COLLISION_RECT.width * 0.6)
        self.NAME_RECT.centerx = self.COLLISION_RECT.centerx  # x
        self.NAME_TEXT_RECT = self.textName.get_rect()
        self.NAME_TEXT_RECT.centerx = self.NAME_RECT.centerx  # x
        self.NAME_RECT.centery = self.COLLISION_RECT.centery + self.COLLISION_RECT.height * 0.26  # y
        self.NAME_TEXT_RECT.bottom = self.NAME_RECT.bottom + self.NAME_RECT.height * 0.03  # y
        self.BORDER_RADIUS_NAME = int(COLLISION_RECT.width * 0.1)
        self.BORDER_RADIUS_NOTE = int(COLLISION_RECT.width * 0.1)

        # Key
        self.textKey = self.fontKey.render(self.strKey, True, ColorRGB.ALMOST_BLACK)
        # Octave
        if self.strOctave:
            self.sizeFontOctave = int(self.DRAW_RECT.width / 2)
            self.fontOctave = pygame.font.SysFont("Verdana", self.sizeFontOctave)
            self.textOctave = self.fontOctave.render(self.strOctave, True, ColorRGB.TEXT_OCTAVE)
    pass  # __init__
pass  # class WhiteKey


class BlackKey(Key):
    def __init__(self, COLLISION_RECT, DRAW_RECT, number, shiftTone):

        width = COLLISION_RECT.width
        match (number + shiftTone) % 12:
            case 1:
                COLLISION_RECT.x -= width * 0.15
                DRAW_RECT.x -= width * 0.15
            case 3:
                COLLISION_RECT.x += width * 0.15
                DRAW_RECT.x += width * 0.15
            case 6:
                COLLISION_RECT.x -= width * 0.25
                DRAW_RECT.x -= width * 0.25
            case 8:
                pass
            case 10:
                COLLISION_RECT.x += width * 0.25
                DRAW_RECT.x += width * 0.25
            case _:
                print(f'ЧЗХ_2, тут не тот параметр: {(number + shiftTone) % 12}')
                exit(0)
        Key.__init__(self, COLLISION_RECT, DRAW_RECT, number, shiftTone)

        # Note font and text
        self.strName = Change.namesNotes[Variables.NAME_NOTE][self.tone % 12]
        self.sizeFontName = int(self.DRAW_RECT.width / 2.2)
        self.fontName = pygame.font.SysFont("Verdana", self.sizeFontName)
        self.textName = self.fontName.render(self.strName, True, ColorRGB.ALMOST_BLACK)
        # Name Rect
        self.NAME_RECT = pygame.Rect(0, 0, COLLISION_RECT.width * 0.65, COLLISION_RECT.width * 0.6)
        self.NAME_RECT.centerx = self.COLLISION_RECT.centerx  # x
        self.NAME_TEXT_RECT = self.textName.get_rect()
        self.NAME_TEXT_RECT.centerx = self.NAME_RECT.centerx  # x
        self.NAME_RECT.centery = self.COLLISION_RECT.centery + self.COLLISION_RECT.height * 0.2  # y
        self.NAME_TEXT_RECT.bottom = self.NAME_RECT.bottom - self.NAME_RECT.height * 0.03  # y
        self.BORDER_RADIUS_NAME = int(COLLISION_RECT.width * 0.1)
        self.BORDER_RADIUS_NOTE = int(COLLISION_RECT.width * 0.07)

        # Key
        self.textKey = self.fontKey.render(self.strKey, True, ColorRGB.KEY_UP_WHITE)
pass  # class BlackKey


class Keyboard:
    # Configuration
    HEIGHT = 0.25
    KEY_SEP_VERTICAL = 0.065
    KEY_SEP_HORIZONTAL = 0.05
    KEY_BLACK_COLLISION_WIDTH = 0.65
    KEY_BLACK_COLLISION_HEIGHT = 0.7
    RECT = pygame.Rect(0, 0, 0, 0)

    volume = Variables.START_VOLUME
    instrument = Variables.MIDI_INSTRUMENT
    isMouseDown = False
    plaingNotes = set()
    blackKeys = []
    whiteKeys = []


    def __init__(self, screen, scaleW, scaleH):
        self.screen = screen
        self.scaleW, self.scaleH = scaleW, scaleH
        self.scaleM = (self.scaleW + self.scaleH) / 2

        pygame.font.init()
        pygame.midi.init()
        self.turntable = pygame.midi.Output(0)
        self.turntable.set_instrument(self.instrument)

        self.calcCountKeys()
        self.isWhiteKeys = [[False, False] for _ in range(Variables.COUNT_WHITE_KEYS)]
        self.isBlackKeys = [[False, False] for _ in range(Variables.COUNT_BLACK_KEYS)]
        self.timeChangesSettings = 0

        self.init()
    pass  # __init__


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

        Variables.MIDI_TONE = (Variables.OCTAVE - 1) * 12 - self.countWhiteLeft - Change.countBlackKeysL[self.countWhiteLeft]
        # print(Variables.MIDI_TONE)
    pass  # calcCountKeys


    def calcCountLinesAndHud(self):
        intervalLines = 1
        quanLines = self.timeDelFall
        while quanLines > 4 or quanLines < 2:
            if quanLines > 4:
                quanLines /= 2
                intervalLines *= 2
            else:  # quanLines < 2
                quanLines *= 2
                intervalLines /= 2

        self.QUAN_LINES = int(self.timeDelFall // intervalLines) + 1
        self.INTERVAL_LINES = intervalLines

        self.TEXT_LINES = []
        fontLine = pygame.font.SysFont("Verdana", max(16, int(16 * self.scaleM)))
        for i in range(1, self.QUAN_LINES):
            self.TEXT_LINES.append(fontLine.render(f'{i * self.INTERVAL_LINES}s', True, ColorRGB.SCENE_LINES))

        self.WIDTH_LINES_VRT1 = int(max(1, 4 * self.scaleH))
        self.WIDTH_LINES_VRT2 = int(max(1, 4 * self.scaleH))
        self.WIDTH_LINES_HRZ = int(max(1, 2 * self.scaleW))

        self.fontHud = pygame.font.SysFont("Arial", max(16, int(64 * self.scaleM)))

    pass  # calcCountLines


    def initKeys(self):
        shiftTone = Variables.MIDI_TONE
        number = 0
        noteInOctave = self.countWhiteLeft

        self.overlayWhite = pygame.Surface((self.KEY_WHITE_COLLISION_WIDTH - 2 * self.KEY_SEP_VERTICAL,
            self.KEY_WHITE_COLLISION_HEIGHT - 2 * self.KEY_SEP_HORIZONTAL), pygame.SRCALPHA)
        self.overlayWhite.fill((*ColorRGB.KEY_DOWN_WHITE, 127))
        self.overlayBlack = pygame.Surface((self.KEY_BLACK_COLLISION_WIDTH - 2 * self.KEY_SEP_VERTICAL,
            self.KEY_BLACK_COLLISION_HEIGHT - 2 * self.KEY_SEP_HORIZONTAL), pygame.SRCALPHA)
        self.overlayBlack.fill((*ColorRGB.KEY_DOWN_BLACK, 127))

        for i in range(Variables.COUNT_WHITE_KEYS):
            whiteKey = WhiteKey(
                pygame.Rect(self.RECT.x + i * self.KEY_WHITE_COLLISION_WIDTH,
                    self.RECT.y,
                    self.KEY_WHITE_COLLISION_WIDTH,
                    self.KEY_WHITE_COLLISION_HEIGHT),
                pygame.Rect(self.RECT.x + i * self.KEY_WHITE_COLLISION_WIDTH + self.KEY_SEP_VERTICAL,
                    self.RECT.y + self.KEY_SEP_HORIZONTAL,
                    self.KEY_WHITE_COLLISION_WIDTH - 2 * self.KEY_SEP_VERTICAL,
                    self.KEY_WHITE_COLLISION_HEIGHT - 2 * self.KEY_SEP_HORIZONTAL),
                number, shiftTone)
            self.whiteKeys.append(whiteKey)

            if Change.addToneAndBlack[noteInOctave]:
                if i + 1 == Variables.COUNT_WHITE_KEYS:
                    break
                number += 1

                blackKey = BlackKey(
                    pygame.Rect(self.RECT.x + (i + 1) * self.KEY_WHITE_COLLISION_WIDTH - self.KEY_BLACK_COLLISION_WIDTH / 2,
                        self.RECT.y,
                        self.KEY_BLACK_COLLISION_WIDTH,
                        self.KEY_BLACK_COLLISION_HEIGHT),
                    pygame.Rect(self.RECT.x + (i + 1) * self.KEY_WHITE_COLLISION_WIDTH - self.KEY_BLACK_COLLISION_WIDTH / 2 + self.KEY_SEP_VERTICAL,
                        self.RECT.y + self.KEY_SEP_HORIZONTAL,
                        self.KEY_BLACK_COLLISION_WIDTH - 2 * self.KEY_SEP_VERTICAL,
                        self.KEY_BLACK_COLLISION_HEIGHT - 2 * self.KEY_SEP_HORIZONTAL),
                number, shiftTone)
                self.blackKeys.append(blackKey)

            noteInOctave = (noteInOctave + 1) % 7
            number += 1
    pass  # initWhiteKeys


    def init(self):
        # self.HEIGHT = self.HEIGHT * Sizes.SCREEN_HEIGHT
        self.RECT = pygame.Rect(0, Sizes.SCREEN_HEIGHT * (1 - self.HEIGHT), Sizes.SCREEN_WIDTH, self.HEIGHT * Sizes.SCREEN_HEIGHT)
        self.speedFall = Variables.SPEED_FALL * self.scaleH
        self.timeDelFall = self.RECT.top / self.speedFall
        self.timeDelFallAdd = (self.RECT.top * 1.1) / (self.speedFall / 1.1)

        self.KEY_WHITE_COLLISION_WIDTH = Sizes.SCREEN_WIDTH / Variables.COUNT_WHITE_KEYS
        self.KEY_WHITE_COLLISION_HEIGHT = self.RECT.height

        self.KEY_BLACK_COLLISION_WIDTH *= self.KEY_WHITE_COLLISION_WIDTH
        self.KEY_BLACK_COLLISION_HEIGHT *= self.KEY_WHITE_COLLISION_HEIGHT

        self.KEY_SEP_VERTICAL *= self.KEY_WHITE_COLLISION_WIDTH / 2
        self.KEY_SEP_HORIZONTAL *= self.RECT.height / 2

        self.initKeys()
        self.calcCountLinesAndHud()
    pass  # calc


    def procNotes(self):
        for i in range(Variables.COUNT_WHITE_KEYS):
            tone = self.whiteKeys[i].tone

            if (self.isWhiteKeys[i][0] or self.isWhiteKeys[i][1]):
                if not (tone in self.plaingNotes):
                    self.plaingNotes.add(tone)
                    self.turntable.note_on(tone, self.volume)
                    self.whiteKeys[i].falls.append({'start': time.time(), 'end': None})
            else:
                if (tone in self.plaingNotes):
                    self.plaingNotes.remove(tone)
                    self.turntable.note_off(tone, self.volume)
                    self.whiteKeys[i].falls[-1]['end'] = time.time()

        for i in range(Variables.COUNT_BLACK_KEYS):
            tone = self.blackKeys[i].tone

            if (self.isBlackKeys[i][0] or self.isBlackKeys[i][1]):
                if not (tone in self.plaingNotes):
                    self.plaingNotes.add(tone)
                    self.turntable.note_on(tone, self.volume)
                    self.blackKeys[i].falls.append({'start': time.time(), 'end': None})
            else:
                if (tone in self.plaingNotes):
                    self.plaingNotes.remove(tone)
                    self.turntable.note_off(tone, self.volume)
                    self.blackKeys[i].falls[-1]['end'] = time.time()
    pass  # playNotes


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
    pass  # procMouse


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

        if keys[pygame.K_UP]:
            self.timeChangesSettings = time.time()
            if self.volume < 127:
                self.volume += 1
            else:
                self.volume = 127
            self.generTextHudInstrumentAndVolume()

        elif keys[pygame.K_DOWN]:
            self.timeChangesSettings = time.time()
            if self.volume > 0:
                self.volume -= 1
            else:
                self.volume = 0
            self.generTextHudInstrumentAndVolume()

        elif keys[pygame.K_RIGHT]:
            self.timeChangesSettings = time.time()
            self.instrument = (self.instrument + 1) % 128
            self.turntable.set_instrument(self.instrument)
            self.generTextHudInstrumentAndVolume()

        elif keys[pygame.K_LEFT]:
            self.timeChangesSettings = time.time()
            self.instrument = (self.instrument - 1) % 128
            self.turntable.set_instrument(self.instrument)
            self.generTextHudInstrumentAndVolume()

    pass  # procKeyboard


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
    pass  # procEvents


    def drawFall(self, currentTime, keys, RGB_GREEN):
        for note in keys:
            # Некоторые атрибуты для ноты, которые рисуются заранее
            if note.strOctave:
                self.screen.blit(note.textOctave, (note.DRAW_RECT.left + note.sizeFontOctave * 0.1, note.COLLISION_RECT.top - note.sizeFontOctave * 1.1))

            # Её падающие прямоугльники
            for fall in note.falls:
                if fall['end']:
                    if fall['end'] + self.timeDelFallAdd < currentTime:  # Удаление
                        note.falls.remove(fall)
                        continue

                # Позиции
                y = (fall['start'] - currentTime) * self.speedFall + self.RECT.top
                h = ((fall['end'] if fall['end'] else currentTime) - fall['start']) * self.speedFall + 10 * self.scaleH
                # Окантовка
                overlayFall = pygame.Surface((note.COLLISION_RECT.width, h + 2 * note.FALL_SEP), pygame.SRCALPHA)
                pygame.draw.rect(overlayFall, (*ColorRGB.TRIM_FALL, 223),
                    pygame.Rect(0, 0, note.COLLISION_RECT.width, h + 2 * note.FALL_SEP),
                    border_radius=note.BORDER_RADIUS_FALL)
                self.screen.blit(overlayFall, (note.COLLISION_RECT.left, y - note.FALL_SEP))
                # Прямоугольник
                pygame.draw.rect(self.screen, RGB_GREEN, pygame.Rect(note.FALL_L, y, note.FALL_W, h), border_radius = note.BORDER_RADIUS_FALL)
    pass  # drawFall


    def drawNote(self, keys, isKeys, overlayNote, RGB_UP):
        for i, note in enumerate(keys):
            # Сама нота
            pygame.draw.rect(self.screen, RGB_UP, note.DRAW_RECT, border_radius = note.BORDER_RADIUS_NOTE)
            # Её название
            if note.strName:
                pygame.draw.rect(self.screen, ColorRGB.OCTAVES[note.numOctave], note.NAME_RECT, border_radius = note.BORDER_RADIUS_NAME)
                self.screen.blit(note.textName, note.NAME_TEXT_RECT)
            # Её клавиша
            # if note.textKey:
            self.screen.blit(note.textKey, (note.DRAW_RECT.left + 5 * self.scaleW,
                note.COLLISION_RECT.bottom - note.sizeFontKey - 17 * self.scaleH))
            # Нажатие
            if (isKeys[i][0] or isKeys[i][1]):
                self.screen.blit(overlayNote, (note.DRAW_RECT.x, note.DRAW_RECT.y))
    pass  # drawNote


    def drawLines(self):
        # Вертикальные
        for i, note in enumerate(self.whiteKeys):
            if note.number % 12 == 0:
                pygame.draw.line(self.screen, ColorRGB.SCENE_LINES,
                    (note.COLLISION_RECT.left, note.COLLISION_RECT.top),
                    (note.COLLISION_RECT.left, note.COLLISION_RECT.top - self.RECT.top),
                    width = self.WIDTH_LINES_VRT1)
            if note.number % 12 == 11:
                pygame.draw.line(self.screen, ColorRGB.SCENE_LINES,
                    (note.COLLISION_RECT.right, note.COLLISION_RECT.top),
                    (note.COLLISION_RECT.right, note.COLLISION_RECT.top - self.RECT.top),
                    width = self.WIDTH_LINES_VRT2)

        # Горизонтальные
        for i in range (1, self.QUAN_LINES):
            y = self.RECT.top - i * self.speedFall
            if y < 0: # Если рисуем за экраном
                break

            pygame.draw.line(self.screen, ColorRGB.SCENE_LINES,
                (self.RECT.left, y),
                (self.RECT.right, self.RECT.top - i * self.speedFall * self.INTERVAL_LINES),
                width = self.WIDTH_LINES_HRZ)
            self.screen.blit(self.TEXT_LINES[i - 1], (self.RECT.left + 5 * self.scaleW, y))

    pass  # drawLines


    def generTextHudInstrumentAndVolume(self):
        self.textInstrument = self.fontHud.render(f'Instrument: {self.instrument}   ' +
            f'{Variables.MIDI_INSTRUMENTS[self.instrument]}', True, ColorRGB.WHITE)
        self.textVolume = self.fontHud.render(f'Volume: {self.volume}', True, ColorRGB.WHITE)
    pass  # generHudInstrumentAndVolume


    def drawHud(self, currentTime):
        if currentTime < self.timeChangesSettings + 5:
            self.screen.blit(self.textInstrument, (10 * self.scaleW, 10 * self.scaleH))
            self.screen.blit(self.textVolume, (10 * self.scaleW, 96 * self.scaleH))
    pass  # drawHud


    def draw(self):
        currentTime = time.time()
        self.drawLines()

        self.drawFall(currentTime, self.whiteKeys, ColorRGB.FALL_GREEN_WHITE)
        self.drawFall(currentTime, self.blackKeys, ColorRGB.FALL_GREEN_BLACK)

        pygame.draw.rect(self.screen, ColorRGB.KEYBOARD_BG, self.RECT)
        self.drawNote(self.whiteKeys, self.isWhiteKeys, self.overlayWhite, ColorRGB.KEY_UP_WHITE)
        self.drawNote(self.blackKeys, self.isBlackKeys, self.overlayBlack, ColorRGB.KEY_UP_BLACK)

        self.drawHud(currentTime)
    pass  # draw

pass  # class Keyboard
