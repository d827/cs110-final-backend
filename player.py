import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, name, x, y, img_file):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(img_file).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.isjump = 0
        self.v = 8
        self.m = 2
        self.speed = 2

    def moveLeft(self):
        self.rect.x -= self.speed
    def moveRight(self):
        self.rect.x += self.speed
    def jump(self):
        self.isjump = 1
        
    def update(self):
        #still experimenting with this... goal is to get physics with the jump
        if self.v > 0:
            F = (0.5 * self.m * (self.v*self.v))
        else:
            F = -(0.5 * self.m * (self.v*self.v))

        self.y -= F
        self.v -= 1

        if self.y >= 500:
            self.y = 500
            self.isjump = 0
            self.v = 8
    
