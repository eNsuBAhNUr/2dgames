import pygame
import random

pygame.init()
WIDTH, HEIGHT = 600, 400
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mode A - Side Runner")

WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

clock = pygame.time.Clock()
FPS = 60

# Player
player_radius = 25
player_x = 100
player_y = HEIGHT - 75
player_vel_y = 0
gravity = 0.8
jump_strength = -15
is_jumping = False

# Ground
ground_y = HEIGHT - 50

# Obstacles
obstacles = []
OB_W, OB_H = 30, 50
obstacle_timer = 0
obstacle_interval = 100

# Score
score = 0
font = pygame.font.SysFont(None, 36)

game_over = False

def reset():
    global player_x, player_y, player_vel_y, is_jumping
    global obstacles, score, obstacle_timer, game_over
    player_x, player_y = 100, HEIGHT - 75
    player_vel_y = 0
    is_jumping = False
    obstacles = []
    score = 0
    obstacle_timer = 0
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

    if not game_over:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and not is_jumping:
            player_vel_y = jump_strength
            is_jumping = True

        # Gravity
        player_vel_y += gravity
        player_y += player_vel_y

        # Ground collision
        if player_y >= ground_y - player_radius:
            player_y = ground_y - player_radius
            is_jumping = False
            player_vel_y = 0

        # Add new obstacles
        obstacle_timer += 1
        if obstacle_timer >= obstacle_interval:
            obstacles.append([WIDTH, ground_y - OB_H])
            obstacle_timer = 0

        # Move obstacles
        for o in obstacles:
            o[0] -= 5

        # Remove off-screen
        obstacles = [o for o in obstacles if o[0] + OB_W > 0]

        # Collision detection
        for o in obstacles:
            if (player_x + player_radius > o[0] and
                player_x - player_radius < o[0] + OB_W and
                player_y + player_radius > o[1]):

                game_over = True
                break

        score += 1/FPS

    # DRAW
    WIN.fill(WHITE)

    pygame.draw.rect(WIN, GREEN, (0, ground_y, WIDTH, 50))
    pygame.draw.circle(WIN, BLUE, (int(player_x), int(player_y)), player_radius)

    for o in obstacles:
        pygame.draw.rect(WIN, RED, (o[0], o[1], OB_W, OB_H))

    score_text = font.render(f"Score: {int(score)}", True, BLACK)
    WIN.blit(score_text, (10, 10))

    if game_over:
        over_text = font.render("GAME OVER - Press R to Restart", True, RED)
        WIN.blit(over_text, (80, HEIGHT//2))

    pygame.display.update()

pygame.quit()
