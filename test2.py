import pygame
import math

pygame.init()

screen = pygame.display.set_mode((500,500))
clock = pygame.time.Clock()

position = pygame.Vector2(screen.get_width() / 2,screen.get_height() / 2)
speed = pygame.Vector2( 0, 0)
g_acceleration = 9.81
radius = 40
dt = 0 

running = True

while running:

	screen.fill("black")

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	if speed.y >= 0:
		speed.y = math.sqrt(2 * (500 - position.y) *  g_acceleration)
	else:
		speed.y -= g_acceleration * dt

	
	if position.y > screen.get_height() - radius :
		speed.y *= -0.7

	position.y += speed.y * dt

	circle = pygame.draw.circle(screen, "white", position, radius)

	

	pygame.display.flip()

	dt = clock.tick(60) / 100