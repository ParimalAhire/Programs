from typing import IO
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
GRAVITY = 0.5

#Sling Properties
slingshot_pos = (200, HEIGHT - 100)
slingshot_radius = 30
pull_back_length = 100

#Ball Properties
ball_radius = 15
ball_color = RED
ball_pos = slingshot_pos

#sling mechanics variables
is_pulling_back = False
pull_back_distance = 0
angle = 0

clock = pygame.time.Clock()
running = True

while running:
	screen.fill(WHITE)

	#Event Handling
	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				is_pulling_back = True
		elif event.type == pygame.MOUSEBUTTONUP:
			if event.button == 1:
				is_pulling_back = False
				ball_speed = min(pull_back_distance, pull_back_length)
				angle_radians = math.radians(angle)
				ball_velocity = (ball_speed * math.cos(angle_radians), - ball_speed * math.sin(angle_radians))
				
	
	pygame.display.flip()
	clock.tick(60)

pygame.quit()