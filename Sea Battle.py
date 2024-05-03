#  Sea Battle
v = 0.02

from random import randint, choice
from time import sleep
import os

def greating():
    os.system('color a')
    os.system('cls')
    print("\n\n\n"
          "      МОРСКОЙ БОЙ\n"
          "\n"
          "   ┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉\n"
          "   ┉┉┉┉┉┉┉┉┉▃▅▇┉┉┉┉\n"
          "   ┉┉┉┉┉╱▔▔▔▔▔▔▏┉┉┉\n"
          "   ▂▂▂┉╱▔▔▔▔▔▉▔┉┉┉┉\n"
          '   ┉╲▔▔▔▔▔▔▔▔▔▔▔▔▔▏\n'
          '   ┉┉╲▂▂▂▂▂▂▂▂▂▂▂╱┉\n'
          "   ▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔\n"
          "\n"
          "Version", v)
    input("\n\nНажмите любую клавишу для продолжения...")
    os.system('cls')

class BoardException(Exception):
    pass

class BoardShipException(BoardException):
    pass

class BoardOutException(BoardException):
    def __str__(self):
        return 'Введите координаты поля - x y'

class BoardUsedException(BoardException):
    def __str__(self):
       return 'В эту клетку нельзя стрелять !'

class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, another):
        return self.x == another.x and self.y == another.y

    def __repr__(self):
        return f"Dot({self.x}, {self.y}"
