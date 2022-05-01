from snake.scenes.sceneBase import *
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
        self.resumeButton = Button("RESUME", 450, 200, self.goBackToGame())
        self.restartButton = Button("RESTART", 455, 300, self.goBackToGame(True))
        self.saveButton = Button("SAVE", 480, 400,)
        self.exitButton = Button("EXIT", 490, 500)

    def goBackToGame(self, shouldRestart = False):
        App.isPaused = False
        self.SwitchToPreviousScene()
        if shouldRestart:
            self.gameMap.resetGame()

    def ProcessInput(self, events, pressed_keys):
        for event in events:
            self.resumeButton.event(event)
            self.restartButton.event(event)
            self.saveButton.event(event)
            self.exitButton.event(event)
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     x, y = pygame.mouse.get_pos()
            #     if pygame.mouse.get_pressed()[0]:
            #         if self.resumeButton.rect.collidepoint(x,y):
            #             App.isPaused = False
            #             self.SwitchToPreviousScene()
            #         elif self.restartButton.rect.collidepoint(x,y):
            #             App.isPaused = False
            #             self.SwitchToPreviousScene()
            #         elif self.saveButton.rect.collidepoint(x,y):
            #             print("save")
            #         elif self.exitButton.rect.collidepoint(x,y):
            #             self.Terminate()

    def Update(self):
        # TODO: Game Logique Update
        pass

    def Render(self):
        App.screen.fill(pygame.Color("Black"))
        self.resumeButton.show()
        self.restartButton.show()
        self.saveButton.show()
        self.exitButton.show()