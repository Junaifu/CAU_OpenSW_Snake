from scenes.sceneBase import SceneBase
from scenes.gameScene import GameScene
from utils.button import Button
from utils.text import Text
from gameMap import *
from snakeBody import SnakeBody
from app import App
import scenes
import pygame
import os
import ast
from datetime import datetime


class SaveScene(SceneBase):
    background = pygame.image.load('resources/bg.png')
    stars = pygame.image.load('resources/Stars Small_1.png')
    stars2 = pygame.image.load('resources/Stars-Big_1_1_PC.png')
    firstStarsIndex = 0
    secondStarsIndex = 0
    error = False
    saveButtons = []

    def __init__(self):
        SceneBase.__init__(self)
        pygame.display.set_caption("Saves")
        self.background = pygame.transform.scale(
            self.background, (App.screenSizeX, App.screenSizeY))
        self.stars = pygame.transform.scale(
            self.stars, (App.screenSizeX, App.screenSizeY))
        self.stars2 = pygame.transform.scale(
            self.stars2, (App.screenSizeX, App.screenSizeY))
        self.firstStarsIndex = 0
        self.secondStarsIndex = 0
        self.backButton = Button("<- Go Back", 0, 50,
                                 (lambda x: self.SwitchToScene(scenes.menuScene.MenuScene())))
        self.titleText = Text("Saves", (0.1 * App.screenSizeX, App.screenSizeY / 2))
        textWidth, _ = self.titleText.font.size("Saves")
        self.saveButtons = []

        try:
            self.rankingsText = []
            files = os.listdir(App.saveDirectory)
            offset = 50
            files.sort(reverse=True)
            for f in files:
                d = datetime.fromtimestamp(float(f.split("_")[1]), tz=None)
                self.saveButtons.append(Button(d.strftime("%Y/%m/%d - %H:%M:%S"), 0.4 * App.screenSizeX, offset, self.saveFileSelected, f))
                offset += 70

        except OSError:
            self.error = True

        self.limit = len(self.saveButtons) * self.saveButtons[0].size[1]
        self.intermediate = pygame.surface.Surface((App.screenSizeX, App.screenSizeY + self.limit), pygame.SRCALPHA, 32)
        self.intermediate = self.intermediate.convert_alpha()
        self.i_a = self.intermediate.get_rect()
        self.x1 = self.i_a[0]
        self.x2 = self.x1 + self.i_a[2]
        self.y1 = self.i_a[1]
        self.y2 = self.y1 + self.i_a[3]
        self.scroll_y = 0
        for line in range(self.y1,self.y2):
            pygame.draw.line(self.intermediate, (0, 0, 0, 32), (self.x1, line), (self.x2, line))
        for button in self.saveButtons:
            self.intermediate.blit(button.surface, (button.x, button.y))


    def getSnakePosition(self, map):
        for i in range(len(map)):
            for j in range(len(map[i])):
                if (map[i][j] == MapTile.HEAD.value):
                    return j, i

    def saveFileSelected(self, params):
        filepath = App.saveDirectory + params[0]
        try:
            f = open(filepath, 'r')
            lines = f.readlines()
            sizeMap = (int(lines[0].split(",")[0]), int(lines[0].split(",")[0]))
            snakeDirection = int(lines[1])
            snakeParts = ast.literal_eval(lines[2])
            score = int(lines[3])
            map = [None] * sizeMap[1]
            i = 0
            for j in range(4, len(lines)):
                map[i] = [int(char) for char in lines[j].split(",")]
                i += 1
            posX, posY = self.getSnakePosition(map)
            snake = SnakeBody(posX, posY, Direction(snakeDirection), snakeParts)    
            gameMap = GameMap()
            gameMap.setSnake(snake)
            gameMap.setMap(map, sizeMap[0], sizeMap[1])
            gameScene = GameScene()
            gameScene.loadGameScene(gameMap, score)
            self.SwitchToScene(gameScene)
        except OSError:
            self.error = True

    def ProcessInput(self, events, pressed_keys):
        for event in events:
            for button in self.saveButtons:
                button.event(event, self.scroll_y)
            self.backButton.event(event)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    self.scroll_y = min(self.scroll_y + 15, 0)
                if event.button == 5:
                    self.scroll_y = max(self.scroll_y - 15, -self.limit)

    def Update(self):
        if (self.firstStarsIndex <= -App.screenSizeY):
            App.screen.blit(
                self.stars, (0, App.screenSizeY + self.firstStarsIndex))
            self.firstStarsIndex = 0
        self.firstStarsIndex -= 2

        if (self.secondStarsIndex <= -App.screenSizeY):
            App.screen.blit(
                self.stars2, (0, App.screenSizeY + self.secondStarsIndex))
            self.secondStarsIndex = 0
        self.secondStarsIndex -= 1

    def Render(self):
        App.screen.blit(self.background, (0, 0))
        App.screen.blit(self.stars, (0, self.firstStarsIndex))
        App.screen.blit(
            self.stars, (0, App.screenSizeY + self.firstStarsIndex))
        App.screen.blit(self.stars2, (0, self.secondStarsIndex))
        App.screen.blit(
            self.stars2, (0, App.screenSizeY + self.secondStarsIndex))
        self.titleText.draw()
        self.backButton.draw()
        App.screen.blit(self.intermediate, (0, self.scroll_y))

