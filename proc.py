# UTF-8 Будет здесь!
import pygame

from config import Variables
from keyboard import Keyboard


def procMouseKey(cX, cY):
    whiteKeys = Keyboard.whiteKeys
    for i in range (Variables.COUNT_WHITE_KEYS):
        if (whiteKeys[i].COLLISION_RECT.collidepoint(cX, cY)):
            Keyboard.isWhiteKeys[i][0] = True
            Keyboard.turntable.note_on(46 + i, 127)
        else:
            Keyboard.isWhiteKeys[i][0] = False

def procKeyboard():
    cX, cY = pygame.mouse.get_pos()
    if Keyboard.RECT.collidepoint(cX, cY):
        procMouseKey(cX, cY)

def procEvents(keyboard):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            keyboard.isMouseDown = True
            procKeyboard()

        elif event.type == pygame.MOUSEBUTTONUP:
            keyboard.isMouseDown = False
        elif event.type == pygame.MOUSEMOTION:
            if (keyboard.isMouseDown):
                procKeyboard()

    return True
