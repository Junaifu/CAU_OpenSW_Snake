from sceneBase import SceneBase
from utils import *
from gameMap import GameMap


class InGameMenuScene(SceneBase):
    gameMap = GameMap()

    def __init__(self):
        SceneBase.__init__(self)
        pygame.display.set_caption("Snake in-game menu")

    def ProcessInput(self, events, pressed_keys):
        # TODO: Game Controller
        pass

    def Update(self):
        # TODO: Game Logique Update
        pass

    def Render(self):
        App.screen.fill(pygame.Color("Black"))
