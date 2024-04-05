# Juego realizado con chatGPT
En este repositorio podemos encontrar un juego de una pelota que tiene el movimiento 
de moverse hacia arriba, abajo, derecha e izquierda.

## Prompts y respuestas:

-You
haz un juego en python usando pygame en el que hay una pelota que tiene la posibilidad de moverse hacia la derecha, izquierda, arriba y abajo
Aquí tienes un ejemplo básico de un juego en Python utilizando Pygame en el que una pelota puede moverse hacia la derecha, izquierda, arriba y abajo:

-ChatGPT
```python
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
RED = (255, 0, 0)

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

# Crear la pelota
ball = Ball(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 20, RED)

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
```

Este código crea una ventana de Pygame donde se dibuja una pelota. Puedes mover la pelota utilizando las teclas de flecha (izquierda, derecha, arriba, abajo). La velocidad de la pelota está configurada en 5 píxeles por fotograma, pero puedes ajustarla según tus necesidades.

-You
puedes hacer que la pelota vuelva a aparecer cuando pase los limites de la screen

-ChatGPT
¡Claro! Para hacer que la pelota vuelva a aparecer en el lado opuesto cuando pase los límites de la pantalla, podemos modificar el código de la siguiente manera:

```python
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
RED = (255, 0, 0)

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
ball = Ball(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 20, RED)

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
```

En este código, dentro del método `move()` de la clase `Ball`, hemos agregado comprobaciones para verificar si la pelota ha pasado los límites de la pantalla. Si lo hace, la posición se ajusta para que la pelota aparezca en el lado opuesto de la pantalla. De esta manera, la pelota reaparecerá en el lado opuesto cuando pase los límites de la pantalla.

-You
como es el color morado

-ChatGPT
El color morado en Pygame se puede representar mediante una tupla RGB (Rojo, Verde, Azul). La tupla de color para el morado puede variar dependiendo de la intensidad de cada componente, pero una representación común sería (128, 0, 128) o (160, 32, 240), por ejemplo.

Aquí tienes un ejemplo de cómo definir el color morado en Pygame y utilizarlo en tu juego:

```python
PURPLE = (128, 0, 128)  # Tupla RGB para el color morado

# Crear la pelota con el color morado
ball = Ball(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 20, PURPLE)
```

En este ejemplo, hemos definido una constante `PURPLE` que representa el color morado utilizando una tupla RGB. Luego, puedes usar esta constante para asignar el color morado a la pelota u a otros elementos de tu juego.

### FIN