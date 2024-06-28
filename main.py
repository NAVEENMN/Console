import pygame
from player import *
from sys import exit

pygame.init()

color = (0, 0, 0)
rect_color = (255, 0, 0)

# CREATING CANVAS
screen_width=1280
screen_height=720
screen=pygame.display.set_mode([screen_width, screen_height])
#screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
window_width, window_height = screen.get_size()
clock = pygame.time.Clock()

# TITLE OF CANVAS
pygame.display.set_caption("My Console")

# use ttf file for font
test_font = pygame.font.Font(None, 50)

text_surface = test_font.render("hello", False, rect_color)

test_surface = pygame.image.load("assets/maps/home/base.png")
test_surface = pygame.transform.scale(test_surface, (test_surface.get_width()*1.4, test_surface.get_height()*1.4))

"""
TODO: Get and test all key codes for console
"""

def main():
    running = True
    print(window_width, window_height)
    player = Player()
    while running:
        screen.fill(color)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                print(f"Pressed: {event.key}")

        screen.blit(test_surface,(180, 0))
        #screen.blit(text_surface, (100, 100))

        player.draw(screen)
        player.handle_keys()

        pygame.display.update()

        # Update screen 60 times per second
        clock.tick(60)


if __name__ == "__main__":
    main()