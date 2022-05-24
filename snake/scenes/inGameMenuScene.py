from scenes.sceneBase import *
from utils.button import Button
import time
import os
import scenes
from enums import GameMode

class InGameMenuScene(SceneBase):
    gameMap = None
    gameMode = None
    resumeButton = None
    restartButton = None
    saveButton = None
    exitButton = None
    score = None
    filePath = "backup_files/"

    def __init__(self, gameMap, score, gameMode):
        SceneBase.__init__(self)
        pygame.display.set_caption("Snake in-game menu")
        self.gameMap = gameMap
        self.score = score
        self.gameMode = gameMode
        self.initMenu()

    def initMenu(self):
        self.resumeButton = Button("RESUME", 450, 200, self.goBackToGame, False)
        self.restartButton = Button("RESTART", 455, 300, self.goBackToGame, True)
        if (self.gameMode == GameMode.SINGLE):
            self.saveButton = Button("SAVE", 480, 400, lambda params: self.saveBackup())
        self.exitButton = Button("EXIT", 490, 500, lambda params: self.Terminate())

    def goBackToGame(self, params):
        App.isPaused = False
        if not params[0]: # resume the game
            self.SwitchToScene(scenes.gameScene.GameScene(self.gameMode, self.score, self.gameMap))
        else:
            self.SwitchToScene(scenes.gameScene.GameScene(self.gameMode))

    def saveBackup(self):
        isExist = os.path.exists(self.filePath)
        if not isExist:
            os.makedirs(self.filePath)
        filename = "backup_" + str(time.time())
        f = open(self.filePath + filename, "a")
        self.gameMap.saveMap(f, self.score)
        f.close()
        App.isPaused = False
        self.SwitchToScene(scenes.menuScene.MenuScene())

    def ProcessInput(self, events, pressed_keys):
        for event in events:
            self.resumeButton.event(event)
            self.restartButton.event(event)
            if (self.gameMode == GameMode.SINGLE):
                self.saveButton.event(event)
            self.exitButton.event(event)

    def Update(self):
        # TODO: Game Logique Update
        pass

    def Render(self):
        App.screen.fill(pygame.Color("Black"))
        self.resumeButton.draw()
        self.restartButton.draw()
        if (self.gameMode == GameMode.SINGLE):
            self.saveButton.draw()
        self.exitButton.draw()