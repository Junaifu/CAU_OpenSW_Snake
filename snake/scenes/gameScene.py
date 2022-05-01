from scenes.sceneBase import *
from utils.text import Text
from gameMap import GameMap
from scenes.inGameMenuScene import InGameMenuScene
from snakeBody import Direction
from scenes.gameOverScene import GameOverScene


class GameScene(SceneBase):
    gameMap = None
    score = 0

    def __init__(self, score = 0, map = None):
        SceneBase.__init__(self)
        pygame.display.set_caption("Snake")
        self.score = score
        self.gameMap = map if map else GameMap()

    def ProcessInput(self, events, pressed_keys):
        if pressed_keys[pygame.K_ESCAPE]:
            # Move to in game menu scene when the user presses Escape
            self.SwitchToScene(InGameMenuScene(self.gameMap, self.score))
            # Pause the game
            App.isPaused = True
        elif pressed_keys[pygame.K_LEFT]:
            self.gameMap.snake.changeDirection(Direction.WEST)
        elif pressed_keys[pygame.K_RIGHT]:
            self.gameMap.snake.changeDirection(Direction.EAST)
        elif pressed_keys[pygame.K_UP]:
            self.gameMap.snake.changeDirection(Direction.NORTH)
        elif pressed_keys[pygame.K_DOWN]:
            self.gameMap.snake.changeDirection(Direction.SOUTH)

    def Update(self):
        isOnApple = self.gameMap.snake.move(self.gameMap.appleX, self.gameMap.appleY)
        if isOnApple == True:
            self.score += 10
        if self.gameMap.checkCollision() == True:
            self.gameMap.render()
            self.SwitchToScene(GameOverScene(self.score))

    def Render(self):
        # TODO: Game Render
        App.screen.fill(pygame.Color("Black"))
        t = Text("Score: " + str(self.score), (450, 30))
        t.draw()
        self.gameMap.render()
