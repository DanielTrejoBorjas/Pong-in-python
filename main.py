import pygame
import sys
from Player import Player
from Ball import Ball

# Configuración de Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()

# Crear instancias de Player y Ball
player1 = Player(screen, x_position=50, y_position=250, width=10, height=100, color=(255, 255, 255))
player2 = Player(screen, x_position=740, y_position=250, width=10, height=100, color=(255, 255, 255))
ball = Ball(screen, x_position=400, y_position=300, direction=[5, 3], radius=10)

# Fuente para mostrar la puntuación
font = pygame.font.Font(None, 36)

def draw_scores():
    score_text = f"Player 1: {player1.score} | Player 2: {player2.score}"
    score_surface = font.render(score_text, True, (255, 255, 255))
    screen.blit(score_surface, (screen.get_width() // 2 - score_surface.get_width() // 2, 10))

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movimiento de la pelota y los jugadores
    ball.move(player1, player2)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player1.move_up()
    if keys[pygame.K_s]:
        player1.move_down()
    if keys[pygame.K_UP]:
        player2.move_up()
    if keys[pygame.K_DOWN]:
        player2.move_down()

    # Rellenar la pantalla con color negro
    screen.fill((0, 0, 0))

    # Dibujar la pelota, los jugadores y las puntuaciones
    ball.draw()
    player1.draw()
    player2.draw()
    draw_scores()

    # Actualizar la pantalla
    pygame.display.flip()

    # Limitar el framerate
    clock.tick(60)
