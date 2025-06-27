import pygame
import config
from utils.button import Button
from utils.text_input import TextInput
import auth
def login_screen(screen, font):
    clock = pygame.time.Clock()
    button_x = 100
    button_width = 300
    spacing = 70
    button_y = 300
    login_button = Button("Войти", button_x, button_y, button_width, 50,
                          config.COLORS["button"], config.COLORS["button_hover"], font)
    register_button = Button("Регистрация", button_x, button_y + spacing, button_width, 50,
                             config.COLORS["button"], config.COLORS["button_hover"], font)
    username_input = TextInput(500, 300, 300, "", font, "Логин")
    password_input = TextInput(500, 380, 300, "", font, "Пароль", password=True)
    error = ""
    while True:
        screen.fill(config.COLORS["background"])
        try:
            bg = pygame.image.load("assets/bg_login.png")
            screen.blit(pygame.transform.scale(bg, screen.get_size()), (0, 0))
        except:
            pass
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            username_input.handle_event(event)
            password_input.handle_event(event)
            if login_button.is_clicked(event):
                if auth.login(username_input.text, password_input.text):
                    return "choose_mode"
                else:
                    error = "Неверный логин или пароль"
            if register_button.is_clicked(event):
                if auth.register(username_input.text, password_input.text):
                    return "choose_mode"
                else:
                    error = "Ошибка регистрации (возможно, пользователь существует)"
        username_input.draw(screen)
        password_input.draw(screen)
        login_button.draw(screen)
        register_button.draw(screen)
        if error:
            error_text = font.render(error, True, (255, 0, 0))
            screen.blit(error_text, (500, 460))
        pygame.display.flip()
        clock.tick(config.FPS)
