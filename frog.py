import pygame
import math
from ball import Ball


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

    def draw_frog(self):
        self.screen.blit(self.image, self.rect)
        self.bullet_center.draw_ball()
        self.bullet_top.draw_ball()

    def rotate(self):
        angle = int(find_angle(*self.rect.center))
        self.image = pygame.transform.rotate(self.original_image, angle)
        self.rect = self.image.get_rect(center=self.frog_position)
        self.bullet_top.move_ball(self.radius*math.cos(math.radians(angle)) +
                                  self.frog_position[0],
                                  - self.radius*math.sin(math.radians(angle))
                                  + self.frog_position[1])

    def shot(self):
        flying_bullet = self.bullet_top
        self.bullet_center.move_ball(self.bullet_top.rect.center[0],
                                     self.bullet_top.rect.center[1])
        self.bullet_top = self.bullet_center
        self.bullet_center = self.generate()
        flying_bullet.angle =\
            math.radians(int(find_angle(*flying_bullet.rect.center)))
        return flying_bullet

    def generate(self):
        return Ball(self.screen, *self.rect.center)





