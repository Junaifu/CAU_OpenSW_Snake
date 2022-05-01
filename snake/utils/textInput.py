import pygame
import os
from app import App


class TextInput():
    text = ""
    active = False
    color_active = pygame.Color('lightskyblue3')
    color_passive = pygame.Color('chartreuse4')
    color = color_passive

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
        if pressed_keys[pygame.K_ESCAPE]:
            self.active = False
            self.color = self.color_passive
            return
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                if event.unicode == '_' or event.key == pygame.K_ESCAPE or len(self.text) >= 10:
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
        text_surface = self.font.render(self.text, True, (255, 255, 255))
        offset = 5
        App.screen.blit(text_surface, (self.x + offset, self.y + 5))
