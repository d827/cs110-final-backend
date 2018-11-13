import pygame

class Hero(pygame.sprite.Sprite):
    def __init__(self, name, x, y, img.file):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(img_file).convert_alpha()
        self.rect = self.image.get_rect()
        selft.rect.x = x
        self.rect.y = y
        
    def moveLeft(self):
        self.rect.x -= 1
    def moveRight(self):
        self.rect.x += 1
    def jump(self):
        
