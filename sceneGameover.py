import pygame.font
import sprite

class SceneGameover:

    def __init__(self):
        self.gameplayService=None
        self.sceneLoader=None

        self.button=None
        self.lstChar=[]

        self.timerDuration=0.2
        self.timer=self.timerDuration

        self.tweening={}

        self.lstSprEnemy=[]


    def load(self,pGameplayService,pSceneLoader):
        self.gameplayService=pGameplayService
        self.sceneLoader=pSceneLoader

        #text
        font=pygame.font.Font("fonts/Minecraft.ttf",70)

        for i in range(0,8):
            text="GAMEOVER"

            char={
                "text":self.gameplayService.GUI.createText(self.gameplayService.screen.get_width()/5+(i*60),
                                                     0-200,
                                                     font,[255,0,0],text[i]),

                "tweening":{
                    "time":0,
                    "begin":0-200,
                    "distance":self.gameplayService.screen.get_height()/1.8,
                    "duration":0.8+(0.3*i)
                }
            }

            self.lstChar.append(char)


        ######button#########
        self.button=self.gameplayService.GUI.createButton((self.gameplayService.screen.get_width()/2),
                                                      self.gameplayService.screen.get_height()/1.7)

        self.button.addImages(self.gameplayService.assetManager.getImage("images/btnGameoverNormal.png"),
                              self.gameplayService.assetManager.getImage("images/btnGameoverHover.png"),
                              self.gameplayService.assetManager.getImage("images/btnGameoverPressed.png"))

        self.button.x=(self.gameplayService.screen.get_width()/2)-self.button.width/2

        #enemy
        x=0
        y=100
        for i in range(0,10):

            sprEnemy = sprite.Sprite(self.gameplayService.assetManager.getImage("images/gameoverEnemy.png"), 0, 0)
            sprEnemy.x=x
            sprEnemy.y=y

            if y < self.gameplayService.screen.get_height()-100:
                y = y + 100
            else:
                y = 100
                x = self.gameplayService.screen.get_width() - sprEnemy.image.get_width()

            self.lstSprEnemy.append(sprEnemy)


        #######music
        self.gameplayService.assetManager.getSound("sounds/musics/tetris-gameboy-04.mp3")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.2)


    def update(self,dt):

        ##tweening text
        for i in range(len(self.lstChar)-1,-1,-1):
            char=self.lstChar[i]

            tween=self.gameplayService.utils.easeInSine(char["tweening"]["time"],char["tweening"]["begin"],
                                                        char["tweening"]["distance"],char["tweening"]["duration"])

            char["text"].y=tween

            char["tweening"]["time"]+=dt
            if char["tweening"]["time"]>=char["tweening"]["duration"]:
                char["tweening"]["time"]=char["tweening"]["duration"]


        ##########button pressed#########
        if self.button.bIsPressed:
            self.timer-=dt

            if self.timer<=0:
                pygame.mixer.music.stop()

                self.gameplayService.assetManager.getSound("sounds/sfx_sounds_button6.wav")
                pygame.mixer.music.play()

                self.sceneLoader.init("gameplay")



    def draw(self):
        for enemy in self.lstSprEnemy:
            enemy.draw(self.gameplayService.screen)