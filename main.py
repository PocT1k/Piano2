# UTF-8 Будет здесь!
import pygame
import pygame.midi

from config import Sizes
from config import Variables
from keyboard import *
from draw import drawScene
from proc import procEvents


def initScreen():
    pygame.display.set_caption("Piano48")
    displayInfo = pygame.display.Info()
    if Sizes.SCREEN_WIDTH == 0: Sizes.SCREEN_WIDTH = displayInfo.current_w
    if Sizes.SCREEN_HEIGHT == 0: Sizes.SCREEN_HEIGHT = displayInfo.current_h
    screen = pygame.display.set_mode((Sizes.SCREEN_WIDTH, Sizes.SCREEN_HEIGHT), pygame.FULLSCREEN)
    # screen = pygame.display.set_mode((100, 100), pygame.FULLSCREEN)
    return screen
pass

def initTurntable():
    pygame.midi.init()
    turntable = pygame.midi.Output(0)
    turntable.set_instrument(2)
    return turntable
pass

def calcKeyboard():
    Keyboard.HEIGHT *= Sizes.SCREEN_HEIGHT
    Keyboard.RECT = pygame.Rect(0, Sizes.SCREEN_HEIGHT - Keyboard.HEIGHT, Sizes.SCREEN_WIDTH, Keyboard.HEIGHT)

    Keyboard.KEY_COLLISION_WIDTH = Sizes.SCREEN_WIDTH / Variables.COUNT_WHITE_KEYS
    Keyboard.KEY_SEP *= Keyboard.KEY_COLLISION_WIDTH / 2
    Keyboard.KEY_WIDTH = Keyboard.KEY_COLLISION_WIDTH - 2 * Keyboard.KEY_SEP
    Keyboard.KEY_HEIGHT = Keyboard.HEIGHT - 2 * Keyboard.KEY_SEP

    whiteKeys = Keyboard.whiteKeys
    for i in range (Variables.COUNT_WHITE_KEYS):
        whiteKeys.append(WhiteKey(
            pygame.Rect(i * Keyboard.KEY_COLLISION_WIDTH, Keyboard.RECT.y, Keyboard.KEY_COLLISION_WIDTH, Keyboard.RECT.height),
            pygame.Rect(i * Keyboard.KEY_COLLISION_WIDTH + Keyboard.KEY_SEP, Keyboard.RECT.y + Keyboard.KEY_SEP, Keyboard.KEY_WIDTH, Keyboard.KEY_HEIGHT) ))
        whiteKeys[i].TONE = Variables.INIT_TONE + i
pass


def run():
    pygame.init()
    screen = initScreen()
    Keyboard.turntable = initTurntable()
    calcKeyboard()

    running = True
    while running:
        drawScene(screen)
        running = procEvents()
    pass

    pygame.midi.quit()
    pygame.quit()
pass

if __name__ == '__main__':
    run()
