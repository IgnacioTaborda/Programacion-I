import pygame
import variables as var

# Inicializar Pygame
pygame.init()

# Definir dimensiones de la ventana
ancho_ventana = 800
alto_ventana = 600
ventana = pygame.display.set_mode((ancho_ventana, alto_ventana))
pygame.display.set_caption("Insertar imagen en rect")

# Cargar la imagen
try:
    imagen = pygame.image.load(var.PLAY_BUTTON).convert_alpha()  # Convertir la imagen para un mejor rendimiento
except FileNotFoundError:
    print("Error: No se encontró la imagen. Asegúrate de que la ruta sea correcta.")
    pygame.quit()
    exit()


# Obtener el rectángulo de la imagen
rect_imagen = imagen.get_rect()

# Definir la posición del rectángulo
rect_imagen.x = 100
rect_imagen.y = 100

# Definir el color de fondo
color_fondo = (0, 230, 0)  # Gris claro

# Bucle principal del juego
ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    # Rellenar la pantalla con el color de fondo
    ventana.fill(color_fondo)

    # Dibujar la imagen en el rectángulo
    ventana.blit(imagen, rect_imagen)

    # Actualizar la pantalla
    pygame.display.flip()

# Salir de Pygame
pygame.quit()