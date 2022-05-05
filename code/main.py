import pygame
import sys
from settings import *
from player import Player
from gun import Gun
from cursor import Cursor
from bullet import Bullet


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Gunner')
        pygame.mouse.set_visible(False)
        self.clock = pygame.time.Clock()

        # game objects
        self.player = Player()
        self.gun = Gun()
        self.cursor = Cursor()

        # game groups
        self.bullet_group = pygame.sprite.Group()

    def run(self):
        while 1 == 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # shooting
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y, angle, vector = self.gun.bullet_data()
                    self.bullet_group.add(Bullet(x, y, angle, vector))

            self.screen.fill((29, 29, 29))
            # updating objects
            self.player.update(self.gun.player_look_angle())
            # updating data for gun
            player_x, player_y, flip = self.player.gun_cords()
            self.gun.update(player_x, player_y, flip)
            self.cursor.update()

            # updating groups
            self.bullet_group.update()

            # drawing game objects
            self.screen.blit(self.player.image, self.player.rect)
            self.screen.blit(self.gun.image, self.gun.rect)
            self.screen.blit(self.cursor.image, self.cursor.rect)
            self.bullet_group.draw(self.screen)

            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.run()
