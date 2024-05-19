import pygame

pygame.init()

screen = pygame.display.set_mode((500,500))

clock = pygame.time.Clock()

speed = pygame.Vector2(10,20)

position = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
dt = 0
radius = 50
color = ( 255, 255, 255)

running = True
bounce = False

while running:
	screen.fill((int(position.x%256), int(position.y % 256), int(position.x + position.y)% 256))
	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			running = False

	position += speed * dt

	circle = pygame.draw.circle(screen,  color , position, radius)

	if position.x > screen.get_width() - radius or position.x < radius:
		speed.x *= -1
		bounce = True
	elif position.y > screen.get_height() - radius or position.y < radius:
		speed.y *= -1
		bounce = True

	if bounce:
		color = (int(position.x%256), int(position.y% 256), int(position.x + position.y)% 256)
		bounce = False


	

	pygame.display.flip()

	dt = clock.tick(60) / 100