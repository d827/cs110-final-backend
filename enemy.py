import pygame
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self, name, x, y, img_file):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(img_file).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        num = random.randrange(-4,5)
        self.rect.x += num

#the goal here is to get some enemies on platforms that move, wait, then move
#again.... trying to figure this out, as the wait might actually be the job
#for the controller... the update function cannot containt the delay since
#it updates every frame. as of right now this just moves horizontally back and
#forth
 
