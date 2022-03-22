import pygame.font

import assetManager
import utils
import GUIManager
import gameplayService

import sceneGame
import sceneGameover

class SceneLoader:

    def __init__(self):
        self.gameState=""

        self.myAssetManager = None
        self.myUtils=None
        self.myGUI=None
        self.myGameplayService = None

        self.mySceneGame=sceneGame.SceneGame()
        self.mySceneGameover=sceneGameover.SceneGameover()


    def load(self,pScreen):
        self.myAssetManager=assetManager.AssetManager()
        self.myUtils=utils.Utils()
        self.myGameplayService=gameplayService.GameplayService()
        self.myGUI=GUIManager.GUI()

        self.myAssetManager.addImage("images/balloon.png")
        self.myAssetManager.addImage("images/enemy.png")
        self.myAssetManager.addImage("images/player.png")
        self.myAssetManager.addImage("images/background.jpg")
        self.myAssetManager.addImage("images/background_stars.png")
        self.myAssetManager.addImage("images/edge.png")

        self.myAssetManager.addImage("images/btnGameoverNormal.png")
        self.myAssetManager.addImage("images/btnGameoverHover.png")
        self.myAssetManager.addImage("images/btnGameoverPressed.png")

        self.myAssetManager.addImage("images/gameoverEnemy.png")

        self.myAssetManager.addSound("sounds/sfx_sounds_button6.wav")
        self.myAssetManager.addSound("sounds/sfx_sounds_impact1.wav")
        self.myAssetManager.addSound("sounds/sfx_sounds_impact4.wav")
        self.myAssetManager.addSound("sounds/bullet-laser.wav")
        self.myAssetManager.addSound("sounds/musics/tetris-gameboy-04.mp3")

        self.myGameplayService.setScreen(pScreen)
        self.myGameplayService.setUtils(self.myUtils)
        self.myGameplayService.setAssetManager(self.myAssetManager)
        self.myGameplayService.setGUI(self.myGUI)


    def init(self,pGameState):
        self.gameState=pGameState
        self.myGameplayService.GUI.totalDelete()

        if self.gameState=="menu":
            print("loadMenu")
        elif self.gameState=="gameplay":
            self.mySceneGame.load(self.myGameplayService, self)
        elif self.gameState=="gameover":
            self.mySceneGameover.load(self.myGameplayService, self)


    def update(self,dt):

        if self.gameState == "gameplay":
            self.mySceneGame.update(dt)

        elif self.gameState == "gameover":
            self.mySceneGameover.update(dt)

        self.myGameplayService.GUI.update(dt)


    def draw(self):

        if self.gameState == "gameplay":
            self.mySceneGame.draw()

        elif self.gameState == "gameover":
            self.mySceneGameover.draw()

        self.myGameplayService.GUI.draw(self.myGameplayService.screen)


    def keypressed(self,pKey):

        if self.gameState == "gameplay":
            self.mySceneGame.keypressed(pKey)


    def mousepressed(self,pBtn,pPos):
        self.myGameplayService.GUI.mousepressed(pBtn,pPos)


    def mousemove(self,pPos):
        self.myGameplayService.GUI.mousemove(pPos)