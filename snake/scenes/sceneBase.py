import pygame
from app import App

class SceneBase:
    def __init__(self):
        App.fps = 30
        self.next = self

    # NOTE: This method will receive all the events that happened since the last frame.
    def ProcessInput(self, events, pressed_keys):
        print("Bruh, you didn't override 'ProcessInput' in the child class")

    # NOTE: Put your game logic in here for the scene.
    def Update(self):
        print("Bruh, you didn't override 'Update' in the child class")

    # NOTE: Put your render code here. It will receive the main screen Surface as input.
    def Render(self):
        print("Bruh, you didn't override 'Render' in the child class")

    def SwitchToScene(self, next_scene):
        if next_scene == None:
            self.next = next_scene
            return
        fade = pygame.Surface((App.screenSizeX, App.screenSizeY))
        for alpha in range(0, 50):
            fade.set_alpha(alpha, pygame.RLEACCEL)
            App.screen.blit(fade, (0, 0))
            pygame.display.update()
            pygame.time.delay(25)
        # for alpha in range (fade.get_alpha(), 0, -1):
        self.next = next_scene

    def Terminate(self):
        self.SwitchToScene(None)
