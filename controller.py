import pygame
import sys
from sequence import Sequence


def draw(obj):
    obj.draw()


class Controller:
    def __init__(self, frog, screen, game_map):
        self.game_map = game_map
        self.timer_event = pygame.USEREVENT + 1
        self.screen = screen
        self.frog = frog
        self.seq = Sequence()
        self.setup_timer()

    def setup_timer(self):
        timer_interval = 2500
        pygame.time.set_timer(self.timer_event, timer_interval)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEMOTION:
                self.frog.rotate()
            elif event.type == self.timer_event:
                self.seq.generate(self.screen)
                self.seq.move()
                self.setup_timer()

    def update(self):
        self.game_map.draw_map()
        self.seq.draw()
        self.frog.draw_frog()
        pygame.display.flip()
