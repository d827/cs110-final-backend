import player
import pygame

class Powerup(pygame.sprite.Sprite):
    def __init__(self, name, x, y, img_file):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(img_file).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def speedUp(self):
        player.speed += 2
        #thisll raise the speed up of the player by 2
    def lowGrav(self):
        player.m = 1
        #the idea is to lower the mass so you jump higher
        
