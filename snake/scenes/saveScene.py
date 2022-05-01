from scenes.sceneBase import SceneBase
from utils.button import Button
from utils.text import Text
from app import App
import scenes
import pygame
import os
from datetime import datetime


class SaveScene(SceneBase):
    background = pygame.image.load('resources/bg.png')
    stars = pygame.image.load('resources/Stars Small_1.png')
    stars2 = pygame.image.load('resources/Stars-Big_1_1_PC.png')
    firstStarsIndex = 0
    secondStarsIndex = 0
    error = False
    saves = []

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
        self.saves = []
        self.saveButtons = []

        try:
            self.rankingsText = []
            files = os.listdir("backups")
            offset = 150
            print(files)
            for f in files:
                d = datetime.fromtimestamp(float(f.split("_")[1]), tz=None)
                # self.saves.append({"filename": f, "label": d.strftime("%Y/%m/%d - %H:%M:%S")})
                self.saveButtons.append(Button(d.strftime("%Y/%m/%d - %H:%M:%S"), 0.25 * App.screenSizeX, offset, self.saveFileSelected, f))
                offset += 70
            
            # f = open(App.rankingPathfile, 'r')
            # lines = f.readlines()
            # offset = 150
            # for i, line in enumerate(lines):
            #     lineParsed = line.strip().split("_")
            #     rankingText = lineParsed[3] + " | " + lineParsed[0] + ". " + \
            #         lineParsed[1][0:10] + ": " + lineParsed[2]
            #     self.rankingsText.append(
            #         Text(rankingText, (0, 0), 30))
            #     rankingTextWidth, rankingTextHeight = self.rankingsText[i].font.size(
            #         rankingText)
            #     self.rankingsText[i].setPosition(
            #         (0.1 * App.screenSizeX, offset))
            #     offset += rankingTextHeight + 10
            # print(self.ranking)

        except OSError:
            self.error = True

    def saveFileSelected(self, params):
        filepath = App.saveDirectory + params[0]
        try:
            f = open(filepath, 'r')
            lines = f.readlines()
            sizeMap = (int(lines[0].split(",")[0]), int(lines[0].split(",")[0]))
            snakeDirection = int(lines[1])
            score = int(lines[2])
            print("SizeMap: " + str(sizeMap[0]) + ", " + str(sizeMap[1]))
            print("snakeDirection: " + str(snakeDirection))
            print("score: " + str(score))
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
        # for rankingText in self.rankingsText:
        #     rankingText.draw()
