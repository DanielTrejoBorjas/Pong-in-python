import pygame

class Player:
    def __init__(self, screen, x_position:int, y_position:int, width:int, height:int, color:tuple) -> None:
        self.screen = screen
        self.x_position = x_position
        self.y_position = y_position
        self.width = width
        self.height = height
        self.color = color
        self.speed = 5
        self.score = 0  # Añadir puntuación

    def move_up(self):
        if self.y_position - self.speed >= 0:
            self.y_position -= self.speed

    def move_down(self):
        if self.y_position + self.height + self.speed <= self.screen.get_height():
            self.y_position += self.speed

    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.x_position, self.y_position, self.width, self.height))
