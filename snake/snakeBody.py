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
    
    def move(self, appleX, appleY):
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
        if self.x == appleX and self.y == appleY:
            isOnApple = True
        else:
            isOnApple = False
        self.moveBody(oldX, oldY, isOnApple)
        return isOnApple
    
    def moveBody(self, oldX, oldY, isOnApple):
        length = 0
        newPart = (0, 0)
        for part in self.bodyParts:
            length += 1
        if length == 0:
            newPart = (oldX, oldY)
        for i in range(length - 1, -1, -1):
            if isOnApple == True and i == length - 1:
                newPart = self.bodyParts[i]
            if i == 0:
                self.bodyParts[i] = (oldX, oldY)
            else:
                self.bodyParts[i] = (self.bodyParts[i - 1][0], self.bodyParts[i - 1][1])
        if isOnApple == True:
            self.bodyParts.append(newPart)
    
    def changeDirection(self, newDirection):
        if (newDirection == Direction.NORTH and self.direction == Direction.SOUTH or
            newDirection == Direction.SOUTH and self.direction == Direction.NORTH or
            newDirection == Direction.WEST and self.direction == Direction.EAST or
            newDirection == Direction.EAST and self.direction == Direction.WEST):
            return
        self.direction = newDirection
    
    def checkBodyCollision(self):
        for part in self.bodyParts:
            if part[0] == self.x and part[1] == self.y:
                return True
        return False
