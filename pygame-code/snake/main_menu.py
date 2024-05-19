class MainMenu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)
        self.title_font = pygame.font.Font(None, 72)
        self.title_text = self.title_font.render("Snake Game", True, (255, 255, 255))
        self.play_text = self.font.render("Play", True, (255, 255, 255))
        self.quit_text = self.font.render("Quit", True, (255, 255, 255))
        self.play_rect = self.play_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
        self.quit_rect = self.quit_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 50))
        self.selected_option = "play"

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.title_text, (self.screen.get_width() // 2 - self.title_text.get_width() // 2, 50))
        self.screen.blit(self.play_text, self.play_rect)
        self.screen.blit(self.quit_text, self.quit_rect)

    def update(self):
        if self.selected_option == "play":
            self.play_text = self.font.render("Play", True, (255, 255, 255))
            self.quit_text = self.font.render("Quit", True, (200, 200, 200))
        else:
            self.play_text = self.font.render("Play", True, (200, 200, 200))
            self.quit_text = self.font.render("Quit", True, (255, 255, 255))
        self.play_rect = self.play_text.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2))
        self.quit_rect = self.quit_text.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2 + 50))

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                self.selected_option = "play" if self.selected_option == "quit" else "quit"
            elif event.key == pygame.K_RETURN:
                return self.selected_option
        return None

#Starting game instance
def main():
    pygame.init()
    WIDTH = 500
    HEIGHT = 500
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    main_menu = MainMenu(screen)
    game_instance = game(WIDTH,HEIGHT)
    in_menu = True
    menu_action = None

    while in_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                in_menu = False
            menu_action = main_menu.handle_event(event)
            if menu_action == "play":
                in_menu = False

        main_menu.update()
        main_menu.draw()
        pygame.display.flip()
        clock.tick(30)

    if menu_action == "play":
        game_instance.start_game()

    pygame.quit()


if __name__ == "__main__":
    main()