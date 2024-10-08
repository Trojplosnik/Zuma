import pygame
import re

"""
    Класс игровой карты
    Отрисововает карту и цель к которой стремятся шарики 
    
    
    DEFAULT_TARGET_SIZE - размар цели
"""

num_reg = r'\d+'
DEFAULT_TARGET_SIZE = 100


class GameMap:
    def __init__(self, game_map_sprite, target_sprite, path_file,
                 target_position):
        self._image = pygame.image.load(game_map_sprite)
        self._rect = self._image.get_rect()
        self.target_image = pygame.image.load(target_sprite)
        self.target_image = pygame.transform.scale(self.target_image,
                                                   (DEFAULT_TARGET_SIZE,
                                                    DEFAULT_TARGET_SIZE))
        self.target_rect = self.target_image.get_rect(center=target_position)
        pygame.display.set_caption("Zuma")
        self._screen = pygame.display.set_mode(self._rect.size)
        self.path = []
        with open(path_file) as path:
            for line in path:
                self.path.append(re.findall(num_reg, line))

    """
        Отрисовывает шарик
    """

    def draw_map(self):
        self._screen.blit(self._image, self._rect)

    """
        Отрисовывает цель
    """

    def draw_target(self):
        self._screen.blit(self.target_image, self.target_rect)

    """
        Геттер для экрана
    """

    def get_screen(self):
        return self._screen
