import pygame
from app import App
from sceneBase import SceneBase
from gameMap import GameMap
from button import Button
import time

class InGameMenuScene(SceneBase):
    gameMap = GameMap()
    resumeButton = Button("Resume", 450, 200)
    restartButton = Button("Restart", 455, 300)
    saveButton = Button("Save", 480, 400)
    exitButton = Button("Exit", 490, 500)

    def __init__(self):
        SceneBase.__init__(self)
        pygame.display.set_caption("Snake in-game menu")

    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if pygame.mouse.get_pressed()[0]:
                    if self.resumeButton.rect.collidepoint(x,y):
                        print("resume")
                    elif self.restartButton.rect.collidepoint(x,y):
                        print("restart")
                    elif self.saveButton.rect.collidepoint(x,y):
                        self.writeBackupFile()
                        self.Terminate()
                    elif self.exitButton.rect.collidepoint(x,y):
                        self.Terminate()

    def writeBackupFile(self):
        filename = "backup_" + str(time.time())
        f = open(filename, "a")
        self.gameMap.saveMap(f)
        f.close()

    def Update(self):
        # TODO: Game Logique Update
        pass

    def Render(self):
        App.screen.fill(pygame.Color("Black"))
        self.resumeButton.show()
        self.restartButton.show()
        self.saveButton.show()
        self.exitButton.show()