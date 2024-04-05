import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Movimiento de la Pelota")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)

# Clase de la pelota
class Ball:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed = 5

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

        # Verificar los límites de la pantalla
        if self.x < -self.radius:
            self.x = SCREEN_WIDTH + self.radius
        elif self.x > SCREEN_WIDTH + self.radius:
            self.x = -self.radius
        if self.y < -self.radius:
            self.y = SCREEN_HEIGHT + self.radius
        elif self.y > SCREEN_HEIGHT + self.radius:
            self.y = -self.radius

# Crear la pelota
ball = Ball(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 20, PURPLE)

# Bucle principal del juego
while True:
    screen.fill(WHITE)

    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Obtener las teclas presionadas
    keys = pygame.key.get_pressed()

    # Mover la pelota basada en las teclas presionadas
    if keys[pygame.K_LEFT]:
        ball.move(-ball.speed, 0)
    if keys[pygame.K_RIGHT]:
        ball.move(ball.speed, 0)
    if keys[pygame.K_UP]:
        ball.move(0, -ball.speed)
    if keys[pygame.K_DOWN]:
        ball.move(0, ball.speed)

    # Dibujar y actualizar la pelota
    ball.draw()

    # Actualizar la pantalla
    pygame.display.flip()

    # Establecer velocidad de fotogramas
    pygame.time.Clock().tick(30)

