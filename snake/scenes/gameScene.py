from scenes.sceneBase import *
from utils.text import Text
from gameMap import GameMap, SnakePlayer
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
        self.gameMap = map if map else GameMap(gameMode)

    def loadGameScene(self, gameMap, score):
        self.gameMap = gameMap
        self.score = score

    def ProcessInput(self, events, pressed_keys):
        if pressed_keys[pygame.K_ESCAPE]:
            # Move to in game menu scene when the user presses Escape
            self.SwitchToScene(InGameMenuScene(self.gameMap, self.score, self.gameMode))
            # Pause the game
            App.isPaused = True
        if self.gameMode == GameMode.SINGLE:
            self.gameMap.snakes[SnakePlayer.FIRST].handleInputs(pressed_keys, [pygame.K_UP, pygame.K_DOWN, pygame.K_RIGHT, pygame.K_LEFT])
        if self.gameMode == GameMode.AUTO:
            print("Auto")
        if self.gameMode == GameMode.DUAL:
            self.gameMap.snakes[SnakePlayer.FIRST].handleInputs(pressed_keys, [pygame.K_UP, pygame.K_DOWN, pygame.K_RIGHT, pygame.K_LEFT])
            self.gameMap.snakes[SnakePlayer.SECOND].handleInputs(pressed_keys, [pygame.K_w, pygame.K_s, pygame.K_d, pygame.K_a])

    def Update(self):
        if self.gameMode == GameMode.SINGLE:
            isOnApple = self.gameMap.snakes[SnakePlayer.FIRST].move(self.gameMap.apples)
            if isOnApple == True:
                self.score += 10
            if self.gameMap.checkCollision() == True:
                self.gameMap.render()
                self.SwitchToScene(GameOverScene(self.score, self.gameMode))
        if self.gameMode == GameMode.AUTO:
            print("Auto")
        if self.gameMode == GameMode.DUAL:
            self.gameMap.snakes[SnakePlayer.FIRST].move(self.gameMap.apples)
            self.gameMap.snakes[SnakePlayer.SECOND].move(self.gameMap.apples)
            if self.gameMap.checkCollision() == True or self.gameMap.checkCollisionFirstWithSecond() == True:
                self.gameMap.render()
                self.SwitchToScene(GameOverScene(1, self.gameMode))
            if self.gameMap.checkCollisionSecondSnake() == True or self.gameMap.checkCollisionSecondWithFirst() == True:
                self.gameMap.render()
                self.SwitchToScene(GameOverScene(2, self.gameMode))

    def Render(self):
        App.screen.fill(pygame.Color("Black"))
        if self.gameMode == GameMode.SINGLE:
            t = Text("Score: " + str(self.score), (400, 30))
            t.draw()
            self.gameMap.render()
        if self.gameMode == GameMode.AUTO:
            print("Auto")
        if self.gameMode == GameMode.DUAL:
            self.gameMap.render()
