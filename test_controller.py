#pygame.init()
#DISPLAYSURF = pygame.display.set_mode((400, 300))
#pygame.display.set_caption('Hello World!')
#while True:
 #   for event in pygame.event.get():
  #      if event.type == QUIT:
   #         pygame.quit()
    #        sys.exit()
    #pygame.display.update()

import sys
import pygame
import random
import player
import enemy


class Controller:
    def __init__(self, width=640, height=480):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.Surface(self.screen.get_size()).convert()
        pygame.font.init() # you have to call this at the start,
           # if you want to use this module.
        """Load the sprites that we need"""

        self.enemies = pygame.sprite.Group()
        num_enemies = 3
        for i in range(num_enemies):
            x = random.randrange(100, 400)
            y = random.randrange(100, 400)
            self.enemies.add(enemy.Enemy("kitty", x, y, 'cat.png' ))
        self.player = player.Player("dogg", 50, 80, "dog.png")
        self.all_sprites = pygame.sprite.Group((self.player,)+tuple(self.enemies))
        self.state = "GAME"

    def mainLoop(self):
        while True:
            if(self.state == "GAME"):
                self.gameLoop()
            elif(self.state == "GAMEOVER"):
                self.gameOver()

    def gameLoop(self):
        """This is the Main Loop of the Game"""
        pygame.key.set_repeat(1,50)
        while self.state == "GAME":
            self.background.fill((250, 250, 250))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if(event.key == pygame.K_SPACE):
                        self.player.jump()
                    elif(event.key == pygame.K_LEFT):
                        self.player.moveLeft()
                    elif(event.key == pygame.K_RIGHT):
                        self.player.moveRight()
            #check for collisions
            fights = pygame.sprite.spritecollide(self.player, self.enemies, True)
            #redraw the entire screen
            self.enemies.update()
            self.screen.blit(self.background, (0, 0))
            if(self.player.rect.x > 640):
                self.state = "GAMEOVER"
            #display the text
            self.all_sprites.draw(self.screen)
            pygame.display.flip()

    def gameOver(self):
        self.player.kill()
        myfont = pygame.font.SysFont(None, 30)
        message = myfont.render('Game Over', False, (0,0,0))
        self.screen.blit(message, (self.width/2,self.height/2))
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
