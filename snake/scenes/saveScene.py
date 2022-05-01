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
    saves = []
    # intermediate = pygame.surface

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
        self.titleText = Text("Saves", (150, 150))
        textWidth, _ = self.titleText.font.size("Saves")
        self.titleText.setPosition(
            ((App.screenSizeX / 2) - (textWidth / 2), 50))
        self.saveButtons = []
        self.page = []

        try:
            self.rankingsText = []
            files = os.listdir("backups")
            offset = 150
            print(files)
            for f in files:
                d = datetime.fromtimestamp(float(f.split("_")[1]), tz=None)
                self.saveButtons.append(Button(d.strftime("%Y/%m/%d - %H:%M:%S"), 0.25 * App.screenSizeX, offset, self.saveFileSelected, f))
                offset += 70

        except OSError:
            self.error = True

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
                button.event(event)
        pass

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
        for button in self.saveButtons:
            button.draw()
