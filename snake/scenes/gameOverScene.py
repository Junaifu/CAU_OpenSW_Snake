from scenes.sceneBase import *
import scenes
from utils.text import Text
from utils.textInput import TextInput
from utils.button import Button
import pygame


class GameOverScene(SceneBase):
    score = 0
    textInput = None
    mainMenuButton = None

    def __init__(self, score):
        SceneBase.__init__(self)
        pygame.display.set_caption("Game Over")
        self.score = score
        self.textInput = TextInput(340, 400, (430, 70))
        self.mainMenuButton = Button(
            "BACK TO MAIN MENU", App.screenSizeX / 2, 600, self.mainMenuCallback)
    
    def mainMenuCallback(self, params):
        self.SwitchToScene(scenes.menuScene.MenuScene())

    def ProcessInput(self, events, pressed_keys):
        for event in events:
            self.textInput.ProcessInput(event, pressed_keys)
            self.textInput.event(event)
            self.mainMenuButton.event(event)

    def Update(self):
        pass

    def Render(self):
        App.screen.fill(pygame.Color("Red"))
        t = Text("Game Over", (350, 100))
        t.draw()
        scoreText = Text("Your score: " + str(self.score), (270, 200))
        scoreText.draw()
        playerNameText = Text("Enter your name:", (200, 300))
        playerNameText.draw()
        self.textInput.draw()
        self.mainMenuButton.draw()
