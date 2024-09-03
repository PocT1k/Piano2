# UTF-8 Будет здесь!
import pygame

from config import Variables
from keyboard import Keyboard


def drawKey(screen):
    keyboard = Keyboard
    isWhiteKeys = keyboard.isWhiteKeys
    for i in range (Variables.COUNT_WHITE_KEYS):
        if(isWhiteKeys[i]):
            pygame.draw.rect(screen, keyboard.KEY_DOWN_WHITE, keyboard.whiteKeys[i].DRAW_RECT)
        else:
            pygame.draw.rect(screen, keyboard.KEY_UP_WHITE, keyboard.whiteKeys[i].DRAW_RECT)
pass

def drawKeyboard(screen):
    pygame.draw.rect(screen, Keyboard.BG, Keyboard.RECT)
    drawKey(screen)

def drawScene(screen):
    screen.fill(Keyboard.SCENE_BG)
    drawKeyboard(screen)
    pygame.display.flip()
pass