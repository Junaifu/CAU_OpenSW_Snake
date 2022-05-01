from scenes.sceneBase import SceneBase
from utils.button import Button
from utils.text import Text
from app import App
import scenes
import pygame


class RankingScene(SceneBase):
    background = pygame.image.load('../resources/bg.png')
    stars = pygame.image.load('../resources/Stars Small_1.png')
    stars2 = pygame.image.load('../resources/Stars-Big_1_1_PC.png')
    firstStarsIndex = 0
    secondStarsIndex = 0
    error = False
    ranking = []

    def __init__(self):
        SceneBase.__init__(self)
        pygame.display.set_caption("Ranking")
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
        self.titleText = Text("Ranking", (150, 150))
        textWidth, _ = self.titleText.font.size("Ranking")
        self.titleText.setPosition(
            ((App.screenSizeX / 2) - (textWidth / 2), 50))

        try:
            self.rankingsText = []
            f = open(App.rankingPathfile, 'r')
            lines = f.readlines()
            offset = 150
            for i, line in enumerate(lines):
                lineParsed = line.strip().split("_")
                rankingText = lineParsed[3] + " | " + lineParsed[0] + ". " + \
                    lineParsed[1][0:10] + ": " + lineParsed[2]
                self.rankingsText.append(
                    Text(rankingText, (0, 0), 30))
                rankingTextWidth, rankingTextHeight = self.rankingsText[i].font.size(
                    rankingText)
                self.rankingsText[i].setPosition(
                    (0.1 * App.screenSizeX, offset))
                offset += rankingTextHeight + 10
            print(self.ranking)

        except OSError:
            self.error = True

    def ProcessInput(self, events, pressed_keys):
        for event in events:
            self.backButton.event(event)
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
        for rankingText in self.rankingsText:
            rankingText.draw()
