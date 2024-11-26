# UTF-8 Будет здесь!
import pygame

from config import Sizes, ColorRGB
from keyboard import Keyboard


def initScreen():
    pygame.display.set_caption('Piano48')
    displayInfo = pygame.display.Info()
    if Sizes.SCREEN_WIDTH == 0: Sizes.SCREEN_WIDTH = displayInfo.current_w
    if Sizes.SCREEN_HEIGHT == 0: Sizes.SCREEN_HEIGHT = displayInfo.current_h
    screen = pygame.display.set_mode((Sizes.SCREEN_WIDTH, Sizes.SCREEN_HEIGHT))
    # screen = pygame.display.set_mode((100, 100), pygame.FULLSCREEN)
    scaleW = Sizes.SCREEN_WIDTH / displayInfo.current_w
    scaleH = Sizes.SCREEN_HEIGHT / displayInfo.current_h
    return screen, scaleW, scaleH
pass


def run():
    pygame.init()
    screen, scaleW, scaleH = initScreen()
    keyboard = Keyboard(screen, scaleW, scaleH)

    running = True
    while running:
        running = keyboard.procEvents()
        keyboard.procNotes()

        screen.fill(ColorRGB.SCENE_BG)
        keyboard.draw()
        pygame.display.flip()
    pass

    pygame.quit()
pass


if __name__ == '__main__':
    run()

# pyinstaller main.py config.py keyboard.py -n Пианино -F --noconsole
