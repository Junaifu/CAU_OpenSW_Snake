from enum import IntEnum

class Direction(IntEnum):
    NORTH = 0
    SOUTH = 1
    EAST = 2
    WEST = 3

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
        self.size = len(parts)
        self.nextMove = self.direction;
        self.nextNextMove = None;
        self.lastMove = self.direction;
    
    def move(self, apples):
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
        if (self.x, self.y) in apples:
            isOnApple = True
        else:
            isOnApple = False
        self.moveBody(oldX, oldY, isOnApple)
        return isOnApple
    
    def moveBody(self, oldX, oldY, isOnApple):
        length = len(self.bodyParts)
        newPart = (0, 0)
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
    
    def handleInputs(self, pressed_keys, keysList):
        if pressed_keys[keysList[Direction.NORTH]]:
            self.changeDirection(Direction.NORTH)
        elif pressed_keys[keysList[Direction.SOUTH]]:
            self.changeDirection(Direction.SOUTH)
        elif pressed_keys[keysList[Direction.EAST]]:
            self.changeDirection(Direction.EAST)
        elif pressed_keys[keysList[Direction.WEST]]:
            self.changeDirection(Direction.WEST)

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
    
    def setNextMove(self, direction):
        self.nextMove = direction;