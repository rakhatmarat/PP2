import pygame
import random

GRID_SIZE = 20
GRID_WIDTH = 20
GRID_HEIGHT = 15
INITIAL_SPEED = 5
SPEED_INCREMENT = 1 
FOOD_SCORE = 1
LEVEL_THRESHOLD = 3
FOOD_TIMER_MAX = 30  # Maximum timer value for food

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

pygame.init()

WINDOW_WIDTH = GRID_WIDTH * GRID_SIZE
WINDOW_HEIGHT = GRID_HEIGHT * GRID_SIZE
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Snake Game")

class Snake:
    def __init__(self):
        self.body = [(5, 5)]
        self.direction = (1, 0)
        self.speed = INITIAL_SPEED
        self.should_grow = False  

    def move(self):
        x, y = self.body[0]
        dx, dy = self.direction
        new_head = (x + dx, y + dy)

        if not (0 <= new_head[0] < GRID_WIDTH) or not (0 <= new_head[1] < GRID_HEIGHT):
            return False 
        
        if new_head in self.body:
            return False

        self.body.insert(0, new_head)

        if self.should_grow:
            self.should_grow = False
        else:
            self.body.pop()

        return True

    def change_direction(self, direction):
        if (direction[0] * -1, direction[1] * -1) != self.direction:
            self.direction = direction

    def grow(self):
        self.should_grow = True

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(window, GREEN, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

class Food:
    def __init__(self):
        self.position = self.generate_position()
        self.timer = FOOD_TIMER_MAX  # Set timer for food disappearance

    def generate_position(self):
        while True:
            x = random.randint(0, GRID_WIDTH - 1)
            y = random.randint(0, GRID_HEIGHT - 1)
            return x, y

    def draw(self):
        pygame.draw.rect(window, RED, (self.position[0] * GRID_SIZE, self.position[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

    def update_timer(self):
        self.timer -= 1
        if self.timer <= 0:
            self.position = self.generate_position()  # Reset food position
            self.timer = FOOD_TIMER_MAX  # Reset timer

snake = Snake()
food = None  # Only one food object at a time
score = 0
level = 1

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.change_direction((0, -1))
            elif event.key == pygame.K_DOWN:
                snake.change_direction((0, 1))
            elif event.key == pygame.K_LEFT:
                snake.change_direction((-1, 0))
            elif event.key == pygame.K_RIGHT:
                snake.change_direction((1, 0))

    if not snake.move():
        running = False 

    # Check if snake ate the food
    if food and snake.body[0] == food.position:
        snake.grow()
        score += FOOD_SCORE
        if score >= LEVEL_THRESHOLD * level:
            level += 1
            snake.speed += SPEED_INCREMENT
        food = None  # Remove the eaten food

    # Generate new food if no food is present
    if not food:
        food = Food()

    # Update food timer
    if food:
        food.update_timer()

    window.fill(WHITE)

    snake.draw()
    if food:
        food.draw()

    pygame.display.flip()

    pygame.time.Clock().tick(snake.speed)

pygame.quit()
