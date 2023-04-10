import pygame
import math
from ball import Ball


class Frog:
    def __init__(self, screen, frog_position):
        self.screen = screen
        self.original_image = pygame.image.load("images/Cirno.png")
        self.image = self.original_image.copy()
        self.frog_rect = self.image.get_rect(center=frog_position)
        self.frog_position = frog_position
        self.bullet = Ball(self.screen, *self.frog_rect.midtop)
        self.bullet2 = Ball(self.screen, *self.frog_rect.center)
        self.radius = math.sqrt(self.frog_position[0] - self.bullet.ball_rect.x
                                + self.frog_position[1] - self.bullet.ball_rect.y)
        print(int(self.radius))

    def draw_frog(self):
        self.screen.blit(self.image, self.frog_rect)
        self.bullet.draw_ball()
        self.bullet2.draw_ball()

    def rotate(self):
        angle = int(self.find_angle())
        # print(angle)
        self.image = pygame.transform.rotate(self.original_image, angle)
        self.frog_rect = self.image.get_rect(center=self.frog_position)
        # self.bullet.move_ball(*self.frog_rect.midtop)
        self.bullet.move_ball(self.radius*5*math.cos(math.radians(angle)) +
                              self.frog_position[0],
                              - self.radius*5*math.sin(math.radians(angle))
                              + self.frog_position[1])

    def shot(self):
        angle = int(self.find_angle())

    def find_angle(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        d_x = mouse_x - self.frog_rect.centerx
        d_y = mouse_y - self.frog_rect.centery
        return (180 / math.pi) * -math.atan2(d_y, d_x)



