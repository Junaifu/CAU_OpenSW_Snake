from scenes.sceneBase import SceneBase
from scenes.saveScene import SaveScene
from scenes.gameScene import GameScene
from scenes.rankingScene import RankingScene
from utils.button import Button
from utils.text import Text
from app import App
from enums import GameMode

import pygame

class MenuScene(SceneBase):
    background = pygame.image.load('resources/bg.png')
    stars = pygame.image.load('resources/Stars Small_1.png')
    stars2 = pygame.image.load('resources/Stars-Big_1_1_PC.png')
    firstStarsIndex = 0
    secondStarsIndex = 0

    singlePlayButton = None
    dualPlayButton = None
    autoPlayButton = None
    loadButton = None
    rankingButton = None
    exitButton = None

    def __init__(self):
        SceneBase.__init__(self)
        pygame.display.set_caption("Menu")
        if (App.screenSizeX != None):
            self.initMenu()

    def playButtonCallback(self, params):
        self.SwitchToScene(GameScene(params[0]))

    # TODO: redirect to LoadFiles screen
    def loadButtonCallback(self, params):
        self.SwitchToScene(SaveScene())

    def initMenu(self):
        self.background = pygame.transform.scale(
            self.background, (App.screenSizeX, App.screenSizeY))
        self.stars = pygame.transform.scale(
            self.stars, (App.screenSizeX, App.screenSizeY))
        self.stars2 = pygame.transform.scale(
            self.stars2, (App.screenSizeX, App.screenSizeY))
        self.firstStarsIndex = -App.screenSizeY
        self.secondStarsIndex = -App.screenSizeY
        self.singlePlayButton = Button(
            "SINGLE PLAY", App.screenSizeX / 2, 150, self.playButtonCallback, GameMode.SINGLE)
        self.dualPlayButton = Button(
            "DUAL PLAY", App.screenSizeX / 2, 200, self.playButtonCallback, GameMode.DUAL)
        self.autoPlayButton = Button(
            "AUTO PLAY", App.screenSizeX / 2, 250, self.playButtonCallback, GameMode.AUTO)
        self.loadButton = Button(
            "LOAD", App.screenSizeX / 2, 300, self.loadButtonCallback)
        self.rankingButton = Button(
            "RANKING", App.screenSizeX / 2, 350, lambda x: self.SwitchToScene(RankingScene()))
        self.exitButton = Button(
            "EXIT", App.screenSizeX / 2, 400, (lambda params: self.Terminate()))

    def ProcessInput(self, events, pressed_keys):
        for event in events:
            self.singlePlayButton.event(event)
            self.dualPlayButton.event(event)
            self.autoPlayButton.event(event)
            self.loadButton.event(event)
            self.rankingButton.event(event)
            self.exitButton.event(event)

    def Update(self):
        if (self.firstStarsIndex >= 0):
            App.screen.blit(
                self.stars, (0, App.screenSizeY + self.firstStarsIndex))
            self.firstStarsIndex = -App.screenSizeY
        self.firstStarsIndex += 2

        if (self.secondStarsIndex >= 0):
            App.screen.blit(
                self.stars2, (0, App.screenSizeY + self.secondStarsIndex))
            self.secondStarsIndex = -App.screenSizeY
        self.secondStarsIndex += 1

    def Render(self):
        App.screen.blit(self.background, (0, 0))
        App.screen.blit(self.stars, (0, self.firstStarsIndex))
        App.screen.blit(
            self.stars, (0, App.screenSizeY + self.firstStarsIndex))
        App.screen.blit(self.stars2, (0, self.secondStarsIndex))
        App.screen.blit(
            self.stars2, (0, App.screenSizeY + self.secondStarsIndex))
        t = Text("Menu", (150, 150))
        t.draw()
        self.singlePlayButton.draw()
        self.dualPlayButton.draw()
        self.autoPlayButton.draw()
        self.loadButton.draw()
        self.rankingButton.draw()
        self.exitButton.draw()
