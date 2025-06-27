import pygame
import config
from utils.button import Button
from utils.dropdown import Dropdown
from utils.mode_manager import get_mode
def play_ai_screen(screen, font):
    clock = pygame.time.Clock()
    mode = get_mode()
    button_x = 100
    button_y = 200
    button_width = 300
    spacing = 70
    play_button = Button("Играть", button_x, button_y, button_width, 50, config.COLORS["button"], config.COLORS["button_hover"], font)
    back_button = Button("Назад", button_x, button_y + spacing, button_width, 50, config.COLORS["button"], config.COLORS["button_hover"], font)
    dropdown = Dropdown(
        x=button_x + button_width + 40,
        y=button_y,
        width=150,
        height=40,
        font=font,
        options=["1"],
        selected="1",
        label="Противников"
    )
    while True:
        screen.fill(config.COLORS["background"])
        try:
            if mode == "TMNT":
                bg = pygame.image.load("assets/bg_gameai_tmnt.png")
                screen.blit(pygame.transform.scale(bg, screen.get_size()), (0, 0))
            else:
                bg = pygame.image.load("assets/bg_gameai_sm.png")
                screen.blit(pygame.transform.scale(bg, screen.get_size()), (0, 0))
        except Exception:
            pass
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            if play_button.is_clicked(event):
                num_opponents = int(dropdown.get_selected())
                screen.fill((0, 0, 0))
                text = font.render("Создание лобби...", True, (255, 255, 255))
                screen.blit(text, (
                    config.WIDTH // 2 - text.get_width() // 2,
                    config.HEIGHT // 2 - text.get_height() // 2))
                pygame.display.flip()
                pygame.time.delay(3000)
                return "play_ai", num_opponents
            if back_button.is_clicked(event):
                return "play_menu"
            dropdown.handle_event(event)
        dropdown.draw(screen)
        play_button.draw(screen)
        back_button.draw(screen)
        pygame.display.flip()
        clock.tick(config.FPS)