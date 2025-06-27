import pygame
from settings_manager import load_settings
settings = load_settings()
pygame.init()
info = pygame.display.Info()
WIDTH = info.current_w
HEIGHT = info.current_h
FULLSCREEN = True
FPS = settings.get("fps", 60)
THEMES = {
    "TMNT": {
        "button": (128, 153, 0),
        "button_hover": (160, 200, 0),
        "background": (30, 40, 20),
        "text": (255, 255, 255)
    },
    "Spider-Man": {
        "button": (198, 59, 56),
        "button_hover": (255, 80, 70),
        "background": (30, 10, 10),
        "text": (255, 255, 255)
    },
    "default": {
        "button": (102, 0, 153),
        "button_hover": (153, 51, 255),
        "background": (20, 20, 40),
        "text": (255, 255, 255)
    }
}
COLORS = THEMES.get(settings.get("theme", "default"), THEMES["default"])
def update_theme_colors(mode):
    global COLORS
    COLORS = THEMES.get(mode, THEMES["default"])
def apply_volume():
    pygame.mixer.music.set_volume(settings.get("volume_music", 80) / 100.0)
pygame.mixer.init()
apply_volume()
