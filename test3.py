import pygame

pygame.init()

screen = pygame.display.set_mode((500,500))
clock = pygame.time.Clock()

x = 80
y = 10
speed = pygame.Vector2(x, y)
position = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 4)
color = (255, 255, 255)
GRAVITY = 9.8
damping_factor = 0.7
dt = 0
r = 30

running = True
while running:
    screen.fill("black")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if position[1] > screen.get_height() - r:
        position[1] = screen.get_height() - r
        speed[1] *= -damping_factor

    if position[0] > screen.get_width() - r:
        position[0] = screen.get_width() - r
        speed[0] *= -damping_factor 
    elif position[0] < r:
        position[0] = r
        speed[0] *= -damping_factor
    
    speed[0] 
    speed[1] += GRAVITY
    position[1] += speed[1] * dt
    position[0] += speed[0] * dt

    pygame.draw.circle(screen, color, position, r)
    pygame.display.flip()
    dt = clock.tick(60) / 1000