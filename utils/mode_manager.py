_current_mode = None  # "TMNT" или "Spider-Man"
def set_mode(mode):
    global _current_mode
    _current_mode = mode
def get_mode():
    return _current_mode