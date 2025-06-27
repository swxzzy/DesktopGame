import pygame
import random
import config
from utils.button import Button
from utils.mode_manager import get_mode
CARDS_SPIDERMAN = [
    {"name": "Доктор Дум",   "интеллект": 424, "сила": 282, "ловкость": 350, "умения": 413, "навыки": 271, "image": "doom.png"},
    {"name": "Человек-лёд",  "интеллект": 126, "сила": 114, "ловкость": 203, "умения": 327, "навыки": 146, "image": "ice_man.png"},
    {"name": "Гвен Стейси",  "интеллект": 139, "сила": 83,  "ловкость": 137, "умения": 25,  "навыки": 32,  "image": "gwen.png"},
    {"name": "Гризли",       "интеллект": 123, "сила": 245, "ловкость": 143, "умения": 72,  "навыки": 202, "image": "greezly.png"},
    {"name": "Женщина-паук", "интеллект": 137, "сила": 230, "ловкость": 199, "умения": 265, "навыки": 276, "image": "spider_woman.png"},
    {"name": "Белый кролик", "интеллект": 124, "сила": 99,  "ловкость": 136, "умения": 72,  "навыки": 84,  "image": "white_rabbit.png"},
    {"name": "Дядюшка Бен",  "интеллект": 130, "сила": 71,  "ловкость": 112, "умения": 54,  "навыки": 68,  "image": "ben.png"},
    {"name": "Водяной",      "интеллект": 74,  "сила": 96,  "ловкость": 136, "умения": 243, "навыки": 142, "image": "water.png"},
]
CARDS_TMNT = [
    {"name": "Леонардо",     "сила": 9500, "ловкость": 9200, "мастерство": 9250, "смекалка": 8250, "image": "leonardo.png"},
    {"name": "Донателло",    "сила": 9250, "ловкость": 9250, "мастерство": 9000, "смекалка": 9600, "image": "donatello.png"},
    {"name": "Сплинтер",     "сила": 8000, "ловкость": 9000, "мастерство": 7000, "смекалка": 9500, "image": "splinter.png"},
    {"name": "Сила черепашек",      "сила": 9999, "ловкость": 9750, "мастерство": 9999, "смекалка": 9750, "image": "turtles_power.png"},
    {"name": "Юные черепашки",        "сила": 50, "ловкость": 60, "мастерство": 70, "смекалка": 50, "image": "young_tmnt.png"},
    {"name": "Эльфинатор",  "сила": 7200, "ловкость": 7855, "мастерство": 6575, "смекалка": 7000, "image": "elfinator.png"},
]
CHARACTERISTICS = {
    "Spider-Man": ["интеллект", "сила", "ловкость", "умения", "навыки"],
    "TMNT": ["сила", "ловкость", "мастерство", "смекалка"]
}
HAT_IMAGE = {
    "Spider-Man": "assets/cards/sm_hat.png",
    "TMNT": "assets/cards/tmnt_hat.png"
}
BG_IMAGE = {
    "Spider-Man": "assets/bg_game_sm.png",
    "TMNT": "assets/bg_game_tmnt.png"
}
def play_match_screen(screen, font, num_opponents=1):
    pygame.mixer.music.stop()
    clock = pygame.time.Clock()
    mode = get_mode()
    cards = CARDS_TMNT if mode == "TMNT" else CARDS_SPIDERMAN
    deck = random.sample(cards, 6)
    ai_deck = random.sample(cards, 6)
    characteristics = CHARACTERISTICS[mode]
    hat_image_path = HAT_IMAGE[mode]
    bg_path = BG_IMAGE[mode]
    popup_button = None
    game_over = False
    mode = get_mode()
    if mode == "TMNT":
        pygame.mixer.music.load("assets/sounds/game_music_tmnt.mp3")
        pygame.mixer.music.play(-1)
    else:
        pygame.mixer.music.load("assets/sounds/game_music_sm.mp3")
        pygame.mixer.music.play(-1)
    turn = random.choice(["player", "ai"])
    ai_card = None
    ai_char = None
    selected_card = None
    selected_char = None
    result_text = ""
    char_buttons = [
        Button(c.title(), config.WIDTH - 200, (config.HEIGHT - 300) + i*60, 160, 40,
               config.COLORS["button"], config.COLORS["button_hover"], font)
        for i, c in enumerate(characteristics)
    ]
    def draw_card(card, pos):
        try:
            img = pygame.image.load(f"assets/cards/{card['image']}")
            img = pygame.transform.scale(img, (150, 190))
            screen.blit(img, pos)
        except:
            pygame.draw.rect(screen, (60, 60, 60), (*pos, 100, 140))
    def draw_hat(pos):
        try:
            hat = pygame.image.load(hat_image_path)
            hat = pygame.transform.scale(hat, (150, 190))
            screen.blit(hat, pos)
        except:
            pygame.draw.rect(screen, (30, 30, 30), (*pos, 100, 140))
    def draw_popup(text):
        nonlocal popup_button
        x, y, w, h = config.WIDTH//2 - 200, config.HEIGHT//2 - 100, 400, 200
        pygame.draw.rect(screen, (20, 20, 20), (x, y, w, h))
        pygame.draw.rect(screen, (255, 255, 255), (x, y, w, h), 2)
        t = font.render(text, True, (255, 255, 255))
        screen.blit(t, (x + (w - t.get_width())//2, y + 40))
        popup_button = Button("В главное меню", x+100, y+120, 200, 40,
                              config.COLORS["button"], config.COLORS["button_hover"], font)
        popup_button.draw(screen)
    while True:
        screen.fill(config.COLORS["background"])
        try:
            bg = pygame.image.load(bg_path)
            bg = pygame.transform.scale(bg, (config.WIDTH, config.HEIGHT))
            screen.blit(bg, (0, 0))
        except:
            pass
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            if game_over and popup_button and popup_button.is_clicked(event):
                return "main_menu"
            if event.type == pygame.MOUSEBUTTONDOWN and turn == "player":
                for idx, card in enumerate(deck):
                    row, col = divmod(idx, 6)
                    x = 150 + col*120
                    y = config.HEIGHT - 260 - row*150
                    if pygame.Rect(x, y, 150, 190).collidepoint(event.pos):
                        selected_card = card
                        break
                if selected_card and not selected_char:
                    for i, btn in enumerate(char_buttons):
                        if btn.is_clicked(event):
                            selected_char = characteristics[i]
                            break
        if turn == "ai" and ai_card is None:
            if ai_deck:
                ai_card = ai_deck.pop(0)
                ai_char = max(characteristics, key=lambda c: ai_card[c])
            turn = "player"
            selected_card = None
            selected_char = None
        if selected_card and selected_char:
            if ai_card is None and ai_deck:
                ai_card = ai_deck.pop(0)
            p_val = selected_card[selected_char]
            a_val = ai_card[selected_char]
            playoff_pile = [selected_card, ai_card]
            deck.remove(selected_card)
            if p_val > a_val:
                result_text = f"Вы выиграли: {p_val} > {a_val}"
                deck.extend(playoff_pile)
                turn = "player"
            elif a_val > p_val:
                result_text = f"ИИ выиграл: {a_val} > {p_val}"
                ai_deck.extend(playoff_pile)
                turn = "ai"
            else:
                result_text = f"Ничья: {p_val} = {a_val}"
            ai_card = None
            selected_card = None
            selected_char = None
        for idx, card in enumerate(deck):
            row, col = divmod(idx, 6)
            draw_card(card, (150 + col*120, config.HEIGHT - 260 - row*150))
        for idx in range(len(ai_deck)):
            row, col = divmod(idx, 6)
            draw_hat((150 + col*120, 20 + row*150))
        if selected_card:
            draw_card(selected_card, (config.WIDTH//2 - 150, config.HEIGHT//2 - 100))
            bx, by = config.WIDTH//2 + 10, config.HEIGHT//2 - 100
            pygame.draw.rect(screen, (0,0,0), (bx, by, 220, 200))
            pygame.draw.rect(screen, (255,255,255), (bx, by, 220, 200), 2)
            txt = font.render(selected_card["name"], True, (255,255,255))
            screen.blit(txt, (bx + (220 - txt.get_width())//2, by + 5))
            y = by + 40
            for char in characteristics:
                line = f"{char}: {selected_card[char]}"
                screen.blit(font.render(line, True, (220,220,220)), (bx+10, y))
                y += 30
        if turn == "player" and selected_card and not selected_char:
            for btn in char_buttons:
                btn.draw(screen)
        if ai_card:
            draw_card(ai_card, (config.WIDTH // 2 - 150, 100))
            txt = font.render(ai_card["name"], True, (255, 255, 255))
            bx, by = config.WIDTH // 2 + 10, 100
            pygame.draw.rect(screen, (0, 0, 0), (bx, by, 220, 200))
            pygame.draw.rect(screen, (255, 255, 255), (bx, by, 220, 200), 2)
            screen.blit(txt, (bx + (220 - txt.get_width()) // 2, by + 5))
            y = by + 40
            for char in characteristics:
                line = f"{char}: {ai_card[char]}"
                screen.blit(font.render(line, True, (220,220,220)), (bx+10, y))
                y += 30
        if result_text:
            surf = font.render(result_text, True, config.COLORS["text"])
            screen.blit(surf, ((config.WIDTH - surf.get_width())//2, 40))
        if not deck:
            game_over = True
            pygame.mixer.music.stop()
            draw_popup("Вы проиграли!")
        elif not ai_deck:
            game_over = True
            pygame.mixer.music.stop()
            draw_popup("Вы выиграли!")
        pygame.display.flip()
        clock.tick(config.FPS)