import math

class Sprite:

    def __init__(self,pImg,pX,pY):

        self.image=pImg

        self.x=pX
        self.y=pY

        self.currentFrame=0
        self.currentFrameInAnimation=0

        self.timerFrame=0

        self.lstAnimations=[]
        self.currentAnimation=None

        self.bIsTilesheet=False
        self.tileSize={"x":0,"y":0}


    def setTilesheet(self,pWFrame,pHFrame):
        self.bIsTilesheet=True

        self.tileSize["x"]=pWFrame
        self.tileSize["y"]=pHFrame


    def addAnimation(self,pName,pLstFrames,pSpeed,pbLoop):
        animation={
            "name":pName,
            "lstFrames":pLstFrames,
            "speed":pSpeed,
            "bLoop":pbLoop,
            "bIsFinish":False
        }

        self.lstAnimations.append(animation)


    def startAnimation(self,pName):

        if self.currentAnimation!=None:
            if self.currentAnimation["name"]==pName:
                return


        for animation in self.lstAnimations:

            if animation["name"]==pName:

                self.currentAnimation=animation
                self.currentFrameInAnimation=0
                self.currentFrame=self.currentAnimation["lstFrames"].index(self.currentFrameInAnimation)
                self.currentAnimation["bIsFinish"]=False


    def update(self,dt):

        if self.currentAnimation!=None:

            self.timerFrame+=dt

            if self.timerFrame>=self.currentAnimation["speed"]:
                self.timerFrame=0
                self.currentFrameInAnimation+=1

                if self.currentFrameInAnimation>len(self.currentAnimation["lstFrames"])-1:

                    if self.currentAnimation["bLoop"]:
                        self.currentFrameInAnimation=0
                    else:
                        self.currentFrameInAnimation=len(self.currentAnimation["lstFrames"])-1
                        self.currentAnimation["bIsFinish"]=True

                self.currentFrame=self.currentAnimation["lstFrames"].index(self.currentFrameInAnimation)



    def draw(self,pScreen):

        if not self.bIsTilesheet:
            pScreen.blit(self.image,(self.x,self.y))

        elif self.bIsTilesheet:
            nbCol=self.image.get_width()/self.tileSize["x"]

            l=math.floor(self.currentFrame/nbCol)
            c=math.floor(self.currentFrame-(l*nbCol))

            x=c*self.tileSize["x"]
            y=l*self.tileSize["y"]

            pScreen.blit(self.image,(self.x,self.y),(x,y,self.tileSize["x"],self.tileSize["y"]))
