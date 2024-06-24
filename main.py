import pygame

pygame.init()

color = (255,255,255)
rect_color = (255,0,0)
me = pygame.Rect(30, 30, 60, 60)

# CREATING CANVAS
canvas = pygame.display.set_mode((500, 500))

# TITLE OF CANVAS
pygame.display.set_caption("My Console")
exit = False

while not exit:
    canvas.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True

    pygame.draw.rect(canvas, rect_color, me)

    pygame.display.update()