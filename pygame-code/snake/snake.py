import pygame
import random

pygame.init()

#Constants
WIDTH = 500
HEIGHT = 500
MOVEMENT = 5
FPS = 30
IMGX = 15
IMGY = 15

Screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()

class snake():

	#Initiaizing the snake element
	def __init__(self, start_pos):
		self.snake_body = pygame.image.load("assets/snake_yellow_blob_64.png")
		self.snake_body = pygame.transform.scale(self.snake_body, (IMGX, IMGY ))

		self.snake_head = pygame.image.load("assets/snake_yellow_head_64.png")
		self.snake_head = pygame.transform.scale(self.snake_head, (IMGX, IMGY))

		#Snake Segment
		self.segments = [start_pos,(start_pos.x,start_pos.y)]
		self.direction = pygame.K_RIGHT 	#Snake Initial Direction 

	#Snake Segment (Collection of snake body)
	def new_segment(self, next_pos):
		self.segments.insert(0, next_pos)

	#Snake movement (Adding new movement point to snake segment(body))
	def move(self, growth):
		next_pos = pygame.Vector2(self.segments[0])

		if self.direction == pygame.K_LEFT:
			next_pos.x -= MOVEMENT
		elif self.direction == pygame.K_RIGHT:
			next_pos.x += MOVEMENT
		elif self.direction == pygame.K_UP:
			next_pos.y -= MOVEMENT
		elif self.direction == pygame.K_DOWN:
			next_pos.y += MOVEMENT

		#Screen Loop
		next_pos.x %= WIDTH
		next_pos.y %= HEIGHT

		#Adding new snake segment
		self.new_segment(next_pos)

		if not growth:
			self.segments.pop()

		growth = False

		#if (self.wall_collision(next_pos)):
		#	self.reset_position()

	#Rendering the snake
	def load_snake(self, snake_head, snake_body):

		for pos in reversed(self.segments[1:]):
			pos = pygame.Vector2(pos)
			Screen.blit(snake_body, (pos.x, pos.y))

		Screen.blit(snake_head, (self.segments[0][0],self.segments[0][1]))

	#Getting head position
	def get_head_position(self):
		return self.segments[0]

	#def reset_position(self):

	#	self.segments.insert(0,(WIDTH//2,HEIGHT//2))
	#	self.direction = pygame.K_RIGHT

	#Checking if the snake goes off the screen
	def wall_collision(self, next_pos):

		if next_pos.x > WIDTH - IMGX or next_pos.x < 0 or next_pos.y > HEIGHT - IMGY or next_pos.y < 0:
			return True
		return False

	#Checking if the snake collides with itself
	def self_collision(self):
		self.unique = set(tuple(seg) for seg in self.segments)

		if len(self.unique) != len(self.segments):
			return True
		return False 

	#Checking if the snake collided with the apple
	def apple_collision(self,apple_pos):
		if (self.segments[0][0],self.segments[0][1]) == apple_pos :
			return True

		return False

class apple():

	#Initializing Apple Element
    def __init__(self):
        self.apple_green_img = pygame.image.load("assets/apple_green_64.png")
        self.apple_green_img = pygame.transform.scale(self.apple_green_img, (IMGX, IMGY))

        self.apple_red_img = pygame.image.load("assets/apple_red_64.png")
        self.apple_red_img = pygame.transform.scale(self.apple_red_img, (IMGX,IMGY))

        self.apple = self.apple_green_img
        self.apple_pos = (WIDTH // 2, HEIGHT // 2)

    #Spawning apple
    def spawn_apple(self,snake_head_pos ):
        
        #Creating new element only if the snake collides with the first apple
        if self.apple_collision(snake_head_pos):
            x = random.randint(0, WIDTH - IMGX)
            y = random.randint(0, HEIGHT - IMGY)
            self.apple_pos = (x, y)
            self.fruit_selection()
            return True

        return False

    #Check if the snake collides with the apple
    def apple_collision(self, snake_head_pos):
        
        #Check if the snake comes around the Image width and length and determine if they collided
        if abs(self.apple_pos[0] - snake_head_pos[0]) <= IMGX and abs(self.apple_pos[1] - snake_head_pos[1]) <= IMGY:
            return True
        return False

    #Render the apple
    def load_apple(self):
        Screen.blit(self.apple, self.apple_pos)

    def fruit_selection(self):
        probability = random.randint(1,5)
        if probability == 5:
            self.apple = self.apple_red_img
        else:
       		self.apple = self.apple_green_img

class game():

	#initializing the game element
	def __init__(self,WIDTH,HEIGHT):

		self.growth = False 	#Growth Flag

		start_pos = pygame.Vector2(WIDTH//2, HEIGHT//2) 	#starting position of snake
		self.snake = snake(start_pos)			#snake instance
		self.apple = apple()				#apple instance

		#Game Background
		self.background_image = pygame.image.load("assets/background_game3.png")
		self.background_image = pygame.transform.scale(self.background_image, (WIDTH,HEIGHT))

	#Game function
	def start_game(self):

		running = True 

		#Game Loop
		while running:

			for event in pygame.event.get():

				if event.type == pygame.QUIT:	#Game quit
					running = False

				elif event.type == pygame.KEYDOWN:	#Key Pressed

					#Navigation Key Condition
					if event.key == pygame.K_LEFT and self.snake.direction != pygame.K_RIGHT:
						self.snake.direction = pygame.K_LEFT
					elif event.key == pygame.K_RIGHT and self.snake.direction != pygame.K_LEFT:
						self.snake.direction = pygame.K_RIGHT
					elif event.key == pygame.K_UP and self.snake.direction != pygame.K_DOWN:
						self.snake.direction = pygame.K_UP
					elif event.key == pygame.K_DOWN and self.snake.direction != pygame.K_UP:
						self.snake.direction = pygame.K_DOWN

			#Insert next point in the snake segment
			self.snake.move(self.growth)

			#Refreshing the background Image
			Screen.blit(self.background_image, (0, 0))
			#Screen.fill((0,0,0))

			#Checking self collision
			if self.snake.self_collision():
				running = False

			#Obtaining the head point
			head = self.snake.get_head_position()
			
			#Spawn the apple and check collision and return if the snake has growth or not
			self.growth = self.apple.spawn_apple(head)

			#Render the snake and apple
			self.snake.load_snake(self.snake.snake_head,self.snake.snake_body)
			self.apple.load_apple()

			pygame.display.flip()
			clock.tick(FPS)

		pygame.quit()

#Starting game instance
#game_instance = game(WIDTH,HEIGHT)
#game_instance.start_game()	


running = True

def main_menu():
    pygame.init()
    game_instance = game(WIDTH,HEIGHT)
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Main Menu")
    running = True
    

    font = pygame.font.Font(None, 74)
    text_play = font.render("Play", True, (255, 0, 0))
    text_play_rect = text_play.get_rect(center=(WIDTH//2, HEIGHT*0.4))
    text_quit = font.render("Quit", True, (255, 0, 0))
    text_quit_rect = text_quit.get_rect(center=(WIDTH//2, HEIGHT*0.6))

    while running:

      
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if text_play_rect.collidepoint(event.pos):
                    print("play is clicked pressed")
                    game_instance.start_game()
                if text_quit_rect.collidepoint(event.pos):
                    print("quit button is clicked")
                    pygame.quit()

        screen.fill((0, 0, 255))
        screen.blit(text_play, text_play_rect)
        screen.blit(text_quit, text_quit_rect)
        rectangle = pygame.Rect(300, 250, 200, 80)

        # Set the border color
        border_color = (255,255,255)

        pygame.draw.rect(screen, border_color, rectangle, 1)

        rectangle1=pygame.Rect(300,350,200,80)
        border_color1=(255,255,255)
        pygame.draw.rect(screen,border_color1,rectangle1,1)

        pygame.display.flip()

main_menu()
pygame.quit()