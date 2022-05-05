import pygame
from settings import *


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, angle, vector):
        super().__init__()
        self.image = pygame.image.load('data/Bullet.png').convert_alpha()
        self.rect = self.image.get_rect(midleft=(x, y))
        self.image = pygame.transform.rotate(self.image, angle)
        self.speed = 30
        self.direction = vector.normalize()

    def update(self):
        self.rect.center += self.direction * self.speed
        if self.rect.centerx > WIDTH or self.rect.centerx < 0 or self.rect.centery > HEIGHT or self.rect.centery < 0:
            self.kill()
