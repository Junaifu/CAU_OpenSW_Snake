import pygame
from app import App
from sceneBase import SceneBase
from button import Button

class InGameMenuScene(SceneBase):
    gameMap = None
    resumeButton = Button("Resume", 450, 200)
    restartButton = Button("Restart", 455, 300)
    saveButton = Button("Save", 480, 400)
    exitButton = Button("Exit", 490, 500)

    def __init__(self, previousScene, gameMap):
        SceneBase.__init__(self, previousScene)
        pygame.display.set_caption("Snake in-game menu")
        self.gameMap = gameMap

    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if pygame.mouse.get_pressed()[0]:
                    if self.resumeButton.rect.collidepoint(x,y):
                        App.isPaused = False
                        self.SwitchToPreviousScene()
                    elif self.restartButton.rect.collidepoint(x,y):
                        App.isPaused = False
                        self.SwitchToPreviousScene()
                        self.gameMap.resetGame()
                    elif self.saveButton.rect.collidepoint(x,y):
                        print("save")
                    elif self.exitButton.rect.collidepoint(x,y):
                        self.Terminate()

    def Update(self):
        # TODO: Game Logique Update
        pass

    def Render(self):
        App.screen.fill(pygame.Color("Black"))
        self.resumeButton.show()
        self.restartButton.show()
        self.saveButton.show()
        self.exitButton.show()