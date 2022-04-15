from sceneBase import SceneBase
from utils import *
from gameMap import GameMap


class GameScene(SceneBase):
    gameMap = GameMap()

    def __init__(self):
        SceneBase.__init__(self)
        pygame.display.set_caption("Snake")

    def ProcessInput(self, events, pressed_keys):
        # TODO: Game Controller
        pass

    def Update(self):
        # TODO: Game Logique Update
        pass

    def Render(self):
        # TODO: Game Render
        App.screen.fill(pygame.Color(3, 187, 0))
        t = Text("Score: 0", (450, 30))
        t.draw()
        self.gameMap.render()
