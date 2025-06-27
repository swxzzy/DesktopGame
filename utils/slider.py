import pygame
class Slider:
    def __init__(self, x, y, width, height, value, label, min_val=0, max_val=100):
        self.rect = pygame.Rect(x, y, width, height)
        self.value = value
        self.label = label
        self.min_val = min_val
        self.max_val = max_val
        self.handle_radius = 10
        self.dragging = False
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self._handle_rect().collidepoint(event.pos):
                self.dragging = True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.dragging = False
        elif event.type == pygame.MOUSEMOTION and self.dragging:
            rel_x = event.pos[0] - self.rect.x
            rel_x = max(0, min(rel_x, self.rect.width))
            self.value = int(self.min_val + (rel_x / self.rect.width) * (self.max_val - self.min_val))
    def draw(self, screen, font):
        pygame.draw.rect(screen, (180, 180, 180), self.rect)
        filled_width = int((self.value - self.min_val) / (self.max_val - self.min_val) * self.rect.width)
        pygame.draw.rect(screen, (255, 255, 255), (self.rect.x, self.rect.y, filled_width, self.rect.height))
        handle_x = self.rect.x + filled_width
        pygame.draw.circle(screen, (255, 255, 255), (handle_x, self.rect.centery), self.handle_radius)
        label_surf = font.render(f"{self.label}: {self.value}", True, (255, 255, 255))
        screen.blit(label_surf, (self.rect.x, self.rect.y - 30))
    def _handle_rect(self):
        handle_x = self.rect.x + int((self.value - self.min_val) / (self.max_val - self.min_val) * self.rect.width)
        return pygame.Rect(handle_x - self.handle_radius, self.rect.centery - self.handle_radius,
                           self.handle_radius * 2, self.handle_radius * 2)