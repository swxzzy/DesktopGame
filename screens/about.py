import pygame
import config
from utils.button import Button
import webbrowser
from utils.mode_manager import get_mode
def authors_screen(screen, font):
    clock = pygame.time.Clock()
    mode = get_mode()
    button_x = 100
    button_y = 200
    button_width = 300
    spacing = 70
    git_button = Button("GitHub", button_x, button_y, button_width, 50, config.COLORS["button"], config.COLORS["button_hover"], font)
    site_button = Button("Официальный сайт",button_x, button_y + spacing, button_width, 50, config.COLORS["button"], config.COLORS["button_hover"], font)
    back_button = Button("Назад", button_x, button_y + spacing * 2, button_width, 50, config.COLORS["button"], config.COLORS["button_hover"], font)
    while True:
        screen.fill(config.COLORS["background"])
        try:
            if mode == "TMNT":
                bg = pygame.image.load("assets/bg_about_tmnt.png")
                screen.blit(pygame.transform.scale(bg, screen.get_size()), (0, 0))
            else:
                bg = pygame.image.load("assets/bg_about_sm.png")
                screen.blit(pygame.transform.scale(bg, screen.get_size()), (0, 0))
        except:
            pass
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            if git_button.is_clicked(event):
                webbrowser.open("https://github.com/swxzzy")
            if site_button.is_clicked(event):
                webbrowser.open("index.html")
            if back_button.is_clicked(event):
                return "main_menu"
        center_x = screen.get_width() // 2
        pygame.draw.rect(screen, (0, 0, 0, 100), (center_x - 150, 150, 500, 200), border_radius=12)
        lines = [
            "Автор: Лячин Денис ИС-141",
            "Движок: Pygame",
            "Версия игры: 1.0"
        ]
        for i, line in enumerate(lines):
            text = font.render(line, True, config.COLORS["text"])
            text_rect = text.get_rect(center=(center_x + 150, 180 + i * 50))
            screen.blit(text, text_rect)
        git_button.draw(screen)
        site_button.draw(screen)
        back_button.draw(screen)
        pygame.display.flip()
        clock.tick(config.FPS)
