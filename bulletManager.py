import pygame.draw

###############CLASS SHOOT#############################
class Bullet:

    def __init__(self,pX,pY,pVx,pVy):
        self.vx=pVx
        self.vy=pVy

        self.x=pX
        self.y=pY

        self.width=10
        self.height=3

    def update(self,dt):
        self.x+=self.vx*60*dt
        self.y+=self.vy*60*dt


    def draw(self,pScreen):
        pygame.draw.rect(pScreen,[0,255,0],(self.x,self.y,self.width,self.height))



#################CLASS SHOOT MANAGER##################################
class BulletManager:

    def __init__(self,pGameplayService):
        self.lstBullet=[]
        self.gameplayService=pGameplayService


    def addBullet(self,pX,pY,pVx,pVy):
        #init shoot
        myBullet=Bullet(pX,pY,pVx,pVy)

        self.lstBullet.append(myBullet)


    def update(self,dt):

        for i in range(len(self.lstBullet) - 1, -1, -1):
            bullet=self.lstBullet[i]
            bullet.update(dt)

            #delete shoot
            if bullet.x>self.gameplayService.screen.get_width():
                self.lstBullet.remove(bullet)


    def draw(self):

        for bullet in self.lstBullet:
            bullet.draw(self.gameplayService.screen)