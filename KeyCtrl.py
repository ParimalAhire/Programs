import pygame

pygame.init()

screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))


circle_radius = 40
circle = pygame.Vector2(screen_width,screen_height)
speed = 5

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        circle.y -= speed
    if keys[pygame.K_DOWN]:
        circle.y += speed
    if keys[pygame.K_LEFT]:
        circle.x -= speed
    if keys[pygame.K_RIGHT]:
        circle.x += speed
    if keys[pygame.K_q]:
        pygame.quit()



    screen.fill("black")

    pygame.draw.circle(screen, "white", (circle.x, circle.y), circle_radius)

    pygame.display.flip()

    pygame.time.Clock().tick(30)

pygame.quit()