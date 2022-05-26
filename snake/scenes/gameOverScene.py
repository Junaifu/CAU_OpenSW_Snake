from scenes.sceneBase import *
import scenes
from utils.text import Text
from utils.textInput import TextInput
from utils.button import Button
import pygame
from datetime import datetime
from enums import GameMode


class GameOverScene(SceneBase):
    gameMode = None
    score = 0
    textInput = None
    playAgainButton = None
    mainMenuButton = None
    error = False

    background = pygame.image.load('resources/bg.png')
    stars = pygame.image.load('resources/Stars Small_1.png')
    stars2 = pygame.image.load('resources/Stars-Big_1_1_PC.png')
    firstStarsIndex = 0
    secondStarsIndex = 0

    def __init__(self, score, gameMode):
        SceneBase.__init__(self)
        pygame.display.set_caption("Game Over")
        self.gameMode = gameMode
        self.score = score
        self.textInput = TextInput(340, 400, (430, 70))
        self.mainMenuButton = Button(
            "BACK TO MAIN MENU", 340, 600, self.mainMenuCallback)
        self.playAgainButton = Button(
            "PLAY AGAIN", 420, 550, self.playAgainCallback)
        self.background = pygame.transform.scale(
            self.background, (App.screenSizeX, App.screenSizeY))
        self.stars = pygame.transform.scale(
            self.stars, (App.screenSizeX, App.screenSizeY))
        self.stars2 = pygame.transform.scale(
            self.stars2, (App.screenSizeX, App.screenSizeY))
        self.firstStarsIndex = -App.screenSizeY
        self.secondStarsIndex = -App.screenSizeY

    def mainMenuCallback(self, params):
        self.SwitchToScene(scenes.menuScene.MenuScene())
        self.handleRanking(self.textInput.text)

    def playAgainCallback(self, params):
        self.SwitchToScene(scenes.gameScene.GameScene(self.gameMode))
        self.handleRanking(self.textInput.text)

    def ProcessInput(self, events, pressed_keys):
        for event in events:
            self.textInput.ProcessInput(event, pressed_keys)
            self.textInput.event(event)
            self.mainMenuButton.event(event)
            self.playAgainButton.event(event)

    def Update(self):
        if (self.firstStarsIndex >= 0):
            App.screen.blit(
                self.stars, (0, App.screenSizeY + self.firstStarsIndex))
            self.firstStarsIndex = -App.screenSizeY
        self.firstStarsIndex += 2
        if (self.secondStarsIndex >= 0):
            App.screen.blit(
                self.stars2, (0, App.screenSizeY + self.secondStarsIndex))
            self.secondStarsIndex = -App.screenSizeY
        self.secondStarsIndex += 1

    def Render(self):
        App.screen.blit(self.background, (0, 0))
        App.screen.blit(self.stars, (0, self.firstStarsIndex))
        App.screen.blit(
            self.stars, (0, App.screenSizeY + self.firstStarsIndex))
        App.screen.blit(self.stars2, (0, self.secondStarsIndex))
        App.screen.blit(
            self.stars2, (0, App.screenSizeY + self.secondStarsIndex))
        t = Text("Game Over", (350, 100))
        t.draw()
        if self.gameMode == GameMode.DUAL:
            winnerText = Text("Player " + str(self.score) + " won the game", (130, 200))
            winnerText.draw()
        else:
            if (self.gameMode == GameMode.SINGLE):
                scoreText = Text("Your score: " + str(self.score), (270, 200))
                playerNameText = Text("Enter your name:", (200, 300))
                playerNameText.draw()
                self.textInput.draw()
                self.playAgainButton.draw()
            else:
                scoreText = Text("Bot's score: " + str(self.score), (270, 200))
            scoreText.draw()
        self.mainMenuButton.draw()

    def getRankingFileContent(self):
        try:
            self.rankingsText = []
            f = open(App.rankingPathfile, 'r')
            lines = f.readlines()
            for i, line in enumerate(lines):
                lineParsed = line.strip().split("_")
                rankingText = lineParsed[0] + "_" + lineParsed[1][0:10] + "_" + lineParsed[2] + "_" + lineParsed[3]
                self.rankingsText.append(rankingText)
            f.close()
        except OSError:
            self.error = True

    def handleRanking(self, playerName):
        if playerName == "":
            return
        self.getRankingFileContent()
        now = datetime.now()
        date = now.strftime("%Y/%m/%d")

        rankingPos = 0
        for ranking in self.rankingsText:
            rankingInfo = ranking.split('_')
            if int(rankingInfo[2]) < int(self.score):
                break
            rankingPos += 1
        if rankingPos >= 9:
            return
        self.rankingsText = self.rankingsText[0:rankingPos] + [str(rankingPos + 1) + "_" + playerName + "_" + str(self.score) + "_" + date] + self.rankingsText[rankingPos:]
        rankingFileContent = ""
        rankingPos = 1
        for ranking in self.rankingsText:
            if rankingPos > 10:
                break
            rankingFileContent += str(rankingPos)
            rankingFileContent += ranking[1:]
            rankingFileContent += "\n"
            rankingPos += 1
        f = open(App.rankingPathfile, "w")
        f.write(rankingFileContent)
        f.close()

