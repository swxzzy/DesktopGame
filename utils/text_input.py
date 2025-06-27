import pygame
class TextInput:
    def __init__(self, x, y, width, text, font, placeholder="", password=False):
        self.rect = pygame.Rect(x, y, width, 40)
        self.color_inactive = (180, 180, 180)
        self.color_active = (255, 255, 255)
        self.text = text
        self.font = font
        self.active = False
        self.placeholder = placeholder
        self.password = password
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.active = self.rect.collidepoint(event.pos)
        elif event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            elif event.key == pygame.K_RETURN:
                pass  # optionally handle submit
            else:
                if len(self.text) < 20:
                    self.text += event.unicode
    def draw(self, screen):
        pygame.draw.rect(screen, self.color_active if self.active else self.color_inactive, self.rect, 2)
        if self.text:
            display_text = '*' * len(self.text) if self.password else self.text
        else:
            display_text = self.placeholder
        text_surface = self.font.render(display_text, True, (255, 255, 255))
        screen.blit(text_surface, (self.rect.x + 5, self.rect.y + 7))
