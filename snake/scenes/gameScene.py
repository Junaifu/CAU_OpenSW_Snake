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
            self.AutoMode()
        if self.gameMode == GameMode.DUAL:
            print("Dual")

    def Update(self):
        isOnApple = self.gameMap.snake.move(self.gameMap.appleX, self.gameMap.appleY)
        if isOnApple == True:
            self.score += 10
        if self.gameMap.checkCollision() == True:
            self.gameMap.render()
            self.SwitchToScene(GameOverScene(self.gameMode, self.score))
        # if self.gameMode == GameMode.DUAL:
        #     print("Dual")


    def Render(self):
        App.screen.fill(pygame.Color("Black"))
        if self.gameMode != GameMode.DUAL:
            t = Text("Score: " + str(self.score), (400, 30))
            t.draw()
        self.gameMap.render()
        # if self.gameMode == GameMode.DUAL:
        #     print("Dual")

    def AutoMode(self):
        snake = self.gameMap.snake
        snakeX = self.gameMap.snake.x
        snakeY = self.gameMap.snake.y
        # westMove = (snakeX - 1, snakeY)
        # eastMove = (snakeX + 1, snakeY)
        # northMove = (snakeX, snakeY - 1)
        # southMove = (snakeX, snakeY + 1)

        if snakeX > self.gameMap.appleX and snake.direction != Direction.EAST:
            snake.changeDirection(Direction.WEST)
        if snakeX < self.gameMap.appleX and snake.direction != Direction.WEST:
            snake.changeDirection(Direction.EAST)
        if snakeY > self.gameMap.appleY and snake.direction != Direction.SOUTH:
            snake.changeDirection(Direction.NORTH)
        if snakeY < self.gameMap.appleY and snake.direction != Direction.NORTH:
            snake.changeDirection(Direction.SOUTH)

    ## too instable algo

        # if snakeX > self.gameMap.appleX and snake.direction != Direction.EAST and snake.bodyParts.count(westMove) == 0:
        #     snake.changeDirection(Direction.WEST)
        # if snakeX < self.gameMap.appleX and snake.direction != Direction.WEST and snake.bodyParts.count(eastMove) == 0:
        #     snake.changeDirection(Direction.EAST)
        # else: #when snakeX == appleX
        #     if snakeY > self.gameMap.appleY and snake.bodyParts.count(northMove) == 0:
        #         snake.changeDirection(Direction.NORTH)
        #     else:
        #         snake.changeDirection(Direction.SOUTH)
        # if snakeY > self.gameMap.appleY and snake.direction != Direction.SOUTH and snake.bodyParts.count(northMove) == 0:
        #     snake.changeDirection(Direction.NORTH)
        # elif snakeY < self.gameMap.appleY and snake.direction != Direction.NORTH and snake.bodyParts.count(southMove) == 0:
        #     snake.changeDirection(Direction.SOUTH)
        # else:
        #     if snakeX > self.gameMap.appleX  and snake.bodyParts.count(westMove) == 0:
        #         snake.changeDirection(Direction.WEST)
        #     else:
        #         snake.changeDirection(Direction.EAST)