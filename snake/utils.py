import pygame
from app import App


class Text:
    def __init__(self, text, pos, fontSize=42):
        self.text = text
        self.pos = pos
        self.fontColor = pygame.Color('white')
        self.fontSize = fontSize
        self.font = pygame.font.Font(os.path.join(
            "..", "fonts", 'PublicPixel.ttf'),
            self.fontSize)
        self.render()

    def setPosition(self, pos):
        self.pos = pos
        self.rect.topleft = self.pos

    def render(self):
        self.sprite = self.font.render(self.text, True, self.fontColor)
        self.rect = self.sprite.get_rect()
        self.rect.topleft = self.pos

    def draw(self):
        App.screen.blit(self.sprite, self.rect)
