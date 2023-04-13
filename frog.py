import pygame
import math
from ball import Ball

"""
    Класс "Лягушки"

    frog_position - разположение "Лягушки" на карте
    bullet_center - шарик в центре лягунки, следуюший после того, которым мы стреляем
    bullet_top - ширик, которым игрок бодет стрелять

    Исполняет роль пушки - главного объекта с которым взаимодействует игрок:
    -Позволяет стрелять шариками в сторону расположения курсора
    -разворачивается вслед за курсором
    -Отрисовает "Лягушку" и 2 шарика на ней (1 которым стреляем и 1 в "обойме")

"""

"""
    Нахождение угла между точкой на экране и расположения курсора мыши
"""


def find_angle(x, y):
    mouse_x, mouse_y = pygame.mouse.get_pos()
    d_x = mouse_x - x
    d_y = mouse_y - y
    return (180 / math.pi) * -math.atan2(d_y, d_x)


class Frog(pygame.sprite.Sprite):
    def __init__(self, screen, frog_position):
        super().__init__()
        self.screen = screen
        self.original_image = pygame.image.load("images/Cirno.png")
        self.image = pygame.transform.rotate(self.original_image, 90)
        self.rect = self.image.get_rect(center=frog_position)
        self.frog_position = frog_position
        self.bullet_center = self.generate()
        self.bullet_top = Ball(self.screen, x=self.rect.midtop[0],
                               y=self.rect.midtop[1])
        self.radius = math.sqrt((self.frog_position[0] -
                                 self.rect.midtop[0]) ** 2
                                + (self.frog_position[1] -
                                   self.rect.midtop[1]) ** 2)
        self.speed = 10

    """
        Отрисовка "Лягушки" и шариков на ней
    """

    def draw_frog(self):
        self.screen.blit(self.image, self.rect)
        self.bullet_center.draw_ball()
        self.bullet_top.draw_ball()

    """
        Поворот "Лягушки" и шариков на ней вслед за курсором
    """

    def rotate(self):
        angle = int(find_angle(*self.rect.center))
        self.image = pygame.transform.rotate(self.original_image, angle)
        self.rect = self.image.get_rect(center=self.frog_position)
        self.bullet_top.move_ball(self.radius * math.cos(math.radians(angle)) +
                                  self.frog_position[0],
                                  - self.radius * math.sin(math.radians(angle))
                                  + self.frog_position[1])

    """
        Выстрел шарика в направлении курсора
    """

    def shot(self):
        flying_bullet = self.bullet_top
        self.bullet_center.move_ball(self.bullet_top.rect.center[0],
                                     self.bullet_top.rect.center[1])
        self.bullet_top = self.bullet_center
        self.bullet_center = self.generate()
        flying_bullet.angle = \
            math.radians(int(find_angle(*self.frog_position)))
        return flying_bullet

    """
        Генерация нового шарика в центре лягушки
    """

    def generate(self):
        return Ball(self.screen, *self.rect.center)
