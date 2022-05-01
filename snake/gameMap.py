from enum import Enum
import pygame
from snakeBody import SnakeBody, Direction

class MapTile(Enum):
    EMPTY = 1
    WALL = 2
    HEAD = 3
    BODY = 4
    APPLE = 5

class GameMap:
    mapSizeX = 40
    mapSizeY = 40
    mapContent = [None] * mapSizeX
    surface = None
    tileSize = 15
    surface = pygame.display.set_mode((mapSizeX * tileSize, mapSizeY * tileSize))
    mapBeginningX = (1080 - mapSizeX * tileSize) / 2
    mapBeginningY = 100
    snake = SnakeBody(mapSizeX / 2, mapSizeY / 2, Direction.NORTH, [])
    wallColor = (127, 127, 127)
    emptyColor = (9, 0, 99)
    headColor = (29, 135, 37)
    bodyColor = (5, 228, 0)

    def __init__(self):
        self.clearMap()
    
    def render(self):
        self.clearMap()
        self.putSnakeOnMap()
        for i in range(self.mapSizeX):
            for j in range(self.mapSizeY):
                if self.mapContent[i][j] == MapTile.WALL:
                    color = GameMap.wallColor
                elif self.mapContent[i][j] == MapTile.HEAD:
                    color = GameMap.headColor
                elif self.mapContent[i][j] == MapTile.BODY:
                    color = GameMap.bodyColor
                else:
                    color = GameMap.emptyColor
                tileX = GameMap.mapBeginningX + i * GameMap.tileSize
                tileY = GameMap.mapBeginningY + j * GameMap.tileSize
                pygame.draw.rect(self.surface, color, pygame.Rect(tileX, tileY, GameMap.tileSize, GameMap.tileSize))

    def resetGame(self):
        self.snake = SnakeBody(self.mapSizeX / 2, self.mapSizeY / 2, Direction.NORTH, [])

    def clearMap(self):
        for i in range(self.mapSizeX):
            self.mapContent[i] = [None] * self.mapSizeY
            for j in range(self.mapSizeY):
                if i == 0 or i == self.mapSizeX - 1 or j == 0 or j == self.mapSizeY - 1:
                    self.mapContent[i][j] = MapTile.WALL
                else:
                    self.mapContent[i][j] = MapTile.EMPTY

    def putSnakeOnMap(self):
        self.mapContent[self.snake.x][self.snake.y] = MapTile.HEAD
        for part in self.snake.bodyParts:
            self.mapContent[part[0]][part[1]] = MapTile.BODY
