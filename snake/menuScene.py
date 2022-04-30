from sceneBase import SceneBase
from gameScene import GameScene
from cursor import Cursor
from utils import *
import pygame


class MenuScene(SceneBase):
    c = Cursor()
    background = pygame.image.load('../resources/bg.png')
    stars = pygame.image.load('../resources/Stars Small_1.png')
    stars2 = pygame.image.load('../resources/Stars-Big_1_1_PC.png')
    firstStarsIndex = 0
    secondStarsIndex = 0
    height = 0
    def __init__(self):
        SceneBase.__init__(self)
        pygame.display.set_caption("Menu")
        # c = Cursor()

    def initMenu(self):
        self.height = App.screenSizeY
        self.background = pygame.transform.scale(self.background, (App.screenSizeX, App.screenSizeY))
        self.stars = pygame.transform.scale(self.stars, (App.screenSizeX, self.height))
        self.stars2 = pygame.transform.scale(self.stars2, (App.screenSizeX, self.height))
        self.firstStarsIndex = -720
        self.secondStarsIndex = -720

    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                # Move to the next scene when the user pressed Enter
                self.SwitchToScene(GameScene())

    def Update(self):
        if (self.firstStarsIndex >= 0):
            App.screen.blit(self.stars, (0, self.height + self.firstStarsIndex))
            self.firstStarsIndex = -720
        self.firstStarsIndex += 2

        if (self.secondStarsIndex >= 0):
            App.screen.blit(self.stars2, (0, self.height + self.secondStarsIndex))
            self.secondStarsIndex = -720
        self.secondStarsIndex += 1
        pass

    def Render(self):
        App.screen.blit(self.background, (0,0))
        App.screen.blit(self.stars, (0, self.firstStarsIndex))
        App.screen.blit(self.stars, (0, self.height + self.firstStarsIndex))
        App.screen.blit(self.stars2, (0, self.secondStarsIndex))
        App.screen.blit(self.stars2, (0, self.height + self.secondStarsIndex))
        t = Text("Menu", (150, 150))
        self.c.draw()
        t.draw()
