from enum import Enum

class Direction(Enum):
    NORTH = 1
    SOUTH = 2
    EAST = 3
    WEST = 4

class SnakeBody:
    x = 0
    y = 0
    size = 0
    direction = Direction.NORTH
    bodyParts = []

    def __init__(self, posX, posY, snakeDir, parts):
        self.x = int(posX)
        self.y = int(posY)
        self.direction = snakeDir
        self.bodyParts = parts
        length = 0
        for part in parts:
            length += 1
        self.size = length
    
    def move(self):
        oldX = self.x
        oldY = self.y
        if self.direction == Direction.NORTH:
            self.y -= 1
        elif self.direction == Direction.SOUTH:
            self.y += 1
        elif self.direction == Direction.EAST:
            self.x += 1
        else:
            self.x -= 1
        self.moveBody(oldX, oldY)
    
    def moveBody(self, oldX, oldY):
        length = 0
        for part in self.bodyParts:
            length += 1
        for i in range(length - 1, -1, -1):
            if i == 0:
                self.bodyParts[i] = (oldX, oldY)
            else:
                self.bodyParts[i] = (self.bodyParts[i - 1][0], self.bodyParts[i - 1][1])
    
    def changeDirection(self, newDirection):
        if newDirection == Direction.NORTH and self.direction == Direction.SOUTH:
            return
        if newDirection == Direction.SOUTH and self.direction == Direction.NORTH:
            return
        if newDirection == Direction.WEST and self.direction == Direction.EAST:
            return
        if newDirection == Direction.EAST and self.direction == Direction.WEST:
            return
        self.direction = newDirection
