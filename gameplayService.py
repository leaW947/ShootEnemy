class GameplayService:

    def __init__(self):
        self.screen=None
        self.assetManager=None
        self.utils=None
        self.GUI=None

        self.score=0


    def setScreen(self,pScreen):
        self.screen=pScreen


    def setAssetManager(self,pAssetManager):
        self.assetManager=pAssetManager


    def setUtils(self,pUtils):
        self.utils=pUtils


    def setGUI(self,pGUI):
        self.GUI=pGUI

