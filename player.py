import pygame
import sprite

class Player:

    def __init__(self):
        self.gameplayService=None

        self.vx=0
        self.vy=0
        self.oldX=0
        self.oldY=0

        self.sprite=None


    def load(self,pGameplayService):
        self.gameplayService=pGameplayService

        self.sprite=sprite.Sprite(self.gameplayService.assetManager.getImage("images/player.png"),0,self.gameplayService.screen.get_height() / 2)


    def update(self,dt):
        self.oldX=self.sprite.x
        self.oldY=self.sprite.y

        keys = pygame.key.get_pressed()

        self.sprite.x+= self.vx
        self.sprite.y+= self.vy

        ###MOVE########
        if keys[pygame.K_UP]:
            self.vy = -5

        elif keys[pygame.K_DOWN]:
            self.vy = 5

        else:
            self.vy = 0


        ######Collision with screen edges #############
        if self.vy != 0:

            if self.sprite.y < 0:
                self.sprite.y = 0
                self.vy = 0

            elif self.sprite.y + self.sprite.image.get_height() > self.gameplayService.screen.get_height():

                self.sprite.y = self.gameplayService.screen.get_height() - self.sprite.image.get_height()
                self.vy = 0


    def draw(self):

        self.sprite.draw(self.gameplayService.screen)