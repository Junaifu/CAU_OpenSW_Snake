import pygame
from app import App

class Button:
    def __init__(self, text,  posx, posy, bg="black"):
        self.x = posx
        self.y = posy

        pygame.font.init()
        self.font = pygame.font.SysFont("Comic Sans MS", 60)
        self.text = self.font.render(text, 1, pygame.Color("White"))
        self.size = self.text.get_size()
        self.surface = pygame.Surface(self.size)
        self.surface.fill(bg)
        self.surface.blit(self.text, (0, 0))
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])

    def show(self):
        App.screen.blit(self.surface, (self.x, self.y))

