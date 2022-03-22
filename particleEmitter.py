import math

import pygame.draw
import random
random.seed(1,10)

class Particle:

    def __init__(self,pX,pY,pColor):
        self.x=pX
        self.y=pY

        angle=random.randint(int(math.pi),int(2*math.pi))

        self.vx=random.randint(-1,1)*math.cos(angle)
        self.vy=random.randint(-1,1)*math.sin(angle)

        self.timerDuration=(random.randint(10,50))/100
        self.timer=self.timerDuration

        self.nbLives=random.randint(1,3)

        self.color=pColor
        self.alpha=1

        self.scale=random.randint(5,7)


    def update(self,dt):
        self.x+=self.vx*60*dt
        self.y+=self.vy*60*dt

        self.timer -= 0.01


    def draw(self,pScreen):
        self.alpha=self.timer/self.timerDuration

        pygame.draw.rect(pScreen,(self.color[0],self.color[1],self.color[2]),(self.x,self.y,self.scale,self.scale))




class ParticleEmitter:

    def __init__(self,pGameplayService):
        self.gameplayService = pGameplayService

        self.lstParticles=[]
        self.x=0
        self.y=0


    def addParticle(self,pNbParticles,pColor,pX,pY):

        self.x=pX
        self.y=pY

        for i in range(1,pNbParticles):
            particle=Particle(self.x+random.randint(-10,10),self.y+random.randint(-10,10),pColor)

            self.lstParticles.append(particle)


    def update(self,dt):

        for p in range(len(self.lstParticles)-1,-1,-1):
            particle=self.lstParticles[p]
            particle.update(dt)

            if particle.timer<=0:
                self.lstParticles.pop(p)


    def draw(self):

        for particle in self.lstParticles:
            particle.draw(self.gameplayService.screen)