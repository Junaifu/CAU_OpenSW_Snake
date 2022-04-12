from sceneBase import SceneBase
from utils import *


class GameScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
        pygame.display.set_caption("Snake")

    def ProcessInput(self, events, pressed_keys):
        # TODO: Game Controller
        pass

    def Update(self):
        # TODO: Game Logique Update
        pass

    def Render(self, screen):
        # TODO: Game Render
        screen.fill(pygame.Color("Blue"))
        t = Text("Game", (150, 150))
        t.draw()
