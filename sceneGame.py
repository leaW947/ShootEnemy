import pygame
import bulletManager
import enemyManager
import player
import scrollingBackground
import particleEmitter

class SceneGame:

    def __init__(self):
        self.gameplayService=None
        self.sceneLoader=None
        self.myBulletManager=None
        self.myEnemyManager=None
        self.myParticleEmitter=None

        self.myPlayer=None
        self.myBackground=None

        self.distWithEdge=0
        self.imgEdge=None
        self.textScore=None

        self.timerSpeed=0.5
        self.timerGame=self.timerSpeed

        self.bIsDeadPlayer=False
        self.nbEnemyOnMove=0


    def initGame(self):
        #particleEmitter
        self.myParticleEmitter=particleEmitter.ParticleEmitter(self.gameplayService)

        #projectileManager
        self.myBulletManager = bulletManager.BulletManager(self.gameplayService)

        #enemyManager
        self.myEnemyManager = enemyManager.EnemyManager(self.gameplayService, self.gameplayService.screen.get_width(), 45)
        self.myEnemyManager.addEnemy(5)

        #player
        self.myPlayer=player.Player()
        self.myPlayer.load(self.gameplayService)


        self.imgEdge = self.gameplayService.assetManager.getImage("images/edge.png")
        self.myBackground=scrollingBackground.ScrollingBackground(self.gameplayService)

        font=pygame.font.Font("fonts/Minecraft.ttf",30)
        self.textScore=self.gameplayService.GUI.createText(self.gameplayService.screen.get_width()-200,
                                                            self.gameplayService.screen.get_height()-40,font,
                                                           [0,255,0],"score = 0")

        self.distWithEdge=self.gameplayService.screen.get_width()-self.imgEdge.get_width()
        self.timerGame = self.timerSpeed

        self.bIsDeadPlayer = False
        self.nbEnemyOnMove=0



    def load(self,pGameplayService,pSceneLoader):
        self.gameplayService=pGameplayService
        self.sceneLoader=pSceneLoader

        self.initGame()
        self.gameplayService.score=0


    def update(self,dt):

        self.textScore.text="Score = "+str(self.gameplayService.score)

        for e in range(len(self.myEnemyManager.lstEnemy) - 1, -1, -1):
            enemy=self.myEnemyManager.lstEnemy[e]

            #####++enemy on move######
            if enemy.timer<=0 and enemy.bOnMove:
                if self.nbEnemyOnMove<len(self.myEnemyManager.lstEnemy):
                    enemy.timer=enemy.timerDuration
                    self.nbEnemyOnMove+=1


            #############collide player with enemy######################
            bCollidePlayer=self.gameplayService.utils.checkCollision(self.myPlayer.sprite.x, self.myPlayer.sprite.y,
                                                                     self.myPlayer.sprite.image.get_width(),
                                                                     self.myPlayer.sprite.image.get_height(),
                                                                     enemy.sprite.x, enemy.sprite.y,
                                                                     enemy.sprite.tileSize["x"], enemy.sprite.tileSize["y"])

            if bCollidePlayer and not self.bIsDeadPlayer:
                # gameover
                self.myPlayer.sprite.x = self.myPlayer.oldX
                self.myPlayer.sprite.y = self.myPlayer.oldY

                self.bIsDeadPlayer=True

                #particles
                self.myParticleEmitter.addParticle(70,[11,231,145],
                                                   self.myPlayer.sprite.x+(self.myPlayer.sprite.tileSize["x"]/2),
                                                   self.myPlayer.sprite.y+(self.myPlayer.sprite.tileSize["y"]/2))
                break


            ############collide projectile with enemy#############
            for n in range(len(self.myBulletManager.lstBullet) - 1, -1, -1):
                bullet = self.myBulletManager.lstBullet[n]

                bCollideBalloon = False
                bCollide = False

                # enemy with projectile
                bCollide = self.gameplayService.utils.checkCollision(bullet.x, bullet.y, bullet.width,
                                                                     bullet.height,
                                                                     enemy.sprite.x, enemy.sprite.y,
                                                                     enemy.sprite.tileSize["x"],
                                                                     enemy.sprite.tileSize["y"])

                # balloon with projectile
                if enemy.spriteBalloon != None and enemy.vy > 0:
                    bCollideBalloon = self.gameplayService.utils.checkCollision(bullet.x, bullet.y,
                                                                                bullet.width, bullet.height,
                                                                                enemy.spriteBalloon.x,
                                                                                enemy.spriteBalloon.y,
                                                                                enemy.spriteBalloon.image.get_width(),
                                                                                enemy.spriteBalloon.image.get_height())


                #########collision with enemy##########
                if bCollide:
                    self.gameplayService.assetManager.getSound("sounds/sfx_sounds_impact1.wav")
                    pygame.mixer.music.play()

                    self.myBulletManager.lstBullet.pop(n)

                    ###particles
                    self.myParticleEmitter.addParticle(70, [21, 8, 130],
                                enemy.sprite.x + (enemy.sprite.tileSize["x"] / 2),
                                enemy.sprite.y + (enemy.sprite.tileSize["y"] / 2))

                    self.myEnemyManager.lstEnemy.pop(e)
                    self.gameplayService.score += 1


                #####collision with balloon########
                elif bCollideBalloon:
                    self.gameplayService.assetManager.getSound("sounds/sfx_sounds_impact4.wav")
                    pygame.mixer.music.play()
                    ###particles
                    self.myParticleEmitter.addParticle(25,[255,0,0],enemy.spriteBalloon.x+(enemy.spriteBalloon.image.get_width()/2),
                                                       enemy.spriteBalloon.y+ (enemy.spriteBalloon.image.get_height()/2))

                    self.myBulletManager.lstBullet.pop(n)
                    enemy.spriteBalloon = None


        if self.nbEnemyOnMove==len(self.myEnemyManager.lstEnemy):
            self.myEnemyManager.addEnemy(5)

        #gameover
        if self.bIsDeadPlayer:
            self.timerGame-=0.01

            if self.timerGame<=0:
                self.gameplayService.score=0
                self.sceneLoader.init("gameover")


        if not self.bIsDeadPlayer:
            self.myPlayer.update(dt)

        self.myBulletManager.update(dt)
        self.myEnemyManager.update(dt, self.distWithEdge)
        self.myBackground.update(dt)
        self.myParticleEmitter.update(dt)


    def draw(self):
        self.myBackground.draw()
        self.gameplayService.screen.blit(self.imgEdge,(self.gameplayService.screen.get_width()-self.imgEdge.get_width(),100))

        self.gameplayService.screen.blit(self.imgEdge,(self.gameplayService.screen.get_width() - self.imgEdge.get_width(),
                                                       100+self.gameplayService.screen.get_height()/3))

        self.myBulletManager.draw()

        if not self.bIsDeadPlayer:
            self.myPlayer.draw()

        self.myEnemyManager.draw()
        self.myParticleEmitter.draw()



    def keypressed(self,pKey):

        ####add bullet###############
        if pKey[pygame.K_SPACE]:
            self.gameplayService.assetManager.getSound("sounds/bullet-laser.wav")
            pygame.mixer.music.play()

            self.myBulletManager.addBullet(self.myPlayer.sprite.x + (self.myPlayer.sprite.image.get_width() / 2),
                                               self.myPlayer.sprite.y + (self.myPlayer.sprite.image.get_height()/2), 5, 0)
