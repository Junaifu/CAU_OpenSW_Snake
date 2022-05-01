from scenes.sceneBase import *
import scenes
from utils.text import Text
from utils.textInput import TextInput
from utils.button import Button
import pygame


class GameOverScene(SceneBase):
    score = 0
    textInput = None
    playAgainButton = None
    mainMenuButton = None

    background = pygame.image.load('resources/bg.png')
    stars = pygame.image.load('resources/Stars Small_1.png')
    stars2 = pygame.image.load('resources/Stars-Big_1_1_PC.png')
    firstStarsIndex = 0
    secondStarsIndex = 0

    def __init__(self, score):
        SceneBase.__init__(self)
        pygame.display.set_caption("Game Over")
        self.score = score
        self.textInput = TextInput(340, 400, (430, 70))
        self.mainMenuButton = Button(
            "BACK TO MAIN MENU", 340, 600, self.mainMenuCallback)
        self.playAgainButton = Button(
            "PLAY AGAIN", 420, 550, self.playAgainCallback)
        self.background = pygame.transform.scale(
            self.background, (App.screenSizeX, App.screenSizeY))
        self.stars = pygame.transform.scale(
            self.stars, (App.screenSizeX, App.screenSizeY))
        self.stars2 = pygame.transform.scale(
            self.stars2, (App.screenSizeX, App.screenSizeY))
        self.firstStarsIndex = -App.screenSizeY
        self.secondStarsIndex = -App.screenSizeY

    def mainMenuCallback(self, params):
        self.SwitchToScene(scenes.menuScene.MenuScene())
        # TODO ranking
    
    def playAgainCallback(self, params):
        self.SwitchToScene(scenes.gameScene.GameScene())

    def ProcessInput(self, events, pressed_keys):
        for event in events:
            self.textInput.ProcessInput(event, pressed_keys)
            self.textInput.event(event)
            self.mainMenuButton.event(event)
            self.playAgainButton.event(event)

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
        t = Text("Game Over", (350, 100))
        t.draw()
        scoreText = Text("Your score: " + str(self.score), (270, 200))
        scoreText.draw()
        playerNameText = Text("Enter your name:", (200, 300))
        playerNameText.draw()
        self.textInput.draw()
        self.mainMenuButton.draw()
        self.playAgainButton.draw()
