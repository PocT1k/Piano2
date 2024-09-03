# UTF-8 Будет здесь!
import pygame

from config import ColorRGB
from config import Sizes


def drawKey(screen):
    for i in range (28):
        pygame.draw.rect(screen, ColorRGB.KEY_UP_WHITE,
                         (Sizes.KEY_SEP + i * Sizes.KEY_WIDTH, Sizes.SCREEN_HEIGHT - Sizes.KEY_HEIGHT,
                          Sizes.KEY_WIDTH - Sizes.KEY_SEP, Sizes.KEY_HEIGHT))
pass

def drawScene(screen):
    screen.fill(ColorRGB.BG)
    drawKey(screen)
    pygame.display.flip()
pass