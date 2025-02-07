# UTF-8 Будет здесь!
import pygame


class ColorRGB:
    WHITE = (255, 255, 255)
    ALMOST_BLACK = (15, 15, 15)
    BLACK = (0, 0, 0)

    SCENE_BG = (56, 56, 56)
    SCENE_LINES1 = (120, 120, 120)
    SCENE_LINES2 = (88, 88, 88)
    KEYBOARD_BG = BLACK
    KEY_DOWN = (127, 127, 127)
    TRIM_FALL = (31, 31, 31)
    TEXT_OCTAVE = (239, 239, 239)

    # White
    KEY_UP_WHITE = WHITE
    KEY_DOWN_WHITE = KEY_DOWN  # (175, 175, 175)
    FALL_GREEN_WHITE = (0, 208, 0)
    # FONT_WHITE = (63, 63, 63)

    # Black
    KEY_UP_BLACK = ALMOST_BLACK
    KEY_DOWN_BLACK = KEY_DOWN  # (63, 63, 63)
    FALL_GREEN_BLACK = (0, 138, 0)

    OCTAVES = [
        (212, 212, 210),
        (209, 178, 176),
        (255, 190, 162),
        (246, 238, 175),
        (185, 252, 181),
        (128, 233, 217),
        (150, 182, 241),
        (232, 190, 230),
        (228, 211, 227)
    ]

pass  # ColorRGB


class Sizes:
    SCREEN_WIDTH, SCREEN_HEIGHT = 0, 0
    # SCREEN_WIDTH, SCREEN_HEIGHT = 500, 300
    # left, top, width, height, right, bottom, center
pass  # Sizes


class Variables:
    COUNT_WHITE_KEYS = 7 * 5  # Сколько белых клавиш делать
    COUNT_WHITE_KEYS_IDENT = 0  # Сколько клавиш добавить к октаве слева
    OCTAVE = 4  # Октава, с которой начинаем
    MIDI_TONE = 0
    MIDI_INSTRUMENT = 0
    SPEED_FALL = 220
    START_VOLUME = 127
    NAME_NOTE = 'C#'

    KEYS_LINE1 = [pygame.K_BACKQUOTE, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7,
            pygame.K_8, pygame.K_9, pygame.K_0, pygame.K_MINUS, pygame.K_EQUALS, pygame.K_BACKSPACE]
    KEYS_LINE2 = [pygame.K_TAB, pygame.K_q, pygame.K_w, pygame.K_e, pygame.K_r, pygame.K_t, pygame.K_y,
            pygame.K_u, pygame.K_i, pygame.K_o, pygame.K_p, pygame.K_LEFTBRACKET, pygame.K_RIGHTBRACKET, pygame.K_RETURN]
    KEYS_LINE3 = [pygame.K_CAPSLOCK, pygame.K_a, pygame.K_s, pygame.K_d, pygame.K_f, pygame.K_g, pygame.K_h, pygame.K_j,
            pygame.K_k, pygame.K_l, pygame.K_SEMICOLON, pygame.K_QUOTE, pygame.K_BACKSLASH]
    KEYS_LINE4 = [pygame.K_LSHIFT, pygame.K_z, pygame.K_x, pygame.K_c, pygame.K_v, pygame.K_b, pygame.K_n,
            pygame.K_m, pygame.K_COMMA, pygame.K_PERIOD, pygame.K_SLASH, pygame.K_RSHIFT]
    KEYS_IHPDWP = [pygame.K_INSERT, pygame.K_HOME, pygame.K_PAGEUP, pygame.K_DELETE, pygame.K_END, pygame.K_PAGEDOWN]
    KEYS_NUMPAD = [pygame.K_KP0, pygame.K_KP1, pygame.K_KP2, pygame.K_KP3, pygame.K_KP4, pygame.K_KP5, pygame.K_KP6, pygame.K_KP7, pygame.K_KP8, pygame.K_KP9,
            pygame.K_KP_DIVIDE, pygame.K_KP_MULTIPLY, pygame.K_KP_MINUS, pygame.K_KP_PLUS, pygame.K_KP_ENTER, pygame.K_KP_PERIOD]
    KEYS_ARROWS = [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]

    KEYS_PIANO = [
        # Octave first
        pygame.K_TAB, pygame.K_1, pygame.K_q, pygame.K_2, pygame.K_w, pygame.K_e, pygame.K_4, pygame.K_r, pygame.K_5,
            pygame.K_t, pygame.K_6, pygame.K_y,
        # Octave second
        pygame.K_u, pygame.K_8, pygame.K_i, pygame.K_9, pygame.K_o, pygame.K_p, pygame.K_MINUS, pygame.K_LEFTBRACKET,
            pygame.K_EQUALS, pygame.K_RIGHTBRACKET, pygame.K_BACKSPACE, pygame.K_RETURN,
        # Octave third
        pygame.K_LSHIFT, pygame.K_a, pygame.K_z, pygame.K_s, pygame.K_x, pygame.K_c, pygame.K_f, pygame.K_v,
            pygame.K_g, pygame.K_b, pygame.K_h, pygame.K_n,
        # Octave fourth
        pygame.K_m, pygame.K_k, pygame.K_COMMA, pygame.K_l, pygame.K_PERIOD, pygame.K_SLASH, pygame.K_QUOTE,
            pygame.K_RSHIFT, pygame.K_BACKSLASH, pygame.K_END, pygame.K_PAGEUP, pygame.K_PAGEDOWN,
        # Octave fifth
        pygame.K_KP7, pygame.K_KP_DIVIDE, pygame.K_KP8, pygame.K_KP_MULTIPLY, pygame.K_KP9, pygame.K_KP1, pygame.K_KP5,
            pygame.K_KP2, pygame.K_KP6, pygame.K_KP3, pygame.K_KP_PLUS, pygame.K_KP_ENTER
    ]

    KEYS_NAMES = {
        None: '',
        pygame.K_BACKQUOTE: '~',
        pygame.K_1: '1',
        pygame.K_2: '2',
        pygame.K_3: '3',
        pygame.K_4: '4',
        pygame.K_5: '5',
        pygame.K_6: '6',
        pygame.K_7: '7',
        pygame.K_8: '8',
        pygame.K_9: '9',
        pygame.K_0: '0',
        pygame.K_MINUS: '-',
        pygame.K_EQUALS: '=',
        pygame.K_BACKSPACE: 'BS',
        pygame.K_TAB: 'TB',  # 36 - start tone
        pygame.K_q: 'q',
        pygame.K_w: 'w',
        pygame.K_e: 'e',
        pygame.K_r: 'r',
        pygame.K_t: 't',
        pygame.K_y: 'y',
        pygame.K_u: 'u',
        pygame.K_i: 'i',
        pygame.K_o: 'o',
        pygame.K_p: 'p',
        pygame.K_LEFTBRACKET: '[',
        pygame.K_RIGHTBRACKET: ']',
        pygame.K_RETURN: 'EN',
        pygame.K_CAPSLOCK: 'CL',
        pygame.K_a: 'a',
        pygame.K_s: 's',
        pygame.K_d: 'd',
        pygame.K_f: 'f',
        pygame.K_g: 'g',
        pygame.K_h: 'h',
        pygame.K_j: 'j',
        pygame.K_k: 'k',
        pygame.K_l: 'l',
        pygame.K_SEMICOLON: ';',
        pygame.K_QUOTE: "'",
        pygame.K_BACKSLASH: '\\',
        pygame.K_LSHIFT: 'LS',
        pygame.K_z: 'z',
        pygame.K_x: 'x',
        pygame.K_c: 'c',
        pygame.K_v: 'v',
        pygame.K_b: 'b',
        pygame.K_n: 'n',
        pygame.K_m: 'm',
        pygame.K_COMMA: ',',
        pygame.K_PERIOD: '.',
        pygame.K_SLASH: '/',
        pygame.K_RSHIFT: 'RS',
        pygame.K_UP: 'UP',
        pygame.K_DOWN: 'DW',
        pygame.K_LEFT: 'LT',
        pygame.K_RIGHT: 'RT',
        pygame.K_INSERT: 'IN',
        pygame.K_HOME: 'HM',
        pygame.K_PAGEUP: 'PU',
        pygame.K_DELETE: 'DL',
        pygame.K_END: 'EN',
        pygame.K_PAGEDOWN: 'PD',
        pygame.K_KP0: 'N0',
        pygame.K_KP1: 'N1',
        pygame.K_KP2: 'N2',
        pygame.K_KP3: 'N3',
        pygame.K_KP4: 'N4',
        pygame.K_KP5: 'N5',
        pygame.K_KP6: 'N6',
        pygame.K_KP7: 'N7',
        pygame.K_KP8: 'N8',
        pygame.K_KP9: 'N9',
        pygame.K_KP_DIVIDE: 'N/',
        pygame.K_KP_MULTIPLY: 'N*',
        pygame.K_KP_MINUS: 'N-',
        pygame.K_KP_PLUS: 'N+',
        pygame.K_KP_ENTER: 'NE',
        pygame.K_KP_PERIOD: 'N.'
    }

    MIDI_INSTRUMENTS = {
        0: '(Пианино) Концертный рояль',
        1: '(Пианино) Яркое фортепиано',
        2: '(Пианино) Электронный рояль',
        3: '(Пианино) Расстроенное пианино из бара',
        4: '(Пианино) Электропиано 1',
        5: '(Пианино) Электропиано 2',
        6: '(Пианино) Клавесин',
        7: '(Пианино) Клавинет',
        8: '(Хроматическая перкуссия) Челеста',
        9: '(Хроматическая перкуссия) Колокольчики',
        10: '(Хроматическая перкуссия) Музыкальная шкатулка',
        11: '(Хроматическая перкуссия) Вибрафон',
        12: '(Хроматическая перкуссия) Маримба',
        13: '(Хроматическая перкуссия) Ксилофон',
        14: '(Хроматическая перкуссия) Колокола',
        15: '(Хроматическая перкуссия) Цимбалы',
        16: '(Орган) Орган Хаммонда',
        17: '(Орган) Перкуссионный орган',
        18: '(Орган) Рок-орган',
        19: '(Орган) Церковный орган',
        20: '(Орган) Язычковый орган',
        21: '(Орган) Аккордеон',
        22: '(Орган) Гармоника',
        23: '(Орган) Бандонеон',
        24: '(Гитара) Акустическая гитара 1',
        25: '(Гитара) Акустическая гитара 2',
        26: '(Гитара) Электрогитара (джаз)',
        27: '(Гитара) Электрогитара (чистый звук)',
        28: '(Гитара) Электрогитара (с приемом palm mute)',
        29: '(Гитара) Перегруженная электрогитара',
        30: '(Гитара) Дисторшн-электрогитара',
        31: '(Гитара) Гитарные флажолеты',
        32: '(Бас) Акустический бас',
        33: '(Бас) Электрическая бас-гитара (палец)',
        34: '(Бас) Электрическая бас-гитара (медиатор)',
        35: '(Бас) Безладовый бас',
        36: '(Бас) Слэп-бас 1',
        37: '(Бас) Слэп-бас 2',
        38: '(Бас) Синтезаторный бас 1',
        39: '(Бас) Синтезаторный бас 2',
        40: '(Струнные инструменты) Скрипка',
        41: '(Струнные инструменты) Виола',
        42: '(Струнные инструменты) Виолончель',
        43: '(Струнные инструменты) Контрабас',
        44: '(Струнные инструменты) Скрипичное тремоло',
        45: '(Струнные инструменты) Скрипичное пиццикато',
        46: '(Струнные инструменты) Арфа',
        47: '(Струнные инструменты) Литавры',
        48: '(Музыкальный коллектив) Струнный оркестр 1',
        49: '(Музыкальный коллектив) Струнный оркестр 2',
        50: '(Музыкальный коллектив) Синтезаторный оркестр 1',
        51: '(Музыкальный коллектив) Синтезаторный оркестр 2',
        52: '(Музыкальный коллектив) Хор, поющий «А»',
        53: '(Музыкальный коллектив) Голос, поющий «О»',
        54: '(Музыкальный коллектив) Синтезаторный хор',
        55: '(Музыкальный коллектив) Оркестровый акцент',
        56: '(Медные духовые инструменты) Труба',
        57: '(Медные духовые инструменты) Тромбон',
        58: '(Медные духовые инструменты) Туба',
        59: '(Медные духовые инструменты) Приглушенная труба',
        60: '(Медные духовые инструменты) Валторна',
        61: '(Медные духовые инструменты) Духовой оркестр',
        62: '(Медные духовые инструменты) Синтезаторные духовые 1',
        63: '(Медные духовые инструменты) Синтезаторные духовые 2',
        64: '(Язычковые духовые инструменты) Сопрано-саксофон',
        65: '(Язычковые духовые инструменты) Альт-саксофон',
        66: '(Язычковые духовые инструменты) Тенор-саксофон',
        67: '(Язычковые духовые инструменты) Баритон-саксофон',
        68: '(Язычковые духовые инструменты) Гобой',
        69: '(Язычковые духовые инструменты) Английский рожок',
        70: '(Язычковые духовые инструменты) Фагот',
        71: '(Язычковые духовые инструменты) Кларнет',
        72: '(Деревянные духовые инструменты) Пикколо',
        73: '(Деревянные духовые инструменты) Флейта',
        74: '(Деревянные духовые инструменты) Блокфлейта',
        75: '(Деревянные духовые инструменты) Флейта Пана',
        76: '(Деревянные духовые инструменты) Бутылочные горлышки',
        77: '(Деревянные духовые инструменты) Сякухати',
        78: '(Деревянные духовые инструменты) Свисток',
        79: '(Деревянные духовые инструменты) Окарина',
        80: '(Синтезаторный ведущий голос) Ведущий голос 1 (меандр)',
        81: '(Синтезаторный ведущий голос) Ведущий голос 2 (пилообразная волна)',
        82: '(Синтезаторный ведущий голос) Ведущий голос 3 (каллиопа)',
        83: '(Синтезаторный ведущий голос) Ведущий голос 4 (чиффер)',
        84: '(Синтезаторный ведущий голос) Ведущий голос 5 (чаранг)',
        85: '(Синтезаторный ведущий голос) Ведущий голос 6 (голос)',
        86: '(Синтезаторный ведущий голос) Ведущий голос 7 (квинта)',
        87: '(Синтезаторный ведущий голос) Ведущий голос 8 (бас и ведущий голос)',
        88: '(Синтезаторный подголосок) Подголосок 1 (Нью Эйдж, или "Фантасия")',
        89: '(Синтезаторный подголосок) Подголосок 2 (теплый звук)',
        90: '(Синтезаторный подголосок) Подголосок 3 (полисинтезатор)',
        91: '(Синтезаторный подголосок) Подголосок 4 (хор, или "Space Voice")',
        92: '(Синтезаторный подголосок) Подголосок 5 (искривленный звук)',
        93: '(Синтезаторный подголосок) Подголосок 6 (металлический звук)',
        94: '(Синтезаторный подголосок) Подголосок 7 (гало)',
        95: '(Синтезаторный подголосок) Подголосок 8 (свип)',
        96: '(Синтезаторные эффекты) FX 1 (дождь)',
        97: '(Синтезаторные эффекты) FX 2 (саундтрэк)',
        98: '(Синтезаторные эффекты) FX 3 (кристалл)',
        99: '(Синтезаторные эффекты) FX 4 (атмосфера)',
        100: '(Синтезаторные эффекты) FX 5 (яркость)',
        101: '(Синтезаторные эффекты) FX 6 (гоблины)',
        102: '(Синтезаторные эффекты) FX 7 (эхо)',
        103: '(Синтезаторные эффекты) FX 8 (сай-фай)',
        104: '(Этнические музыкальные инструменты) Ситар',
        105: '(Этнические музыкальные инструменты) Банджо',
        106: '(Этнические музыкальные инструменты) Сямисэн',
        107: '(Этнические музыкальные инструменты) Кото',
        108: '(Этнические музыкальные инструменты) Калимба',
        109: '(Этнические музыкальные инструменты) Волынка',
        110: '(Этнические музыкальные инструменты) Фиддл',
        111: '(Этнические музыкальные инструменты) Шахнай',
        112: '(Ударные музыкальные инструменты) Медные колокольчики',
        113: '(Ударные музыкальные инструменты) Агого',
        114: '(Ударные музыкальные инструменты) Стальные барабаны',
        115: '(Ударные музыкальные инструменты) Деревянная коробочка',
        116: '(Ударные музыкальные инструменты) Тайко',
        117: '(Ударные музыкальные инструменты) Мелодичный том-том',
        118: '(Ударные музыкальные инструменты) Электробарабаны',
        119: '(Ударные музыкальные инструменты) Цимбалы задом наперед',
        120: '(Звуковые эффекты) Шум гитарных струн',
        121: '(Звуковые эффекты) Дыхание',
        122: '(Звуковые эффекты) Шум прибоя',
        123: '(Звуковые эффекты) Птичья трель',
        124: '(Звуковые эффекты) Телефонный звонок',
        125: '(Звуковые эффекты) Шум вертолета',
        126: '(Звуковые эффекты) Аплодисменты',
        127: '(Звуковые эффекты) Выстрел'
    }

    # not init
    COUNT_BLACK_KEYS = 0

pass  # Variables


class Change:
    countBlackKeysL = [0, 0, 1, 2, 3, 3, 4, 5]
    countBlackKeysR = [0, 0, 1, 2, 2, 3, 4, 5]
    addToneAndBlack = [1, 1, 0, 1, 1, 1, 0]

    namesNotes = {
        '': ['', '', '', '', '', '', '', '', '', '', '', '', ],
        'C#': ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'],
        'C': ['C', '', 'D', '', 'E', 'F', '', 'G', '', 'A', '', 'B'],
        'do': ['do', '', 're', '', 'mi', 'fa', '', 'sol', '', 'la', '', 'si'],
        'do#': ['do', 'do#', 're', 're#', 'mi', 'fa', 'fa#', 'sol', 'sol#', 'la', 'la#', 'si'],
        'до': ['до', '', 'ре', '', 'ми', 'фа', '', 'соль', '', 'ля', '', 'си'],
        'до#': ['до', 'до#', 'ре', 'ре#', 'ми', 'фа', 'фа#', 'соль', 'соль#', 'ля', 'ля#', 'си'],
        '1': ['1', '', '2', '', '3', '4', '', '5', '', '6', '', '7']
    }

pass  # Change
