import pygame
import sys


class Controller:
    def __init__(self, frog):
        self.frog = frog

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEMOTION:
                self.frog.rotate()

    def update(self):
        self.frog.show()
        pygame.display.flip()
