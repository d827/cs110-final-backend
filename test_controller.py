import pygame
#import sys
#from pygame.locals import *

#pygame.init()
#DISPLAYSURF = pygame.display.set_mode((400, 300))
#pygame.display.set_caption('Hello World!')
#while True:
 #   for event in pygame.event.get():
  #      if event.type == QUIT:
   #         pygame.quit()
    #        sys.exit()
    #pygame.display.update()

class Controller:
    def __init__(self, width = 500, height = 500):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display
        self.background = pygame.Surface(self.screen.get_size()).convert()
        pygame.font.init()

    def mainLoop(self):
        while True:
            if self.state == "GAME":
                self.gameLoop()
            elif self.state == "GAMEOVER":
                self.gameOver()

    def gameLoop():

        while self.state == "GAME":
            self.bg = pygame.image.load(#backgroundimage).convert()
            self.screen.blit(self.bg, (self.width, self.height))
            pygame.display.update
            for event in pygame.event.get():
                if 
