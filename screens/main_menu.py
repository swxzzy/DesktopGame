import pygame
import config
from utils.button import Button
from utils.mode_manager import get_mode
import os
def main_menu_screen(screen, font):
    clock = pygame.time.Clock()
    mode = get_mode()
    config.update_theme_colors(mode)
    bg_path = {
        "TMNT": "assets/bg_mainmenu_tmnt.png",
        "Spider-Man": "assets/bg_mainmenu_sm.png"
    }.get(mode, "assets/bg_mainmenu.png")
    play_button = Button("Играть", 100, 300, 300, 60, config.COLORS["button"], config.COLORS["button_hover"], font)
    change_mode_button = Button("Сменить режим", 100, 380, 300, 60, config.COLORS["button"], config.COLORS["button_hover"], font)
    settings_button = Button("Настройки", 100, 460, 300, 60, config.COLORS["button"], config.COLORS["button_hover"], font)
    about_button = Button("Авторы", 100, 540, 300, 60, config.COLORS["button"], config.COLORS["button_hover"], font)
    quit_button = Button("Выход", 100, 620, 300, 60, config.COLORS["button"], config.COLORS["button_hover"], font)
    title = f"{mode}" if mode else "Главное меню"
    while True:
        screen.fill(config.COLORS["background"])
        if os.path.exists(bg_path):
            bg = pygame.image.load(bg_path)
            screen.blit(pygame.transform.scale(bg, screen.get_size()), (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            if play_button.is_clicked(event):
                return "play_menu"
            if change_mode_button.is_clicked(event):
                return "choose_mode"
            if settings_button.is_clicked(event):
                return "settings"
            if about_button.is_clicked(event):
                return "about"
            if quit_button.is_clicked(event):
                return "quit"
        title_surface = font.render(title, True, config.COLORS["text"])
        screen.blit(title_surface, (100, 200))
        play_button.draw(screen)
        change_mode_button.draw(screen)
        settings_button.draw(screen)
        about_button.draw(screen)
        quit_button.draw(screen)
        pygame.display.flip()
        clock.tick(config.FPS)
def show_wip(screen, font):
    clock = pygame.time.Clock()
    text = "Режим в разработке..."
    timer = 0
    while timer < 90:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
        screen.fill((0, 0, 0))
        text_surface = font.render(text, True, (255, 255, 255))
        screen.blit(text_surface, (
            screen.get_width() // 2 - text_surface.get_width() // 2,
            screen.get_height() // 2 - text_surface.get_height() // 2))
        pygame.display.flip()
        clock.tick(60)
        timer += 1
    return "main_menu"
