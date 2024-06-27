import pygame
from sys import exit

pygame.init()

color = (255, 255, 255)
rect_color = (255, 0, 0)
me = pygame.Rect(30, 30, 60, 60)

# CREATING CANVAS
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
window_width, window_height = screen.get_size()
clock = pygame.time.Clock()

# TITLE OF CANVAS
pygame.display.set_caption("My Console")

# use ttf file for font
test_font = pygame.font.Font(None, 50)

text_surface = test_font.render("hello", False, rect_color)

test_surface = pygame.Surface((100, 200))
test_surface.fill(rect_color)

"""
TODO: Get and test all key codes for console
"""

def main():
    running = True
    print(window_width, window_height)
    while running:
        screen.fill(color)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                print(f"Pressed: {event.key}")

        pygame.draw.rect(screen, rect_color, me)

        screen.blit(test_surface,(0, 0))
        screen.blit(text_surface, (100, 100))

        pygame.display.update()

        # Update screen 60 times per second
        clock.tick(60)


if __name__ == "__main__":
    main()