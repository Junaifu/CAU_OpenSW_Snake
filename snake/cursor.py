import pygame
from app import App

class Cursor:
    cursorRect = None
    points = [[0, 15], [15, 7.5], [0, 0]]
    color = pygame.Color("white")
    # def __init__(self):
        # pygame.draw.polygon(App.screen, color=(255, 0, 0),points=[(50, 100), (100, 50), (150, 100)])
        # pygame.draw.rect(App.screen, (0, 0, 255), [100, 100, 400, 100], 2)

    def draw(self):
        cursorRect = pygame.draw.polygon(App.screen, self.color, points=self.points, )
        # pygame.draw.rect(App.screen, (0, 0, 255), [100, 100, 400, 100], 2)
        # print(cursorRect)
        for point in self.points:
            point[1] += 1
        self.color = pygame.Color("blue")
