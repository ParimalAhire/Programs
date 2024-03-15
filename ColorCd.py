import pygame
import sys

# Initialize pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Interactive Color Palette")

# Define colors
BLACK = (0, 0, 0)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Calculate color based on mouse position
    red = min(255, mouse_x // 2)
    green = min(255, mouse_y // 2)
    blue = int(min(255, (mouse_x+mouse_y) // 4))
 
    # Fill the screen with the calculated color
    screen.fill((red, green, blue))

    # Draw a rectangle with a contrasting color
    #pygame.draw.circle(screen, (255 - red, 255 - green, 255 - blue), (mouse_x, mouse_y), 25)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Quit pygame
pygame.quit()
sys.exit()
