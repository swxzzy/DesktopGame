import pygame
from game import run_game
import config
from utils.button import load_sounds
from settings_manager import load_settings
def main():
    pygame.init()
    pygame.mixer.init()
    settings = load_settings()
    music_volume = settings.get("volume_music", 80) / 100
    effects_volume = settings.get("volume_effects", 80) / 100
    pygame.mixer.music.set_volume(music_volume)
    load_sounds(effects_volume)
    info = pygame.display.Info()
    config.WIDTH, config.HEIGHT = info.current_w, info.current_h
    config.FULLSCREEN = True
    screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT), pygame.FULLSCREEN)
    icon = pygame.image.load("assets/icon.png")
    pygame.display.set_icon(icon)
    pygame.display.set_caption("Heroes & Villains & Way of the Warrior")
    font = pygame.font.SysFont(None, 32)
    run_game(screen, font)
if __name__ == "__main__":
    main()