import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('bullet.png')
        self.rect = self.image.get_rect()
    #positions the bullet at the players curretnt location, not sure if correct
        start_x = self.player_sprite.center_x
        start_y = self.player_sprite.center_y
        self.rect.center_x = start_x
        self.rect.center_y = start_y
    def update(self):
        if (self.direction == "right"):
          self.rect.centerx += 10
        if (self.direction == "left"):
          self.rect.centerx -= 10)
    #supposed to remove the bullet once it gets off the screen
        if self.rect.bottom > self.width or self.rect.top < 0 or self.rect.right < 0 or self.rect.left > self.width:
                self.rect.kill()
