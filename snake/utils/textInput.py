import pygame
import os
from app import App


class TextInput():
    text = ""
    active = False
    color_active = pygame.Color('white')
    color_passive = (95, 95, 95)
    color = color_passive
    defaultOffset = 5

    def __init__(self, posx, posy, size, fontsize=42):
        self.x = posx
        self.y = posy
        self.size = size
        self.font = pygame.font.Font(os.path.join(
            "fonts", 'PublicPixel.ttf'), fontsize)
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])
    
    def ProcessInput(self, event, pressed_keys):
        if self.active == False:
            return
        if pressed_keys[pygame.K_ESCAPE] or pressed_keys[pygame.K_RETURN]:
            self.active = False
            self.color = self.color_passive
            return
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                if (event.unicode == '_' or event.key == pygame.K_ESCAPE
                or event.key == pygame.K_RETURN or len(self.text) >= 10):
                    return
                self.text += event.unicode

    def event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    self.active = True
                    self.color = self.color_active
                else:
                    self.active = False
                    self.color = self.color_passive

    def draw(self):
        pygame.draw.rect(App.screen, self.color, self.rect)
        text_surface = self.font.render(self.text, True, (0, 0, 0))
        offset = self.size[0] / 2 - (len(self.text) / 2) * self.size[0] / 10
        if offset < self.defaultOffset:
            offset = self.defaultOffset
        App.screen.blit(text_surface, (self.x + offset, self.y + 5))
