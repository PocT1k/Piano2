# UTF-8 Будет здесь!
import pygame
import pygame.midi

from config import Sizes
from config import Variables
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

def calcSizes():
    Sizes.KEY_HEIGHT *= Sizes.SCREEN_HEIGHT
    Sizes.KEY_WIDTH = Sizes.SCREEN_WIDTH / Variables.COUNT_WHITE_KEYS
    Sizes.KEY_SEP *= Sizes.SCREEN_WIDTH / (Variables.COUNT_WHITE_KEYS + 1)
    # Sizes.KEY_SEP = Sizes.KEY_SEP * (Sizes.KEY_WIDTH -)
pass


def run():
    pygame.init()
    screen = initScreen()
    turntable = initTurntable()
    calcSizes()

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
