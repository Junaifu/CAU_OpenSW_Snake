import pygame
from app import App
import os


class Text:
    def __init__(self, text, pos):
        self.text = text
        self.pos = pos

        self.fontname = None
        self.fontcolor = pygame.Color('white')
        self.font = pygame.font.Font(os.path.join(
            "..", "fonts", 'PublicPixel.ttf'),
            42)
        self.render()

    def render(self):
        self.img = self.font.render(self.text, True, self.fontcolor)
        self.rect = self.img.get_rect()
        self.rect.topleft = self.pos

    def draw(self):
        App.screen.blit(self.img, self.rect)
