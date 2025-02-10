import pygame
from Tetris_funciones import FONDO
import random

# Configuración del juego
ANCHO = 700
ALTO = 900
TAM_BLOQUE = 30
COLUMNAS = ANCHO // TAM_BLOQUE
FILAS = ALTO // TAM_BLOQUE
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

# Inicializar Pygame
pygame.init()
VENTANA = pygame.display.set_mode([ANCHO, ALTO])
pygame.display.set_caption('Juego de Tetris')

# Icono del juego
icono = pygame.image.load('pngwing.com (7).png')
pygame.display.set_icon(icono)

# Fuentes
fuente = pygame.font.SysFont("arial", 30)

fondo = FONDO(20, 25)

# Cargar y redimensionar imágenes de figuras
FIGURAS = {
    'L': [pygame.transform.scale(pygame.image.load(f'pngwing.com (1_{i}).png'), (TAM_BLOQUE, TAM_BLOQUE)) for i in range(4)],
    'T': [pygame.transform.scale(pygame.image.load(f'pngwing.com (2_{i}).png'), (TAM_BLOQUE, TAM_BLOQUE)) for i in range(4)],
    'cuadrado': [pygame.transform.scale(pygame.image.load('pngwing.com (3).png'), (TAM_BLOQUE, TAM_BLOQUE))],
    'linea_triple': [pygame.transform.scale(pygame.image.load(f'pngwing.com (4_{i}).png'), (TAM_BLOQUE, TAM_BLOQUE)) for i in range(2)],
    'N': [pygame.transform.scale(pygame.image.load(f'pngwing.com (6_{i}).png'), (TAM_BLOQUE, TAM_BLOQUE)) for i in range(2)],
}

# Clase para las piezas
class Piezas:
    def __init__(self, x, y, tipo):
        self.x = x
        self.y = y
        self.tipo = tipo
        self.rotacion = 0
        self.imagenes = FIGURAS[tipo]

    def dibujar(self, ventana):
        ventana.blit(self.imagenes[self.rotacion], (self.x, self.y))

    def mover_abajo(self):
        self.y += TAM_BLOQUE

    def mover_lateral(self, dx):
        self.x += dx

    def rotar(self):
        self.rotacion = (self.rotacion + 1) % len(self.imagenes)

# Crear una matriz para el tablero
def crear_tablero():
    return [[None for _ in range(COLUMNAS)] for _ in range(FILAS)]

tablero = crear_tablero()

# Verificar si una fila está completa
def verificar_filas():
    global tablero, score
    filas_completas = 0
    for i in range(FILAS):
        if None not in tablero[i]:  # Si la fila no tiene huecos
            filas_completas += 1
            del tablero[i]  # Eliminar la fila completa
            tablero.insert(0, [None for _ in range(COLUMNAS)])  # Añadir una fila vacía en la parte superior
    return filas_completas

# Detectar colisiones
def detectar_colision(pieza, dx=0, dy=0):
    nueva_x = pieza.x + dx
    nueva_y = pieza.y + dy
    if nueva_x < 0 or nueva_x >= ANCHO or nueva_y >= ALTO:  # Límites de la ventana
        return True
    fila = nueva_y // TAM_BLOQUE
    columna = nueva_x // TAM_BLOQUE
    if fila >= FILAS or tablero[fila][columna] is not None:  # Colisión con el tablero
        return True
    return False

# Generar una nueva pieza
def generar_nueva_pieza():
    x = random.randint(0, COLUMNAS - 1) * TAM_BLOQUE
    tipo = random.choice(list(FIGURAS.keys()))
    return Piezas(x, 0, tipo)

# Fin del juego
def verificar_fin_juego():
    for columna in range(COLUMNAS):
        if tablero[0][columna] is not None:  # Si la fila superior está ocupada
            return True
    return False

# Configuración inicial
pieza_actual = generar_nueva_pieza()
velocidad = 500  # Milisegundos entre movimientos
ultimo_tiempo = pygame.time.get_ticks()
score = 0

# Bucle principal del juego
jugando = True
while jugando:
    eventos = pygame.event.get()

    for evento in eventos:
        if evento.type == pygame.QUIT:
            jugando = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT and not detectar_colision(pieza_actual, dx=-TAM_BLOQUE):
                pieza_actual.mover_lateral(-TAM_BLOQUE)
            if evento.key == pygame.K_RIGHT and not detectar_colision(pieza_actual, dx=TAM_BLOQUE):
                pieza_actual.mover_lateral(TAM_BLOQUE)
            if evento.key == pygame.K_UP:
                pieza_actual.rotar()

    fondo.dibujar(VENTANA)
    # Movimiento automático hacia abajo
    tiempo_actual = pygame.time.get_ticks()
    if tiempo_actual - ultimo_tiempo > velocidad:
        if not detectar_colision(pieza_actual, dy=TAM_BLOQUE):
            pieza_actual.mover_abajo()
        else:
            # Colocar pieza actual en el tablero
            fila = pieza_actual.y // TAM_BLOQUE
            columna = pieza_actual.x // TAM_BLOQUE
            tablero[fila][columna] = pieza_actual.tipo

            # Verificar filas completas y actualizar puntaje
            filas_eliminadas = verificar_filas()
            if filas_eliminadas > 0:
                score += filas_eliminadas * 100  # 100 puntos por fila eliminada

            # Verificar si el juego ha terminado
            if verificar_fin_juego():
                jugando = False

            # Generar nueva pieza
            pieza_actual = generar_nueva_pieza()

        ultimo_tiempo = tiempo_actual

    # Dibujar todo
    VENTANA.fill(NEGRO)  # Limpiar pantalla
    for fila in range(FILAS):
        for columna in range(COLUMNAS):
            if tablero[fila][columna] is not None:
                pieza = FIGURAS[tablero[fila][columna]][0]  # Usar la primera rotación para piezas fijas
                VENTANA.blit(pieza, (columna * TAM_BLOQUE, fila * TAM_BLOQUE))
    pieza_actual.dibujar(VENTANA)

    # Dibujar puntaje
    texto_score = fuente.render(f'Score: {score}', True, BLANCO)
    VENTANA.blit(texto_score, (10, 10))
    pygame.display.update()

pygame.quit()
