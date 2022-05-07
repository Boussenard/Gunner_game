import pygame
from settings import *


class Interface:
    def __init__(self):
        pygame.init()
        self.face = pygame.image.load('data/Player_face_interface.png').convert_alpha()
        self.face_rect = self.face.get_rect(topright=(WIDTH-50, 50))
        self.gun = pygame.image.load('data/Gun_interface.png').convert_alpha()
        self.gun_rect = self.gun.get_rect(topleft=(50, 50))

    def interface_draw(self, screen):
        screen.blit(self.face, self.face_rect)
        screen.blit(self.gun, self.gun_rect)
        pygame.draw.polygon(screen, 'White', [(40, 40), (124, 40), (124, 124), (40, 124)], 4,)
        pygame.draw.polygon(screen, 'White', [(WIDTH - 40, 40), (WIDTH - 124, 40), (WIDTH - 124, 124), (WIDTH - 40, 124)], 4, )
