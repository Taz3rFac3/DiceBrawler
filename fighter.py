import pygame

class Fighter():
    def __init__(self, x, y):
        self.rect = pygame.Rect((x, y, 80, 180))

    def move(self, screen_width):
        SPEED = 10
        dx = 0
        dy = 0

        #get key presses
        key = pygame.key.get_pressed()

        #movement
        if key[pygame.K_a]:
            dx = -SPEED
        if key[pygame.K_d]:
            dx = SPEED

        #keep player on scren
        if self.rect.left + dx < 0:
            dx = 0 - self.rect.left
        if self.rect.right + dx > screen_width:
            dx = screen_width - self.rect.right

        #update player position
        self.rect.x += dx
        self.rect.y += dy



    def draw(self, surface):
        pygame.draw.rect(surface, (255,0,0), self.rect)
