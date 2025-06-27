import pygame
import config
from utils.button import Button
from utils import mode_manager
from utils.mode_manager import get_mode
def play_menu_screen(screen, font):
    clock = pygame.time.Clock()
    mode = get_mode()
    button_x = 100
    button_width = 300
    button_y = 200
    spacing = 70
    play_ai_button = Button("Игра против ИИ", button_x, button_y + spacing * 0, button_width, 50, config.COLORS["button"], config.COLORS["button_hover"], font)
    #host_button = Button("Создать лобби", button_x, button_y + spacing * 1, button_width, 50, config.COLORS["button"], config.COLORS["button_hover"], font)
    back_button = Button("Назад", button_x, button_y + spacing * 1, button_width, 50, config.COLORS["button"], config.COLORS["button_hover"], font)
    current_mode = mode_manager.get_mode()
    while True:
        screen.fill(config.COLORS["background"])
        try:
            if mode == "TMNT":
                bg = pygame.image.load("assets/bg_play_tmnt.png")
                screen.blit(pygame.transform.scale(bg, screen.get_size()), (0, 0))
            else:
                bg = pygame.image.load("assets/bg_play_sm.png")
                screen.blit(pygame.transform.scale(bg, screen.get_size()), (0, 0))
        except:
            pass
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            if back_button.is_clicked(event):
                return "main_menu"
            #if host_button.is_clicked(event):
                #pass
            if play_ai_button.is_clicked(event):
                return "play_ai"
        play_ai_button.draw(screen)
        #host_button.draw(screen)
        back_button.draw(screen)
        pygame.display.flip()
        clock.tick(config.FPS)
def show_notice(screen, font, message):
    overlay = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 180))
    screen.blit(overlay, (0, 0))
    text = font.render(message, True, (255, 255, 255))
    rect = text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
    screen.blit(text, rect)
    pygame.display.flip()
    pygame.time.wait(1500)