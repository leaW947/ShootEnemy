
import random
import sprite

#############################CLASS ENEMY###########################
class Enemy:

    def __init__(self,pSprite,pSpriteBalloon,pId,pDuration):

        self.vx=0
        self.vy=0

        self.sprite=pSprite
        self.spriteBalloon=pSpriteBalloon

        self.timerDuration=0

        if pId>0:
            self.timerDuration=pDuration
        else:
            self.timerDuration=0.5

        self.timer=self.timerDuration

        self.bOnMove=False
        self.bOnStop=False

        self.id=pId


    def update(self,dt):

        self.sprite.x+=self.vx
        self.sprite.y+=self.vy

        if self.spriteBalloon!=None:
            self.spriteBalloon.x=self.sprite.x
            self.spriteBalloon.y=self.sprite.y-(self.spriteBalloon.image.get_height()/1.2)


        if self.timer<=0:
            self.bOnMove=True


        self.sprite.update(dt)


    def draw(self,pScreen):

        if self.vy>0 and self.spriteBalloon!=None:
            self.spriteBalloon.draw(pScreen)

        self.sprite.draw(pScreen)



################CLASS ENEMY MANAGER###########################
class EnemyManager:

    def __init__(self,pGameplayService,pX,pY):
        self.gameplayService=pGameplayService

        self.x=pX
        self.y=pY

        self.lstEnemy=[]
        self.nbEnemyStop=0
        self.duration=2.5


    def addEnemy(self,pNbEnemy):

        #init enemy
        for i in range(0,pNbEnemy):

            rnd=random.randint(1,2)
            y=0

            if rnd==1:
                y=self.y
            else:
                y=self.y+self.gameplayService.screen.get_height()/3

            #sprite init
            spriteEnemy=sprite.Sprite(self.gameplayService.assetManager.getImage("images/enemy.png"),self.x,y)
            spriteEnemy.setTilesheet(64, 54)
            spriteEnemy.addAnimation("move", [0, 1, 2], 0.1, True)
            spriteEnemy.addAnimation("idle", [0], 0, False)
            spriteEnemy.startAnimation("move")

            spriteEnemy.x += (i * spriteEnemy.tileSize["x"])

            imgBalloon=self.gameplayService.assetManager.getImage("images/balloon.png")
            spriteBalloon=sprite.Sprite(imgBalloon,spriteEnemy.x,spriteEnemy.y-(imgBalloon.get_height()/1.2))


            enemy = Enemy(spriteEnemy, spriteBalloon, len(self.lstEnemy),self.duration)
            self.lstEnemy.append(enemy)

        if self.duration > 1:
            self.duration -= 0.5


    def update(self,dt,pDistWithEdge):

        for i in range(len(self.lstEnemy)-1,-1,-1):
            enemy=self.lstEnemy[i]
            
            enemy.update(dt)

            ###TIMER ENEMY
            if i>0:

                if self.lstEnemy[i-1]!=None:
                    if self.lstEnemy[i-1].bOnMove and enemy.timer>-1:
                        enemy.timer-=0.01

                else:
                    if enemy.timer>-1:
                        enemy.timer -= 0.01

            else:
                if not enemy.bOnMove and enemy.timer>-1:
                    enemy.timer-=0.01





            ##########MOVE ENEMY#############
            if enemy.bOnMove and not enemy.bOnStop:

                if enemy.sprite.y+enemy.sprite.tileSize["y"]<self.gameplayService.screen.get_height():

                    #move to the edge
                    if pDistWithEdge-(enemy.sprite.tileSize["x"]*1.5)<enemy.sprite.x:
                        enemy.vx=-2
                        enemy.sprite.startAnimation("move")

                    #move down
                    elif pDistWithEdge-(enemy.sprite.tileSize["x"]*1.5)>=enemy.sprite.x:
                        enemy.vx = 0
                        enemy.sprite.startAnimation("idle")

                        #Balloon?
                        if enemy.spriteBalloon!=None:
                            enemy.vy=1
                        else:
                            enemy.vy=5



                else:
                    ########collide with edge left screen
                    colEdgeLeftScreen=0

                    if enemy.id>0:
                        colEdgeLeftScreen=0+enemy.sprite.tileSize["x"]
                    else:
                        colEdgeLeftScreen=0

                    if enemy.sprite.x>colEdgeLeftScreen:
                        #touch down
                        enemy.sprite.y=self.gameplayService.screen.get_height()-enemy.sprite.tileSize["y"]

                        enemy.vx=-1
                        enemy.vy=0
                        enemy.sprite.startAnimation("move")

                    else:
                       if enemy.vx!=0 or enemy.vy!=0:
                            #####STOP enemy###########
                            enemy.sprite.x=0
                            enemy.sprite.y=enemy.sprite.y-(self.nbEnemyStop*enemy.sprite.tileSize["y"])

                            enemy.vx=0
                            enemy.vy=0

                            self.nbEnemyStop+=1
                            enemy.sprite.startAnimation("idle")
                            enemy.bOnStop=True


    def draw(self):

        for enemy in self.lstEnemy:
            enemy.draw(self.gameplayService.screen)
