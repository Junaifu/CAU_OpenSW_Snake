import pygame
from enum import Enum, IntEnum
import numpy as np
from snakeBody import SnakeBody, Direction
from enums import GameMode

class MapTile(Enum):
    EMPTY = 1
    WALL = 2
    HEAD = 3
    BODY = 4
    APPLE = 5

class SnakePlayer(IntEnum):
    FIRST = 0
    SECOND = 1

class GameMap:
    mapSizeX = 40
    mapSizeY = 40
    mapContent = [None] * mapSizeX
    surface = None
    tileSize = 15
    surface = pygame.display.set_mode((mapSizeX * tileSize, mapSizeY * tileSize))
    mapBeginningX = (1080 - mapSizeX * tileSize) / 2
    mapBeginningY = 100
    snakes = []
    wallColor = (127, 127, 127)
    emptyColor = (9, 0, 99)
    headColor = (29, 135, 37)
    bodyColor = (5, 228, 0)
    appleColor = (255, 0, 0)
    appleX = 0
    appleY = 0
    gameMode = GameMode.SINGLE

    def __init__(self, gameMode):
        self.gameMode = gameMode
        if self.gameMode == gameMode.DUAL:
            self.mapSizeX = 80
            self.mapContent = [None] * self.mapSizeX
            GameMap.tileSize = 12
            GameMap.mapBeginningX = (1080 - self.mapSizeX * GameMap.tileSize) / 2
            self.snakes = [SnakeBody(78, 38, Direction.NORTH, []), SnakeBody(1, 1, Direction.SOUTH, [])]
        else:
            self.snakes = [SnakeBody(self.mapSizeX / 2, self.mapSizeY / 2, Direction.NORTH, [])]
        self.appleX = 0
        self.appleY = 0
        self.clearMap()

    def setMap(self, mapContent, mapSizeX, mapSizeY):
        self.mapContent = mapContent
        self.mapSizeX = mapSizeX
        self.mapSizeY = mapSizeY

    def setSnake(self, snake):
        self.snakes = [snake]

    def render(self):
        self.clearMap()
        self.putSnakeOnMap()
        self.appleManagement()
        for i in range(self.mapSizeX):
            for j in range(self.mapSizeY):
                if self.mapContent[i][j] == MapTile.WALL:
                    color = GameMap.wallColor
                elif self.mapContent[i][j] == MapTile.HEAD:
                    color = GameMap.headColor
                elif self.mapContent[i][j] == MapTile.BODY:
                    color = GameMap.bodyColor
                elif self.mapContent[i][j] == MapTile.APPLE:
                    color = GameMap.appleColor
                else:
                    color = GameMap.emptyColor
                tileX = GameMap.mapBeginningX + i * GameMap.tileSize
                tileY = GameMap.mapBeginningY + j * GameMap.tileSize
                pygame.draw.rect(self.surface, color, pygame.Rect(tileX, tileY, GameMap.tileSize, GameMap.tileSize))

    def resetGame(self):
        self.snakes = [SnakeBody(self.mapSizeX / 2, self.mapSizeY / 2, Direction.NORTH, [])]

    def clearMap(self):
        for i in range(self.mapSizeX):
            self.mapContent[i] = [None] * self.mapSizeY
            for j in range(self.mapSizeY):
                if i == 0 or i == self.mapSizeX - 1 or j == 0 or j == self.mapSizeY - 1:
                    self.mapContent[i][j] = MapTile.WALL
                elif i == self.appleX and j == self.appleY:
                    self.mapContent[i][j] = MapTile.APPLE
                else:
                    self.mapContent[i][j] = MapTile.EMPTY

    def putSnakeOnMap(self):
        for part in self.snakes[SnakePlayer.FIRST].bodyParts:
            self.mapContent[part[0]][part[1]] = MapTile.BODY
        self.mapContent[self.snakes[SnakePlayer.FIRST].x][self.snakes[0].y] = MapTile.HEAD
        if self.gameMode == GameMode.DUAL:
            for part in self.snakes[SnakePlayer.SECOND].bodyParts:
                self.mapContent[part[0]][part[1]] = MapTile.BODY
            self.mapContent[self.snakes[SnakePlayer.SECOND].x][self.snakes[SnakePlayer.SECOND].y] = MapTile.HEAD

    def checkCollision(self):
        if self.mapContent[self.snakes[SnakePlayer.FIRST].x][self.snakes[SnakePlayer.FIRST].y] == MapTile.WALL or self.snakes[SnakePlayer.FIRST].checkBodyCollision() == True:
            self.putSnakeOnMap()
            return True
        return False

    def saveMap(self, f, score):
        f.write(str(self.mapSizeX) + ',' + str(self.mapSizeY) + '\n')
        f.write(str(self.snakes[SnakePlayer.FIRST].direction.value) + '\n')
        f.write(str(self.snakes[SnakePlayer.FIRST].bodyParts) + '\n')
        f.write(str(score) + '\n')
        for i in range(self.mapSizeX):
            for j in range(self.mapSizeY):
                if self.mapContent[j][i] == MapTile.WALL:
                    f.write(str(MapTile.WALL.value))
                elif self.mapContent[j][i] == MapTile.HEAD:
                    f.write(str(MapTile.HEAD.value))
                elif self.mapContent[j][i] == MapTile.BODY:
                    f.write(str(MapTile.BODY.value))
                elif self.mapContent[j][i] == MapTile.APPLE:
                    f.write(str(MapTile.APPLE.value))
                else:
                    f.write(str(MapTile.EMPTY.value))
                if j + 1 != self.mapSizeY:
                    f.write(',')
            f.write('\n')

    ## Apple

    def isThereAppleOnMap(self):
        if self.mapContent[self.appleX][self.appleY] == MapTile.APPLE:
            return True
        return False

    def randGeneration(self):
        x = np.random.randint(low=1, high=self.mapSizeX, size=1)[0]
        y = np.random.randint(low=1, high=self.mapSizeY, size=1)[0]
        return x,y

    def putAppleOnMap(self):
        x,y = self.randGeneration()

        while (self.mapContent[x][y] != MapTile.EMPTY):
            x,y = self.randGeneration()
        self.mapContent[x][y] = MapTile.APPLE
        self.appleX = x
        self.appleY = y

    def appleManagement(self):
        hasApple = self.isThereAppleOnMap()
        if not hasApple:
            self.putAppleOnMap()
