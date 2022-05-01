from scenes.sceneBase import *
from utils.button import Button

class InGameMenuScene(SceneBase):
    gameMap = None
    resumeButton = None
    restartButton = None
    saveButton = None
    exitButton = None

    def __init__(self, previousScene, gameMap):
        SceneBase.__init__(self, previousScene)
        pygame.display.set_caption("Snake in-game menu")
        self.gameMap = gameMap
        self.initMenu()

    def initMenu(self):
        self.resumeButton = Button("RESUME", 450, 200, self.goBackToGame, False)
        self.restartButton = Button("RESTART", 455, 300, self.goBackToGame, True)
        self.saveButton = Button("SAVE", 480, 400, None)
        self.exitButton = Button("EXIT", 490, 500, lambda params: self.Terminate())

    def goBackToGame(self, params):
        App.isPaused = False
        self.SwitchToPreviousScene()
        if params[0]:
            self.gameMap.resetGame()

    def ProcessInput(self, events, pressed_keys):
        for event in events:
            self.resumeButton.event(event)
            self.restartButton.event(event)
            self.saveButton.event(event)
            self.exitButton.event(event)

    def Update(self):
        # TODO: Game Logique Update
        pass

    def Render(self):
        App.screen.fill(pygame.Color("Black"))
        self.resumeButton.draw()
        self.restartButton.draw()
        self.saveButton.draw()
        self.exitButton.draw()