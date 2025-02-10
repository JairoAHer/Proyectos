import pygame 

class FONDO:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.ancho = 420
        self.alto = 680
        self.velocidad = 1
        self.border = 1
        self.color = "white"
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)

    def dibujar(self, ventana):
        pygame.draw.rect(ventana, self.color,  self.rect, self.border)
