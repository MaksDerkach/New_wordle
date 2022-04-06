import pygame
import random
import sys

pygame.init()

SIZE = W, H = 800, 900

class KeyBoard:
    def __init__(self):
        pass

class PlayingField:
    def __init__(self):
        self.keybord = pygame.Surface(500, 700)

class WordleGame:
    def __init__(self):
        self.size = SIZE
        self.screen = pygame.display.set_mode(SIZE)
        self.playing_field = PlayingField()
        self.keyboard = KeyBoard()

    def run(self):
        while True:

            self.screen.fill('black')

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()




if __name__ == '__main__':
    game = WordleGame()
    game.run()