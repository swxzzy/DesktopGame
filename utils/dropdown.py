import pygame
class Dropdown:
    def __init__(self, x, y, width, height, font, options, selected, label=""):
        self.rect = pygame.Rect(x, y, width, height)
        self.font = font
        self.options = options
        self.selected = selected
        self.label = label
        self.expanded = False
        self.bg_color = (80, 80, 80)
        self.hover_color = (120, 120, 120)
        self.text_color = (255, 255, 255)
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.expanded = not self.expanded
                return True
            elif self.expanded:
                for i, option in enumerate(self.options):
                    option_rect = pygame.Rect(self.rect.x, self.rect.y + (i + 1) * self.rect.height, self.rect.width, self.rect.height)
                    if option_rect.collidepoint(event.pos):
                        self.selected = option
                        self.expanded = False
                        return True
                self.expanded = False
        return False
    def draw(self, screen):
        if self.label:
            label_surface = self.font.render(self.label, True, self.text_color)
            screen.blit(label_surface, (self.rect.x, self.rect.y - 30))
        pygame.draw.rect(screen, self.bg_color, self.rect)
        text_surface = self.font.render(self.selected, True, self.text_color)
        screen.blit(text_surface, (self.rect.x + 10, self.rect.y + 5))
        pygame.draw.rect(screen, self.text_color, self.rect, 2)
        if self.expanded:
            for i, option in enumerate(self.options):
                option_rect = pygame.Rect(self.rect.x, self.rect.y + (i + 1) * self.rect.height, self.rect.width, self.rect.height)
                pygame.draw.rect(screen, self.hover_color if option == self.selected else self.bg_color, option_rect)
                opt_surface = self.font.render(option, True, self.text_color)
                screen.blit(opt_surface, (option_rect.x + 10, option_rect.y + 5))
                pygame.draw.rect(screen, self.text_color, option_rect, 1)
    def get_selected(self):
        return self.selected