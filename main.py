# UTF-8 Будет здесь!
#import pygame
import pygame.midi

from config import Sizes
from config import Variables
from keyboard import Keyboard
from draw import drawScene
from proc import procEvents


def initScreen():
    pygame.display.set_caption('Piano48')
    displayInfo = pygame.display.Info()
    if Sizes.SCREEN_WIDTH == 0: Sizes.SCREEN_WIDTH = displayInfo.current_w
    if Sizes.SCREEN_HEIGHT == 0: Sizes.SCREEN_HEIGHT = displayInfo.current_h
    screen = pygame.display.set_mode((Sizes.SCREEN_WIDTH, Sizes.SCREEN_HEIGHT))
    # screen = pygame.display.set_mode((100, 100), pygame.FULLSCREEN)
    return screen
pass


def run():
    pygame.init()
    screen = initScreen()
    keyboard = Keyboard(screen)
    keyboard.calc()

    running = True
    while running:
        drawScene(screen)
        running = procEvents(keyboard)
    pass

    pygame.midi.quit()
    pygame.quit()
pass

if __name__ == '__main__':
    run()
