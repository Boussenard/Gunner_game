import pygame


class Camera:
    def __init__(self):
        self.offset_vector = pygame.math.Vector2()
        self.x_cursor, self.y_cursor = pygame.mouse.get_pos()

    def calculating(self, player):
        # calculating vector's length
        self.offset_vector.xy = (self.x_cursor - player.rect.centerx)/-3, (self.y_cursor - player.rect.centery)/-3

    def update(self, player):
        self.x_cursor, self.y_cursor = pygame.mouse.get_pos()
        self.calculating(player)

    def camera_draw(self, screen, image, rect):
        screen.blit(image, rect.center + self.offset_vector)
