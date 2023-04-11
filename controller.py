import pygame
import sys
from sequence import Sequence
from gameMap import GameMap
from frog import Frog


def draw(obj):
    obj.draw()


class Controller:
    def __init__(self, game_map_sprite, frog_position, path_file, target_sprite, target_position):
        self.timer_event = pygame.USEREVENT + 1
        self.timer_event_generate = pygame.USEREVENT + 2
        self.game_map = GameMap(game_map_sprite=game_map_sprite, path_file=path_file,
                                target_sprite=target_sprite, target_position=target_position)
        self.screen = self.game_map.get_screen()
        self.frog = Frog(screen=self.screen, frog_position=frog_position)
        self.seq = Sequence(screen=self.screen, path=self.game_map.path)
        self.setup_timer()
        self.setup_timer_generate()
        self.flying_bullets = pygame.sprite.Group()

    def setup_timer(self):
        timer_interval = 20
        pygame.time.set_timer(self.timer_event, timer_interval)

    def setup_timer_generate(self):
        timer_interval = 820
        pygame.time.set_timer(self.timer_event_generate, timer_interval)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEMOTION:
                self.frog.rotate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.flying_bullets.add(self.frog.shot())
            elif event.type == self.timer_event:
                if self.flying_bullets:
                    for flying_bullet in self.flying_bullets:
                        flying_bullet.fly()
                self.seq.move()
                self.setup_timer()
            elif event.type == self.timer_event_generate:
                self.seq.generate()
                self.setup_timer_generate()

    def update(self):
        self.game_map.draw_map()
        self.seq.draw()
        self.game_map.draw_target()
        self.frog.draw_frog()
        self.flying_bullets.draw(surface=self.screen)
        pygame.display.flip()
