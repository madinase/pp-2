import pygame
from ball import Ball

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

FPS = 60
def main():
    ball = Ball(x= WIDTH // 2, y= HEIGHT // 2, radius=20, color = RED, screen_height= HEIGHT, screen_width= WIDTH)
    step = 20

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen.fill(WHITE)

        keys = pygame.key.get_pressed()
        ball.move(keys, step)
        ball.draw(screen)

        pygame.display.flip()
        clock.tick(FPS) 

    pygame.quit()

if __name__ == "__main__":
    main()