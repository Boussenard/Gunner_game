import pygame
from settings import *


class Interface:
    def __init__(self):
        pygame.init()
        self.gun = pygame.image.load('data/Gun_interface.png').convert_alpha()
        self.gun_copy = self.gun
        self.gun_rect = self.gun.get_rect(center=(WIDTH-100, HEIGHT-135))
        self.bullet = pygame.image.load('data/Bullet_int.png')
        self.bullet_rect = self.bullet.get_rect(midright=(WIDTH-20, HEIGHT-104))
        self.can = True

    def interface_draw(self, screen, ammo):
        pygame.draw.rect(screen, (colour[0]-10, colour[1]-10, colour[2]-10), pygame.Rect(WIDTH - 150, HEIGHT - 170, 100, 70))
        screen.blit(self.gun, self.gun_rect)
        pygame.draw.polygon(screen, 'White', [(WIDTH-50, HEIGHT-100), (WIDTH-150, HEIGHT-100), (WIDTH-150, HEIGHT-170), (WIDTH-50, HEIGHT-170)], 3,)
        # number of bullets depends on ammo value
        for i in range(ammo):
            self.bullet_rect = self.bullet.get_rect(midright=(WIDTH - 20, HEIGHT - 104 - 15 * i))
            screen.blit(self.bullet, self.bullet_rect)

    def update(self, shot):
        if shot is True:
            self.gun = pygame.transform.rotate(self.gun_copy, 20)
            self.gun_rect = self.gun.get_rect(center=(WIDTH-100, HEIGHT-135))
        elif shot == 'no ammo':
            self.gun = pygame.transform.rotate(self.gun_copy, -30)
            self.gun_rect = self.gun.get_rect(center=(WIDTH - 100, HEIGHT - 135))
        elif shot is False:
            self.gun = self.gun_copy
            self.gun_rect = self.gun.get_rect(center=(WIDTH - 100, HEIGHT - 135))
