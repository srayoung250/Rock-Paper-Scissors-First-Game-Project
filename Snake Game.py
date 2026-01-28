import sys
import random
import pygame

# Snake Game - minimal pygame implementation
# Save as "Snake Game.py" and run with: python "Snake Game.py"

# Config
CELL = 20
COLS, ROWS = 32, 24
WIDTH, HEIGHT = COLS * CELL, ROWS * CELL
FPS = 8
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
GRAY = (40, 40, 40)

def random_food(snake):
    while True:
        pos = (random.randrange(COLS), random.randrange(ROWS))
        if pos not in snake:
            return pos

def draw_grid(surface):
    for x in range(0, WIDTH, CELL):
        pygame.draw.line(surface, GRAY, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, CELL):
        pygame.draw.line(surface, GRAY, (0, y), (WIDTH, y))

def draw_block(surface, color, pos):
    r = pygame.Rect(pos[0]*CELL, pos[1]*CELL, CELL, CELL)
    pygame.draw.rect(surface, color, r)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 28)

    def reset():
        head = (COLS // 2, ROWS // 2)
        snake = [head, (head[0]-1, head[1]), (head[0]-2, head[1])]
        direction = (1, 0)
        food = random_food(snake)
        return snake, direction, food, 0, False

    snake, direction, food, score, game_over = reset()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit(); sys.exit()
                if not game_over:
                    if event.key in (pygame.K_w, pygame.K_UP) and direction != (0, 1):
                        direction = (0, -1)
                    elif event.key in (pygame.K_s, pygame.K_DOWN) and direction != (0, -1):
                        direction = (0, 1)
                    elif event.key in (pygame.K_a, pygame.K_LEFT) and direction != (1, 0):
                        direction = (-1, 0)
                    elif event.key in (pygame.K_d, pygame.K_RIGHT) and direction != (-1, 0):
                        direction = (1, 0)
                else:
                    if event.key == pygame.K_r:
                        snake, direction, food, score, game_over = reset()
                    elif event.key == pygame.K_q:
                        pygame.quit(); sys.exit()

        if not game_over:
            # move snake
            head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
            # check wall collision
            if not (0 <= head[0] < COLS and 0 <= head[1] < ROWS) or head in snake:
                game_over = True
            else:
                snake.insert(0, head)
                if head == food:
                    score += 1
                    food = random_food(snake)
                else:
                    snake.pop()

        screen.fill(BLACK)
        draw_grid(screen)
        draw_block(screen, RED, food)
        for segment in snake:
            draw_block(screen, GREEN, segment)

        score_surf = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_surf, (8, 8))

        if game_over:
            go_surf = font.render("GAME OVER - R to restart, Q to quit", True, WHITE)
            rect = go_surf.get_rect(center=(WIDTH//2, HEIGHT//2))
            screen.blit(go_surf, rect)

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()