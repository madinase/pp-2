import pygame

class Ball:
    def __init__(self, x, y, radius, color, screen_width, screen_height):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.sw = screen_width
        self.sh = screen_height

    def move(self, keys, step):
        if keys[pygame.K_LEFT] and self.x - step >= self.radius:
            self.x -= step
        if keys[pygame.K_RIGHT] and self.x + step <= self.sw - self.radius:
            self.x += step
        if keys[pygame.K_UP] and self.y - step >= self.radius:
            self.y -= step
        if keys[pygame.K_DOWN] and self.y + step <= self.sh - self.radius:
            self.y += step

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)