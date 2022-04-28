import pygame
from app import App
from sceneBase import SceneBase
from gameScene import GameScene
from utils import Text

class MenuScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
        pygame.display.set_caption("Menu")

    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                # Move to the next scene when the user pressed Enter
                self.SwitchToScene(GameScene())

    def Update(self):
        pass

    def Render(self):
        App.screen.fill(pygame.Color("Red"))
        t = Text("Menu", (150, 150))
        t.draw()
