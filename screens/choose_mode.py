import pygame
import config
from utils.button import Button
from utils import mode_manager
def choose_mode_screen(screen, font):
    clock = pygame.time.Clock()
    button_x = 100
    button_width = 300
    spacing = 70
    button_y = 300
    tmnt_button = Button("Черепашки-ниндзя", button_x, button_y, button_width, 50, config.COLORS["button"], config.COLORS["button_hover"], font)
    spiderman_button = Button("Человек-паук", button_x, button_y + spacing, button_width, 50, config.COLORS["button"], config.COLORS["button_hover"], font)
    while True:
        screen.fill(config.COLORS["background"])
        try:
            bg = pygame.image.load("assets/bg_choose.png")
            screen.blit(pygame.transform.scale(bg, screen.get_size()), (0, 0))
        except:
            pass
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            if tmnt_button.is_clicked(event):
                mode_manager.set_mode("TMNT")
                return "main_menu"
            if spiderman_button.is_clicked(event):
                mode_manager.set_mode("Spider-Man")
                return "main_menu"
        tmnt_button.draw(screen)
        spiderman_button.draw(screen)
        pygame.display.flip()
        clock.tick(config.FPS)