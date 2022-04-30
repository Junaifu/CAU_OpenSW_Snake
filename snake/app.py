import pygame

class App:
    screen = None
    clock = None
    screenSizeX = None
    screenSizeY = None
    snakeFont = None
    currentScene = None
    fps = 60

    def __init__(self, x, y, scene):
        pygame.init()
        pygame.font.init()
        pygame.mouse.set_visible(False) 
        self.flags = pygame.RESIZABLE
        self.snakeFont = pygame.font.SysFont('Comic Sans MS', 30)
        App.screenSizeX = x
        App.screenSizeY = y
        App.screen = pygame.display.set_mode(
            (App.screenSizeX, App.screenSizeY), self.flags)
        App.screen.fill(pygame.Color('gray'))
        App.clock = pygame.time.Clock()
        scene.initMenu()
        self.currentScene = scene
        # NOTE: Do not delete
        # self.screen = pygame.display.set_mode(
        #     (0, 0), pygame.FULLSCREEN)

    def run(self):
        while self.currentScene != None:
            filtered_events = []
            pressed_keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                quit_attempt = False
                if event.type == pygame.QUIT:
                    quit_attempt = True
                elif event.type == pygame.KEYDOWN:
                    alt_pressed = pressed_keys[pygame.K_LALT] or \
                        pressed_keys[pygame.K_RALT]
                    if event.key == pygame.K_ESCAPE:
                        quit_attempt = True
                    elif event.key == pygame.K_F4 and alt_pressed:
                        quit_attempt = True
                if quit_attempt:
                    self.currentScene.Terminate()
                else:
                    filtered_events.append(event)
            self.currentScene.ProcessInput(filtered_events, pressed_keys)
            self.currentScene.Update()
            self.currentScene.Render()
            self.currentScene = self.currentScene.next
            pygame.display.flip()
            App.clock.tick(App.fps)
