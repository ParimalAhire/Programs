import pygame

pygame.init()

#Constants
WIDTH = 500
HEIGHT = 500
MOVEMENT = 5
FPS = 60

Screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()

class snake():
	def __init__(self, start_pos):
		start_pos = pygame.Vector2(start_pos)
		self.segments = [start_pos,(start_pos.x,start_pos.y)]
		self.direction = pygame.K_RIGHT

	def new_segment(self, next_pos):
		self.segments.insert(0, next_pos)

	def move(self):
		next_pos = pygame.Vector2(self.segments[0])

		if self.direction == pygame.K_LEFT:
			next_pos.x -= MOVEMENT
		elif self.direction == pygame.K_RIGHT:
			next_pos.x += MOVEMENT
		elif self.direction == pygame.K_UP:
			next_pos.y -= MOVEMENT
		elif self.direction == pygame.K_DOWN:
			next_pos.y += MOVEMENT

		self.new_segment(next_pos)

		if not (self.wall_collision(next_pos)):
			self.segments.pop()
		else:
			self.segments.pop()
			self.reset_position()

	def load_snake(self, snake_image):
		for pos in self.segments:
			pos = pygame.Vector2(pos)
			Screen.blit(snake_image, (pos.x, pos.y))

	def reset_position(self):
		self.segments.insert(0,(WIDTH//2,HEIGHT//2))
		self.direction = pygame.K_RIGHT

	def wall_collision(self, next_pos):

		if next_pos.x > WIDTH or next_pos.x < 0 or next_pos.y > HEIGHT or next_pos.y < 0:
			return True
		return False

	def self_collision(self):
		self.unique = set(tuple(seg) for seg in self.segments)

		if len(self.unique) != len(self.segments):
			return True
		return False 


class game(snake):

	def start_game(self):

		start_pos = pygame.Vector2(WIDTH//2, HEIGHT//2)
		self.snake = snake(start_pos)

		running = True

		snake_image = pygame.image.load("images/snake_yellow_blob_64.png")
		snake_image = pygame.transform.scale(snake_image, (10, 10))

		while running:

			for event in pygame.event.get():

				if event.type == pygame.QUIT:
					running = False

				elif event.type == pygame.KEYDOWN:

					if event.key == pygame.K_LEFT and self.snake.direction != pygame.K_RIGHT:
						self.snake.direction = pygame.K_LEFT
					elif event.key == pygame.K_RIGHT and self.snake.direction != pygame.K_LEFT:
						self.snake.direction = pygame.K_RIGHT
					elif event.key == pygame.K_UP and self.snake.direction != pygame.K_DOWN:
						self.snake.direction = pygame.K_UP
					elif event.key == pygame.K_DOWN and self.snake.direction != pygame.K_UP:
						self.snake.direction = pygame.K_DOWN

			self.snake.move()

			Screen.fill((0,0,0)) 

			if self.snake.self_collision():
				running = False

			self.snake.load_snake(snake_image)

			Screen.blit(snake_image, self.snake.segments[0])

			pygame.display.flip()
			clock.tick(FPS)

		pygame.quit()


game_instance = game((0,0))
game_instance.start_game()	