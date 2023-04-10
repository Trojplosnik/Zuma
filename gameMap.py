import pygame
import re


num_reg = r'\d+'


class GameMap:
    def __init__(self, game_map_sprite, path_file):
        self._image = pygame.image.load(game_map_sprite)
        self._rect = self._image.get_rect()
        pygame.display.set_caption("Zuma")
        self._screen = pygame.display.set_mode(self._rect.size)
        self.path = []
        with open(path_file) as path:
            for line in path:
                self.path.append(re.findall(num_reg, line))

    def draw_map(self):
        self._screen.blit(self._image, self._rect)

    def get_screen(self):
        return self._screen
