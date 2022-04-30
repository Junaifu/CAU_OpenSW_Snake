from scenes.sceneBase import SceneBase
from scenes.gameScene import GameScene
from utils.button import Button
from utils.text import Text
from app import App
import pygame


def test():
    print("GHello")


class MenuScene(SceneBase):
    background = pygame.image.load('../resources/bg.png')
    stars = pygame.image.load('../resources/Stars Small_1.png')
    stars2 = pygame.image.load('../resources/Stars-Big_1_1_PC.png')
    firstStarsIndex = 0
    secondStarsIndex = 0
    height = 0

    playButton = None
    loadButton = None
    rankingButton = None
    exitButton = None
    hello_button = None

    def __init__(self):
        SceneBase.__init__(self)
        pygame.display.set_caption("Menu")

    def playButtonCallback(self, params):
        self.SwitchToScene(GameScene())

    def loadButtonCallback(self, params):
        self.SwitchToScene(GameScene())

    def initMenu(self):
        self.height = App.screenSizeY
        self.background = pygame.transform.scale(
            self.background, (App.screenSizeX, App.screenSizeY))
        self.stars = pygame.transform.scale(
            self.stars, (App.screenSizeX, self.height))
        self.stars2 = pygame.transform.scale(
            self.stars2, (App.screenSizeX, self.height))
        self.firstStarsIndex = -720
        self.secondStarsIndex = -720
        self.playButton = Button(
            "PLAY", App.screenSizeX / 2, 150, self.playButtonCallback)
        self.loadButton = Button(
            "LOAD", App.screenSizeX / 2, 250, self.loadButtonCallback)
        self.rankingButton = Button(
            "RANKING", App.screenSizeX / 2, 350, lambda x: print("Hello"))
        self.exitButton = Button(
            "EXIT", App.screenSizeX / 2, 450, (lambda params: self.Terminate()))

    def ProcessInput(self, events, pressed_keys):
        for event in events:
            self.playButton.event(event)
            self.loadButton.event(event)
            self.rankingButton.event(event)
            self.exitButton.event(event)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                # Move to the next scene when the user pressed Enter
                self.SwitchToScene(GameScene())

    def Update(self):
        if (self.firstStarsIndex >= 0):
            App.screen.blit(
                self.stars, (0, self.height + self.firstStarsIndex))
            self.firstStarsIndex = -720
        self.firstStarsIndex += 2

        if (self.secondStarsIndex >= 0):
            App.screen.blit(
                self.stars2, (0, self.height + self.secondStarsIndex))
            self.secondStarsIndex = -720
        self.secondStarsIndex += 1
        pass

    def Render(self):
        App.screen.blit(self.background, (0, 0))
        App.screen.blit(self.stars, (0, self.firstStarsIndex))
        App.screen.blit(self.stars, (0, self.height + self.firstStarsIndex))
        App.screen.blit(self.stars2, (0, self.secondStarsIndex))
        App.screen.blit(self.stars2, (0, self.height + self.secondStarsIndex))
        t = Text("Menu", (150, 150))
        t.draw()
        self.playButton.show()
        self.loadButton.show()
        self.rankingButton.show()
        self.exitButton.show()
