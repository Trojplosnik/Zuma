import pygame
import math


class Frog:
    def __init__(self, screen, frog_position):
        self.screen = screen
        self.original_image = pygame.image.load("images/Cirno.png")
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect(center=frog_position)
        self.frog_position = frog_position
        self.screen.blit(self.image, self.rect)

    def draw_frog(self):
        self.screen.blit(self.image, self.rect)

    def rotate(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        rel_x, rel_y = mouse_x - self.rect.centerx, mouse_y - self.rect.centery
        angle = (180 / math.pi) * -math.atan2(rel_y, rel_x) - 90
        self.image = pygame.transform.rotate(self.original_image, int(angle))
        self.rect = self.image.get_rect(center=self.frog_position)
