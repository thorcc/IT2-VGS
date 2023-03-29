import pygame
import random

class Hinder:
    def __init__(self, bredde_verden, høyde_verden):
        self._høyde = random.randint(50, 100)
        self._bredde = 20
        self._y = høyde_verden - self._høyde
        self._x = bredde_verden

    def tegn(self, vindu):
        pygame.draw.rect(vindu, (0,0,0), (self._x, self._y, self._bredde, self._høyde))
    
    def flytt(self):
        self._x -= 2

