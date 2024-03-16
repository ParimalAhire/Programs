import pygame
import math

pygame.init()

WIDTH, HEIGHT = 500 , 400
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Slingshot")

#Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#Constants
FPS = 60
GRAVITY = 1
FORCE = 2
damping_factor = 0.7

#Sling Properties
slingshot_pos = pygame.Vector2(100, HEIGHT - 100)
slingshot_radius = 50
pull_back_length = 100
angle_radians = pygame.Vector2(0, 0)

#Ball Properties
ball_radius = 40
ball_color = RED
ball_pos = pygame.Vector2(slingshot_pos)
ball_velocity = pygame.Vector2(0, 0)

#sling mechanics variables
is_pulling_back = False
release = False
pull_back_distance = 0
angle = 0

clock = pygame.time.Clock()
running = True
dt = 0

while running:

	screen.fill(WHITE)

	#Event Handling
	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				is_pulling_back = True
				release = False
				ball_pos = pygame.Vector2(slingshot_pos)

		elif event.type == pygame.MOUSEBUTTONUP:
			if event.button == 1:
				is_pulling_back = False
				ball_speed = FORCE * min(pull_back_distance, pull_back_length)
				ball_velocity = pygame.Vector2(-ball_speed * math.cos(angle_radians.x), -ball_speed * math.sin(angle_radians.y))
				release = True

	pygame.draw.circle(screen, BLACK, slingshot_pos, slingshot_radius, 2)
	pygame.draw.line(screen,BLACK, (slingshot_pos.x , slingshot_pos.y + slingshot_radius ), (slingshot_pos.x, screen.get_height()), 2)

	if is_pulling_back:
			mouse = pygame.Vector2(pygame.mouse.get_pos())
			line = pygame.draw.line(screen, "red", ball_pos, mouse, 1)
			pull_back_distance = math.sqrt( (mouse.y - ball_pos.y)**2 + (mouse.x - ball_pos.x)**2)
			angle_radians = pygame.Vector2((math.atan2((mouse.y - ball_pos.y),(mouse.x - ball_pos.x))))

	if release :

		if ball_pos.y > screen.get_height() - ball_radius:
			ball_pos.y = screen.get_height() - ball_radius
			ball_velocity.y *= -damping_factor
		elif ball_pos.y < ball_radius:
			ball_pos.y = ball_radius
			ball_velocity.y *= -damping_factor

		if  ball_pos.x > screen.get_width() - ball_radius:
			ball_pos.x = screen.get_width() - ball_radius
			ball_velocity.x *= -damping_factor 
		elif ball_pos.x < ball_radius:
			ball_pos.x = ball_radius
			ball_velocity.x *= -damping_factor

		ball_pos.x += ball_velocity.x * dt
		ball_pos.y += ball_velocity.y * dt
		ball_velocity.y += GRAVITY


	#print(angle_radians )
	pygame.draw.circle(screen,"black",ball_pos,ball_radius)


				
	
	pygame.display.flip()
	dt = clock.tick(60)/1000

pygame.quit()