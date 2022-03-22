class ScrollingBackground:

    def __init__(self,pGameplayService):
        self.gameplayService=pGameplayService
        self.x=0
        self.y=0
        self.speed=-3
        self.img=self.gameplayService.assetManager.getImage("images/background_stars.png")


    def update(self,dt):
        self.x+=self.speed

        if self.x<0-self.img.get_width():
            self.x=0


    def draw(self):
        self.gameplayService.screen.blit(self.img,(self.x,self.y))
        self.gameplayService.screen.blit(self.img, (self.x+self.img.get_width(), self.y))