import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, name, x, y, img_file):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(img_file).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 2

        self.isJump = False
        self.jumpCount = 10
    def moveLeft(self):
        self.rect.x -= self.speed
    def moveRight(self):
        self.rect.x += self.speed
    def jump(self):
        if self.jumpCount >= -10:
            neg = 1
            if self.jumpCount < 0:
                neg = -1  
            self.rect.y -= (self.jumpCount ** 2) * 0.5 * neg
            self.jumpCount -= 1
        else:
            self.isJump = False
            self.jumpCount = 10
    def update(self):
        if self.rect.y > 80:
            self.rect.y = 80
        pass

