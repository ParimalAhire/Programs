import pygame

pygame.init()

screen = pygame.display.set_mode((500,500))
clock = pygame.time.Clock()

position = pygame.Vector2(screen.get_width() / 2,screen.get_height() / 2)
speed = pygame.Vector2( 0, 200)

radius = 30
dt = 0

GRAVITY = 0.72
damping_factor = 0.8
ball_adj = 0.92 * radius


running = True
rest = False

while running:

	screen.fill("black")

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	if position.y > screen.get_height() - radius or position.y < 0:
		position.y = screen.get_height() - radius  
		speed.y *= -1 * damping_factor

	elif screen.get_width() - ball_adj < position.y:
		rest = True

	if not rest:
		speed.y += GRAVITY

	print(speed.y,screen.get_width() - ball_adj, position.y)

	position.y += speed.y * dt


	
	circle = pygame.draw.circle(screen, "white", position, radius)

	pygame.display.flip()

	dt = clock.tick(60) / 1000