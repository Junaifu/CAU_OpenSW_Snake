import pygame

class App:
    screen = None
    clock = None
    screenSizeX = None
    screenSizeY = None
    snakeFont = None
    currentScene = None
    fps = 30
    isPaused = False
    rankingPathfile = "resources/rankings.txt"
    saveDirectory = "backup_files/"
    def __init__(self, x, y, scene):
        pygame.init()
        pygame.font.init()
        self.snakeFont = pygame.font.SysFont('Comic Sans MS', 30)
        App.screenSizeX = x
        App.screenSizeY = y
        App.screen = pygame.display.set_mode(
            (App.screenSizeX, App.screenSizeY))
        App.screen.fill(pygame.Color('gray'))
        App.clock = pygame.time.Clock()
        scene.initMenu()
        self.currentScene = scene

    def run(self):
        time = 0
        while self.currentScene != None:
            filtered_events = []
            pressed_keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                quit_attempt = False
                if event.type == pygame.VIDEORESIZE:
                    App.screen = pygame.display.set_mode(
                        (event.w, event.h), pygame.RESIZABLE)
                    App.screenSizeX = event.w
                    App.screenSizeY = event.h
                if event.type == pygame.QUIT:
                    quit_attempt = True
                elif event.type == pygame.KEYDOWN:
                    alt_pressed = pressed_keys[pygame.K_LALT] or \
                        pressed_keys[pygame.K_RALT]
                    if event.key == pygame.K_F4 and alt_pressed:
                        quit_attempt = True
                if quit_attempt:
                    self.currentScene.Terminate()
                else:
                    filtered_events.append(event)
            if time >= self.fps:
                self.currentScene.Update()
                time = 0
            self.currentScene.ProcessInput(filtered_events, pressed_keys)
            self.currentScene.Render()
            self.currentScene = self.currentScene.next
            pygame.display.flip()
            if (self.isPaused != True):
                time += App.clock.tick(App.fps)