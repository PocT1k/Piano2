# UTF-8 Будет здесь!
#import pygame
import pygame.midi

from config import Sizes
from keyboard import Keyboard


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

    running = True
    while running:
        running = keyboard.procEvents()
        keyboard.procNotes()

        screen.fill(Keyboard.SCENE_BG)
        keyboard.draw()
        pygame.display.flip()
    pass

    pygame.midi.quit()
    pygame.quit()
pass

if __name__ == '__main__':
    run()
