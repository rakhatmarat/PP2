import pygame
import sys

pygame.init()

screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Moving Ball")

WHITE = (255, 255, 255)
RED = (255, 0, 0)

ball_radius = 25
ball_x, ball_y = screen_width // 2, screen_height // 2 

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ball_y = max(ball_y - 20, ball_radius) 
            elif event.key == pygame.K_DOWN:
                ball_y = min(ball_y + 20, screen_height - ball_radius) 
            elif event.key == pygame.K_LEFT:
                ball_x = max(ball_x - 20, ball_radius) 
            elif event.key == pygame.K_RIGHT:
                ball_x = min(ball_x + 20, screen_width - ball_radius)  

    screen.fill(WHITE)

    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)

    pygame.display.update()

pygame.quit()
sys.exit()
