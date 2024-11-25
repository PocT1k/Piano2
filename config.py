# UTF-8 Будет здесь!
import pygame


class ColorRGB:
    SCENE_BG = (56, 56, 56)
    KEYBOARD_BG = (0, 0, 0)

    KEY_UP_WHITE = (255, 255, 255)
    KEY_DOWN_WHITE = (175, 175, 175)
    FALL_GREEN_WHITE = (0, 208, 0)

    KEY_UP_BLACK = (15, 15, 15)
    KEY_DOWN_BLACK = (63, 63, 63)
    FALL_GREEN_BLACK = (0, 138, 0)

class Sizes:
    SCREEN_WIDTH, SCREEN_HEIGHT = 0, 0
    # SCREEN_WIDTH, SCREEN_HEIGHT = 500, 300

class Variables:
    COUNT_WHITE_KEYS = 28
    COUNT_WHITE_KEYS_IDENT = 0
    OCTAVE = 3
    MIDI_TONE = 0
    MIDI_INSTRUMENT = 2

    KEYS_LINE_1 = [pygame.K_BACKQUOTE, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7,
              pygame.K_8, pygame.K_9, pygame.K_0, pygame.K_MINUS, pygame.K_EQUALS, pygame.K_BACKSPACE]
    KEYS_LINE_2 = [pygame.K_TAB, pygame.K_q, pygame.K_w, pygame.K_e, pygame.K_r, pygame.K_t, pygame.K_y,
              pygame.K_u, pygame.K_i, pygame.K_o, pygame.K_p, pygame.K_LEFTBRACKET, pygame.K_RIGHTBRACKET, pygame.K_RETURN]
    KEYS_LINE_3 = [pygame.K_CAPSLOCK, pygame.K_a, pygame.K_s, pygame.K_d, pygame.K_f, pygame.K_g, pygame.K_h, pygame.K_j,
              pygame.K_k, pygame.K_l, pygame.K_SEMICOLON, pygame.K_QUOTE, pygame.K_BACKSLASH]
    KEYS_LINE_4 = [pygame.K_LSHIFT, pygame.K_z, pygame.K_x, pygame.K_c, pygame.K_v, pygame.K_b, pygame.K_n,
              pygame.K_m, pygame.K_COMMA, pygame.K_PERIOD, pygame.K_SLASH, pygame.K_RSHIFT]
    KEYS_ARROWS = [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]
    KEYS_PIANO = [
        pygame.K_TAB, pygame.K_1, pygame.K_q, pygame.K_2, pygame.K_w, pygame.K_e, pygame.K_4, pygame.K_r, pygame.K_5, pygame.K_t, pygame.K_6, pygame.K_y,
            pygame.K_u, pygame.K_8, pygame.K_i, pygame.K_9, pygame.K_o, pygame.K_p, pygame.K_MINUS, pygame.K_LEFTBRACKET, pygame.K_EQUALS, pygame.K_RIGHTBRACKET, pygame.K_BACKSPACE, pygame.K_RETURN,
        pygame.K_LSHIFT, pygame.K_a, pygame.K_z, pygame.K_s, pygame.K_x, pygame.K_c, pygame.K_f, pygame.K_v, pygame.K_g, pygame.K_b, pygame.K_h, pygame.K_n,
            pygame.K_m, pygame.K_k, pygame.K_COMMA, pygame.K_l, pygame.K_PERIOD, pygame.K_SLASH, pygame.K_QUOTE, pygame.K_RSHIFT, pygame.K_BACKSLASH
    ]
    KEYS_NAMES = {
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
        pygame.K_TAB: 'TB',
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
        pygame.K_RIGHT: 'RT'
    }

    # not init
    COUNT_BLACK_KEYS = 0

class Change:
    countBlackKeysL = [0, 0, 1, 2, 3, 3, 4, 5]
    countBlackKeysR = [0, 0, 1, 2, 2, 3, 4, 5]
    addToneAndBlack = [1, 1, 0, 1, 1, 1, 0]
    nameNotes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
