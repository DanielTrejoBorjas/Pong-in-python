import pygame
import random

class Ball:
    def __init__(self, screen, x_position:int = 0, y_position:int = 0, direction:list = [0,0], radius:float = 5) -> None:
        self.screen = screen
        self.x_position = x_position
        self.y_position = y_position
        self.direction = direction
        self.radius = radius
        self.speed_increment = 1.1  # Factor de incremento de velocidad
        self.reset()

    def reset(self):
        # Reset the ball to the center and give it a random direction
        self.x_position = self.screen.get_width() // 2
        self.y_position = self.screen.get_height() // 2
        angle = random.uniform(-1, 1)
        self.direction = [5 * angle, 5 * (1 - abs(angle))]

        # Ensure the ball moves in both directions
        if random.choice([True, False]):
            self.direction[0] = -self.direction[0]

    def move(self, player1, player2):
        # Mover la pelota
        self.x_position += self.direction[0]
        self.y_position += self.direction[1]

        # Verifica los límites de la pantalla y rebota si es necesario
        if self.x_position - self.radius < 0:
            player2.score += 1
            self.reset()
        elif self.x_position + self.radius > self.screen.get_width():
            player1.score += 1
            self.reset()

        if self.y_position - self.radius < 0 or self.y_position + self.radius > self.screen.get_height():
            self.direction[1] = -self.direction[1]

        # Verifica colisiones con los jugadores
        self.check_collision(player1)
        self.check_collision(player2)

    def check_collision(self, player):
        # Verifica colisión con un jugador
        if (self.x_position - self.radius < player.x_position + player.width and
            self.x_position + self.radius > player.x_position and
            self.y_position - self.radius < player.y_position + player.height and
            self.y_position + self.radius > player.y_position):
            # Rebota la pelota al chocar con el jugador
            self.direction[0] = -self.direction[0]
            # Incrementa la velocidad
            self.direction[0] *= self.speed_increment
            self.direction[1] *= self.speed_increment

    def draw(self):
        pygame.draw.circle(self.screen, (255, 0, 0), (int(self.x_position), int(self.y_position)), int(self.radius))  # Rojo
