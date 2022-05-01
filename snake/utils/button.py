import pygame
from app import App
import os


class Button:
    """
        A button object

        Args:
            text: string -> Text on button
            postx: double -> Position x of the button
            posty: double -> Position y of the button
            callback: func -> The function to call when we click on the button
            *params: splat operator -> The parameters that the function need.
                -> the callback function has to contain a parameter which will be a tuple. 
                -> You don't need to provide this arg if you don't need arg.
            bg: string -> Button background
            fontsize: int -> text font size

        Example:
            Button("TEST", 150, 150, onClick, "yes", 1, 2)
            def onClick(params):
                print(params[0])
                print(params[1])
                print(params[2])

        Result OnClick:
            yes
            1
            2
    """

    def __init__(self, text,  posx, posy, callback, *params, bg="black", fontsize=25):
        self.x = posx
        self.y = posy
        self.callback = callback
        self.params = params

        pygame.font.init()
        self.font = pygame.font.Font(os.path.join(
            "fonts", 'PublicPixel.ttf'), fontsize)
        self.text = self.font.render(text, 1, pygame.Color("White"))
        self.size = self.text.get_size()
        self.surface = pygame.Surface(self.size)
        self.surface.fill(bg)
        self.surface.blit(self.text, (0, 0))
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])

    def draw(self):
        App.screen.blit(self.surface, (self.x, self.y))

    def event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    self.callback(self.params)
