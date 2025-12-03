import pygame
import random

pygame.init()
WIDTH, HEIGHT = 600, 400
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mode B - POV Driving (Time Score)")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

clock = pygame.time.Clock()
FPS = 60

# Player
player_w, player_h = 40, 40
player_x = WIDTH//2 - 20
player_y = HEIGHT - 60
player_speed = 7

# Obstacles
obstacles = []
OB_W, OB_H = 50, 70
obstacle_speed = 4
spawn_timer = 0
spawn_interval = 60

# Score (time-based like Mode A)
score = 0
font = pygame.font.SysFont(None, 36)

game_over = False

def reset():
    global obstacles, score, player_x, player_y
    global obstacle_speed, spawn_timer, game_over

    player_x = WIDTH//2 - 20
    player_y = HEIGHT - 60

    obstacles = []
    score = 0
    obstacle_speed = 4
    spawn_timer = 0
    game_over = False

running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if game_over and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                reset()

    keys = pygame.key.get_pressed()

    if not game_over:
        # Movement
        if keys[pygame.K_LEFT]:
            player_x -= player_speed
        if keys[pygame.K_RIGHT]:
            player_x += player_speed

        # Boundaries
        player_x = max(0, min(WIDTH - player_w, player_x))

        # Spawn obstacles
        spawn_timer += 1
        if spawn_timer >= spawn_interval:
            x = random.randint(0, WIDTH - OB_W)
            obstacles.append([x, -OB_H])
            spawn_timer = 0

        # Increase obstacle speed over time
        obstacle_speed += 0.002

        # Move obstacles
        for o in obstacles:
            o[1] += obstacle_speed

        # Remove off-screen
        obstacles = [o for o in obstacles if o[1] < HEIGHT + 200]

        # Collision detection
        for o in obstacles:
            if (player_x < o[0] + OB_W and
                player_x + player_w > o[0] and
                player_y < o[1] + OB_H and
                player_y + player_h > o[1]):
                game_over = True
                break

        # TIME-BASED score (same as Mode A)
        score += 1 / FPS

    # DRAW
    WIN.fill(WHITE)

    pygame.draw.rect(WIN, BLUE, (player_x, player_y, player_w, player_h))

    for o in obstacles:
        pygame.draw.rect(WIN, RED, (o[0], o[1], OB_W, OB_H))

    score_text = font.render(f"Score: {int(score)}", True, BLACK)
    WIN.blit(score_text, (10, 10))

    if game_over:
        over_text = font.render("GAME OVER - Press R to Restart", True, RED)
        WIN.blit(over_text, (80, HEIGHT//2))

    pygame.display.update()

pygame.quit()
