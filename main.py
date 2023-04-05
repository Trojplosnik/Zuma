import pygame
from frog import Frog
from controller import Controller
from ball import Ball
from sequence import Sequence


class Game:

    def __init__(self, game_map_sprite, frog_sprite, frog_position):
        pygame.init()
        pygame.display.set_caption("Zuma")
        self.image = pygame.image.load(game_map_sprite)
        self.rect = self.image.get_rect()
        self.screen = pygame.display.set_mode(self.rect.size)
        self.frog = Frog(screen=self.screen, frog_sprite=frog_sprite,
                         frog_position=frog_position)
        self.controller = Controller(screen=self.screen, frog=self.frog)

    def run(self):
        while True:
            self.screen.blit(self.image, self.rect)
            self.controller.events()
            self.controller.update()


if __name__ == '__main__':
    game = Game("images/Map.jpg", "images/Cirno.png", (372, 280))
    game.run()
