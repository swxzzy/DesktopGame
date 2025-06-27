import json
import os
SETTINGS_FILE = "settings.json"
default_settings = {
    "volume_music": 50,
    "volume_effects": 50,
    "fps": 60,
    "fullscreen": False,
    "resolution": {
        "width": 1280,
        "height": 720
    }
}
def load_settings():
    if not os.path.exists(SETTINGS_FILE):
        save_settings(default_settings)
        return default_settings
    try:
        with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return default_settings
def save_settings(settings):
    with open(SETTINGS_FILE, "w", encoding="utf-8") as f:
        json.dump(settings, f, indent=4)