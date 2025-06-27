import pygame
import config
from utils.button import Button, load_sounds
from utils.slider import Slider
from utils.text_input import TextInput
from utils.dropdown import Dropdown
from settings_manager import save_settings, load_settings
from utils.mode_manager import get_mode
def settings_screen(screen, font):
    clock = pygame.time.Clock()
    settings = load_settings()
    resolution_options = ["2560x1440", "1920x1080", "1600x900", "1280x720"]
    resolution_str = f"{settings['resolution']['width']}x{settings['resolution']['height']}"
    mode = get_mode()
    button_x = 100
    button_width = 220
    button_y = 200
    spacing = 70
    fullscreen = settings["fullscreen"]
    fullscreen_button = Button("Полный экран" if fullscreen else "Оконный режим", button_x, button_y + spacing * 0, button_width, 50, config.COLORS["button"], config.COLORS["button_hover"], font)
    apply_button = Button("Применить", button_x, button_y + spacing * 1, button_width, 50, config.COLORS["button"], config.COLORS["button_hover"], font)
    back_button = Button("Назад", button_x, button_y + spacing * 2, button_width, 50, config.COLORS["button"], config.COLORS["button_hover"], font)
    ctrl_x = 500
    music_slider = Slider(ctrl_x, 200, 400, 20, settings.get('volume_music', 80), "Музыка")
    effects_slider = Slider(ctrl_x, 260, 400, 20, settings.get('volume_effects', 80), "Эффекты")
    fps_input = TextInput(ctrl_x, 330, 200, str(settings.get('fps', 60)), font, "FPS")
    resolution_dropdown = Dropdown(ctrl_x, 400, 200, 40, font, resolution_options, resolution_str, "Разрешение")
    while True:
        screen.fill(config.COLORS["background"])
        try:
            if mode == "TMNT":
                bg = pygame.image.load("assets/bg_settings_tmnt.png")
                screen.blit(pygame.transform.scale(bg, screen.get_size()), (0, 0))
            else:
                bg = pygame.image.load("assets/bg_settings_sm.png")
                screen.blit(pygame.transform.scale(bg, screen.get_size()), (0, 0))
        except:
            pass
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            if back_button.is_clicked(event):
                return "main_menu"
            if fullscreen_button.is_clicked(event):
                fullscreen = not fullscreen
                fullscreen_button.text = "Полный экран" if fullscreen else "Оконный режим"
            if apply_button.is_clicked(event):
                width, height = map(int, resolution_dropdown.get_selected().split("x"))
                new_fps = int(fps_input.text) if fps_input.text.isdigit() else 60
                new_settings = {
                    "volume_music": music_slider.value,
                    "volume_effects": effects_slider.value,
                    "fps": new_fps,
                    "fullscreen": fullscreen,
                    "resolution": {"width": width, "height": height},
                    "theme": settings.get("theme", "default")
                }
                save_settings(new_settings)
                config.settings.update(new_settings)
                load_sounds(effects_slider.value / 100.0)
                config.WIDTH = width
                config.HEIGHT = height
                config.FULLSCREEN = fullscreen
                config.FPS = new_fps
                flags = pygame.FULLSCREEN if fullscreen else 0
                pygame.display.set_mode((width, height), flags)
                pygame.mixer.music.set_volume(music_slider.value / 100.0)
            music_slider.handle_event(event)
            effects_slider.handle_event(event)
            fps_input.handle_event(event)
            resolution_dropdown.handle_event(event)
        music_slider.draw(screen, font)
        effects_slider.draw(screen, font)
        fps_input.draw(screen)
        resolution_dropdown.draw(screen)
        fullscreen_button.draw(screen)
        apply_button.draw(screen)
        back_button.draw(screen)
        pygame.display.flip()
        clock.tick(config.FPS)
