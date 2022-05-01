from scenes.sceneBase import *
from utils.text import Text
import pygame


class GameOverScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
        pygame.display.set_caption("Game Over")

    def ProcessInput(self, events, pressed_keys):
        pass

    def Update(self):
        pass

    def Render(self):
        App.screen.fill(pygame.Color("Red"))
        t = Text("Game Over", (150, 150))
        t.draw()
