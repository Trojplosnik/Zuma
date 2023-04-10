import pygame
import sys
from sequence import Sequence
from gameMap import GameMap
from frog import Frog


def draw(obj):
    obj.draw()


class Controller:
    def __init__(self, game_map_sprite, frog_position, path_file):
        self.timer_event = pygame.USEREVENT + 1
        self.game_map = GameMap(game_map_sprite=game_map_sprite)
        self.screen = self.game_map.get_screen()
        self.frog = Frog(screen=self.screen, frog_position=frog_position)
        self.seq = Sequence(path_file=path_file, screen=self.screen)
        self.setup_timer()

    def setup_timer(self):
        timer_interval = 10
        pygame.time.set_timer(self.timer_event, timer_interval)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEMOTION:
                self.frog.rotate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.frog.shot()
            elif event.type == self.timer_event:
                self.seq.move()
                self.setup_timer()

    def update(self):
        self.game_map.draw_map()
        self.seq.draw()
        self.frog.draw_frog()
        pygame.display.flip()
