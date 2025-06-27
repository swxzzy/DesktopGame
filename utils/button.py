import pygame
import os
hover_sound = None
click_sound = None
hover_played = set()
def load_sounds(volume):
    global hover_sound, click_sound
    hover_sound = pygame.mixer.Sound("assets/sounds/hover.wav")
    click_sound = pygame.mixer.Sound("assets/sounds/click.wav")
    hover_sound.set_volume(volume)
    click_sound.set_volume(volume)
class Button:
    def __init__(self, text, x, y, width, height, color, hover_color, font, text_color=(255, 255, 255)):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.hover_color = hover_color
        self.font = font
        self.text_color = text_color
        self.hovered = False
    def draw(self, screen):
        global hover_played
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, self.hover_color, self.rect)
            if id(self) not in hover_played:
                if hover_sound:
                    hover_sound.play()
                hover_played.add(id(self))
        else:
            pygame.draw.rect(screen, self.color, self.rect)
            hover_played.discard(id(self))
        pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)
        text_surf = self.font.render(self.text, True, self.text_color)
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)
    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            if click_sound:
                click_sound.play()
            return True
        return False