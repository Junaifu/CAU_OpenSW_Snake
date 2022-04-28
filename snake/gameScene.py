from sceneBase import SceneBase
from utils import *
from gameMap import GameMap
from inGameMenuScene import InGameMenuScene

class GameScene(SceneBase):
    gameMap = GameMap()

    def __init__(self):
        SceneBase.__init__(self)
        pygame.display.set_caption("Snake")

    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                # Move to in game menu scene when the user presses Escape
                self.SwitchToScene(InGameMenuScene())

    def Update(self):
        # TODO: Game Logique Update
        pass

    def Render(self):
        # TODO: Game Render
        App.screen.fill(pygame.Color("Black"))
        t = Text("Score: 0", (450, 30))
        t.draw()
        self.gameMap.render()
