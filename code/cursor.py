import pygame


class Cursor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('data/Cursor.png').convert_alpha()
        self.x_cursor, self.y_cursor = pygame.mouse.get_pos()
        self.rect = self.image.get_rect(center=(self.x_cursor, self.y_cursor))

    def update(self):
        self.x_cursor, self.y_cursor = pygame.mouse.get_pos()
        self.rect = self.image.get_rect(center=(self.x_cursor, self.y_cursor))
