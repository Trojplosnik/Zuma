import pygame
from random import randint
import math
import os

DEFAULT_BALL_SIZE = 40
DEFAULT_SPEED = 10

"""
Класс шарика, описывает поведение шарика
-создание случайного шарика
-полет шарика при выстреле
-настройка коллизий
-перемешение
-орисовка

ROOT_DIR - путь в корневую папку проекта
counter - итератор по пути шарика
color - цвет ширика
DEFAULT_SPEED - скорость шарика в полете
DEFAULT_BALL_SIZE - размер шарика
"""

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


class Ball(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, color="RANDOM"):
        super().__init__()
        self.counter = 0
        self.screen = screen
        self.color = color
        if color == "GREEN":
            self.original_image = pygame.image.load(
                f'{ROOT_DIR}/images/gball.png')
        elif color == "YELLOW":
            self.original_image = pygame.image.load(
                f'{ROOT_DIR}/images/yball.png')
        elif color == "BLUE":
            self.original_image = pygame.image.load(
                f'{ROOT_DIR}/images/bball.png')
        elif color == "RED":
            self.original_image = pygame.image.load(
                f'{ROOT_DIR}/images/rball.png')
        else:
            i = randint(0, 3)
            if i == 0:
                self.color = "GREEN"
                self.original_image = pygame.image.load(
                    f'{ROOT_DIR}/images/gball.png')
            elif i == 1:
                self.color = "YELLOW"
                self.original_image = pygame.image.load(
                    f'{ROOT_DIR}/images/yball.png')
            elif i == 2:
                self.color = "BLUE"
                self.original_image = pygame.image.load(
                    f'{ROOT_DIR}/images/bball.png')
            else:
                self.color = "RED"
                self.original_image = pygame.image.load(
                    f'{ROOT_DIR}/images/rball.png')
        self.image = pygame.transform.scale(self.original_image,
                                            (DEFAULT_BALL_SIZE,
                                             DEFAULT_BALL_SIZE))
        self.rect = self.image.get_rect()
        self.rect.center = x, y
        self.angle = 0

    """
        Проверяет столкнулись ли шарики
    """

    def collode_balls(self, other):
        return math.sqrt((other.rect.centerx - self.rect.centerx) ** 2
                         + ((other.rect.centery - self.rect.centery) ** 2)) \
               < DEFAULT_BALL_SIZE - 4

    """
        Перемещает ширик во время полета и уничтожает его после вылета за экран
    """

    def fly(self):
        self.rect.centerx += int(math.cos(self.angle) * DEFAULT_SPEED)
        self.rect.centery -= int(math.sin(self.angle) * DEFAULT_SPEED)
        if self.rect.x > self.screen.get_width() \
                or self.rect.x < -DEFAULT_BALL_SIZE \
                or self.rect.y > self.screen.get_height() \
                or self.rect.y < -DEFAULT_BALL_SIZE:
            self.kill()

    """
        Перемещает ширик в определенные координаты
    """

    def move_ball(self, x, y):
        self.rect.center = x, y

    """
        Отрисовывает шарик
    """

    def draw_ball(self):
        self.screen.blit(self.image, self.rect)
