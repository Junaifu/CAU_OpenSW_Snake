import pygame
from enum import Enum
import numpy as np
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
    snake = None
    wallColor = (127, 127, 127)
    emptyColor = (9, 0, 99)
    headColor = (29, 135, 37)
    bodyColor = (5, 228, 0)
    appleColor = (255, 0, 0)
    appleX = 0
    appleY = 0

    def __init__(self):
        self.snake = SnakeBody(self.mapSizeX / 2, self.mapSizeY / 2, Direction.NORTH, [])
        self.appleX = 0
        self.appleY = 0
        self.clearMap()

    def setMap(self, mapContent, mapSizeX, mapSizeY):
        self.mapContent = mapContent
        self.mapSizeX = mapSizeX
        self.mapSizeY = mapSizeY

    def setSnake(self, snake):
        self.snake = snake

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
        self.snake = SnakeBody(self.mapSizeX / 2, self.mapSizeY / 2, Direction.NORTH, [])

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
        for part in self.snake.bodyParts:
            self.mapContent[part[0]][part[1]] = MapTile.BODY
        self.mapContent[self.snake.x][self.snake.y] = MapTile.HEAD

    def checkCollision(self):
        if self.mapContent[self.snake.x][self.snake.y] == MapTile.WALL or self.snake.checkBodyCollision() == True:
            self.putSnakeOnMap()
            return True
        return False

    def saveMap(self, f, score):
        f.write(str(self.mapSizeX) + ',' + str(self.mapSizeY) + '\n')
        f.write(str(self.snake.direction.value) + '\n')
        f.write(str(self.snake.bodyParts) + '\n')
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

    def checkHorizontalSnakeBody(self):
        snakeBodyPartVertical = [position for position in self.snake.bodyParts if position[1] == self.snake.y]
        if (snakeBodyPartVertical):
            snakeBodyPartVerticalNorth = [position for position in snakeBodyPartVertical if position[1] < self.snake.y]
            snakeBodyPartVerticalSouth = [position for position in snakeBodyPartVertical if position[1] > self.snake.y]
            if not snakeBodyPartVerticalNorth:
                self.snake.setNextMove(Direction.NORTH)
                return
            if not snakeBodyPartVerticalSouth:
                self.snake.setNextMove(Direction.SOUTH)
                return
            maxDistance = max(snakeBodyPartVertical, key = lambda t: abs(t[1] - self.snake.y))
            self.snake.setNextMove(Direction.NORTH)
            if (maxDistance[1] > self.snake.y):
                self.snake.setNextMove(Direction.SOUTH)
        else:
            self.snake.setNextMove(Direction.NORTH)
            if (self.appleY > self.snake.y):
                self.snake.setNextMove(Direction.SOUTH)

    def checkVerticalSnakeBody(self):
        snakeBodyPartHorizontal = [position for position in self.snake.bodyParts if position[0] == self.snake.x]
        if (snakeBodyPartHorizontal):
            snakeBodyPartHorizontalWest = [position for position in snakeBodyPartHorizontal if position[0] < self.snake.x]
            snakeBodyPartHorizontalEast = [position for position in snakeBodyPartHorizontal if position[0] > self.snake.x]
            if not snakeBodyPartHorizontalWest:
                self.snake.setNextMove(Direction.WEST)
                return
            if not snakeBodyPartHorizontalEast:
                self.snake.setNextMove(Direction.EAST)
                return
            maxDistance = max(snakeBodyPartHorizontal, key = lambda t: abs(t[0] - self.snake.x))
            self.snake.setNextMove(Direction.WEST)
            if (maxDistance[0] > self.snake.x):
                self.snake.setNextMove(Direction.EAST)
        else:
            self.snake.setNextMove(Direction.WEST)
            if (self.appleX > self.snake.x):
                self.snake.setNextMove(Direction.EAST)
    
    def snakeAvoidBody(self):
        offset = 2
        if self.snake.nextMove == Direction.NORTH and any(pos in self.snake.bodyParts for pos in [(self.snake.x, nextPos) for nextPos in range(self.snake.y, self.snake.y - offset, -1)]):
            self.checkVerticalSnakeBody()
        if self.snake.nextMove == Direction.SOUTH and any(pos in self.snake.bodyParts for pos in [(self.snake.x, nextPos) for nextPos in range(self.snake.y + 1, self.snake.y + offset)]):
            self.checkVerticalSnakeBody()
        if self.snake.nextMove == Direction.WEST and any(pos in self.snake.bodyParts for pos in [(nextPos, self.snake.y) for nextPos in range(self.snake.x, self.snake.x - offset, -1)]):
            self.checkHorizontalSnakeBody()
        if self.snake.nextMove == Direction.EAST and any(pos in self.snake.bodyParts for pos in [(nextPos, self.snake.y) for nextPos in range(self.snake.x + 1, self.snake.x + offset)]):
            self.checkHorizontalSnakeBody()

    

    def snakeNextMove(self):
        if (self.appleX > self.snake.x and self.snake.direction != Direction.WEST):
            self.snake.setNextMove(Direction.EAST);
        elif (self.appleX < self.snake.x and self.snake.direction != Direction.EAST):
            self.snake.setNextMove(Direction.WEST);
        elif (self.appleY > self.snake.y and self.snake.direction != Direction.NORTH):
            self.snake.setNextMove(Direction.SOUTH);
        elif (self.appleY < self.snake.y and self.snake.direction != Direction.SOUTH):
            self.snake.setNextMove(Direction.NORTH);

        self.snakeAvoidBody()
        if (self.snake.nextMove == Direction.WEST and self.snake.x - 1 <= 0):
            self.snake.setNextMove(Direction.SOUTH)
        if (self.snake.nextMove == Direction.NORTH and self.snake.y - 1 <= 0):
            self.snake.setNextMove(Direction.EAST)
        if (self.snake.nextMove == Direction.SOUTH and self.snake.x + 1 >= self.mapSizeX):
            self.snake.setNextMove(Direction.WEST)
        if (self.snake.nextMove == Direction.EAST and self.snake.y + 1 >= self.mapSizeY):
            self.snake.setNextMove(Direction.NORTH)

        self.snake.changeDirection(self.snake.nextMove)
        self.snake.lastMove = self.snake.nextMove