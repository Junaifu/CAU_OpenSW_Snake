from scenes.sceneBase import *
from utils.text import Text
from gameMap import GameMap
from scenes.inGameMenuScene import InGameMenuScene
from snakeBody import Direction
from scenes.gameOverScene import GameOverScene
from enums import GameMode

class GameScene(SceneBase):
    gameMap = None
    score = 0
    gameMode = None

    def __init__(self, gameMode, score = 0, map = None):
        self.gameMode = gameMode
        SceneBase.__init__(self)
        pygame.display.set_caption("Snake")
        App.fps = 80
        self.score = score
        self.gameMap = map if map else GameMap()

    def loadGameScene(self, gameMap, score):
        self.gameMap = gameMap
        self.score = score

    def ProcessInput(self, events, pressed_keys):
        if pressed_keys[pygame.K_ESCAPE]:
            # Move to in game menu scene when the user presses Escape
            self.SwitchToScene(InGameMenuScene(self.gameMap, self.score))
            # Pause the game
            App.isPaused = True
        if self.gameMode == GameMode.SINGLE:
            if pressed_keys[pygame.K_LEFT]:
                self.gameMap.snake.changeDirection(Direction.WEST)
            elif pressed_keys[pygame.K_RIGHT]:
                self.gameMap.snake.changeDirection(Direction.EAST)
            elif pressed_keys[pygame.K_UP]:
                self.gameMap.snake.changeDirection(Direction.NORTH)
            elif pressed_keys[pygame.K_DOWN]:
                self.gameMap.snake.changeDirection(Direction.SOUTH)
        if self.gameMode == GameMode.AUTO:
            print("Auto")
        if self.gameMode == GameMode.DUAL:
            print("Dual")

    def Update(self):
        if self.gameMode == GameMode.SINGLE:
            isOnApple = self.gameMap.snake.move(self.gameMap.appleX, self.gameMap.appleY)
            if isOnApple == True:
                self.score += 10
            if self.gameMap.checkCollision() == True:
                self.gameMap.render()
                self.SwitchToScene(GameOverScene(self.score))
        if self.gameMode == GameMode.AUTO:
            print("Auto")
        if self.gameMode == GameMode.DUAL:
            print("Dual")


    def Render(self):
        App.screen.fill(pygame.Color("Black"))
        if self.gameMode == GameMode.SINGLE:
            t = Text("Score: " + str(self.score), (400, 30))
            t.draw()
            self.gameMap.render()
        if self.gameMode == GameMode.AUTO:
            print("Auto")
        if self.gameMode == GameMode.DUAL:
            print("Dual")
