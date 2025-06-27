import pygame
import config
import settings_manager
import pygame.mixer
from screens.login import login_screen
from screens.choose_mode import choose_mode_screen
from screens.main_menu import main_menu_screen
from screens.settings import settings_screen
from screens.about import authors_screen
from screens.play_menu import play_menu_screen
from screens.play_ai import play_ai_screen
from logic.play_ai_logic import play_match_screen
from utils.mode_manager import get_mode
current_music_path = None
def play_music(path):
    global current_music_path
    if current_music_path == path:
        return  # музыка уже играет — не перезапускаем
    try:
        pygame.mixer.music.stop()
        pygame.mixer.music.load(path)
        pygame.mixer.music.play(-1)
        current_music_path = path
    except:
        print("Ошибка загрузки музыки:", path)
def run_game(screen, font):
    current_screen = "login"
    mode = get_mode()
    while True:
        if current_screen == "login":
            result = login_screen(screen, font)
        elif current_screen == "choose_mode":
            result = choose_mode_screen(screen, font)
            mode = get_mode()
            if mode == "TMNT":
                play_music("assets/sounds/menu_music_tmnt.mp3")
            else:
                play_music("assets/sounds/menu_music_sm.mp3")
        elif current_screen == "main_menu":
            result = main_menu_screen(screen, font)
            mode = get_mode()
            if mode == "TMNT":
                play_music("assets/sounds/menu_music_tmnt.mp3")
            else:
                play_music("assets/sounds/menu_music_sm.mp3")
        elif current_screen == "settings":
            result = settings_screen(screen, font)
            mode = get_mode()
            if mode == "TMNT":
                play_music("assets/sounds/menu_music_tmnt.mp3")
            else:
                play_music("assets/sounds/menu_music_sm.mp3")
        elif current_screen == "about":
            result = authors_screen(screen, font)
            mode = get_mode()
            if mode == "TMNT":
                play_music("assets/sounds/menu_music_tmnt.mp3")
            else:
                play_music("assets/sounds/menu_music_sm.mp3")
        elif current_screen == "play_menu":
            result = play_menu_screen(screen, font)
        elif isinstance(current_screen, tuple) and current_screen[0] == "play_ai":
            result = play_match_screen(screen, font)
            pygame.mixer.music.stop()
            mode = get_mode()
            if mode == "TMNT":
                play_music("assets/sounds/game_music_tmnt.mp3")
            else:
                play_music("assets/sounds/game_music_sm.mp3")
        elif current_screen == "play_ai":
            result = play_ai_screen(screen, font)
            mode = get_mode()
            if mode == "TMNT":
                play_music("assets/sounds/menu_music_tmnt.mp3")
            else:
                play_music("assets/sounds/menu_music_sm.mp3")
        elif current_screen == "quit":
            pygame.quit()
            return
        else:
            print(f"Неизвестный экран: {current_screen}")
            pygame.quit()
            return
        if result is None:
            current_screen = "quit"
        else:
            current_screen = result