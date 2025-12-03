import pygame
import random
import os
from settings import WIN, WIDTH, HEIGHT, FPS, BG_COLOR, WHITE, ENERGY_BAR_COLOR, ORB_COLOR, YELLOW

pygame.init()

# Load spaceship avatar
AVATAR_IMG = pygame.image.load(os.path.join("images", "abstract_avatar.png"))
AVATAR_IMG = pygame.transform.scale(AVATAR_IMG, (60, 60))

def run_level2():
    clock = pygame.time.Clock()

    # Player properties
    player_x, player_y = 100, HEIGHT // 2
    player_width, player_height = 60, 60
    player_speed = 6

    # Energy and score
    energy = 0
    score = 0

    # Obstacles
    planets = []
    blackholes = []
    planet_timer = 0
    blackhole_timer = 0
    obstacle_interval = 90  # frames
    blackhole_interval = 300  # frames

    # Collectibles
    orbs = []
    orb_timer = 0
    orb_interval = 150

    running = True
    while running:
        clock.tick(FPS)
        WIN.fill(BG_COLOR)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        keys = pygame.key.get_pressed()
        # Move player up/down
        if keys[pygame.K_UP]:
            player_y -= player_speed
        if keys[pygame.K_DOWN]:
            player_y += player_speed
        player_y = max(0, min(HEIGHT - player_height, player_y))

        # Spawn planets
        planet_timer += 1
        if planet_timer >= obstacle_interval:
            planet_y = random.randint(0, HEIGHT - 80)
            planets.append([WIDTH, planet_y, random.randint(50, 120), random.randint(50, 120)])
            planet_timer = 0

        # Spawn blackholes
        blackhole_timer += 1
        if blackhole_timer >= blackhole_interval:
            bh_y = random.randint(0, HEIGHT - 80)
            blackholes.append([WIDTH, bh_y, 50])
            blackhole_timer = 0

        # Spawn orbs
        orb_timer += 1
        if orb_timer >= orb_interval:
            orb_y = random.randint(20, HEIGHT - 20)
            orbs.append([WIDTH, orb_y, 20])
            orb_timer = 0

        # Move obstacles and collectibles left
        for p in planets:
            p[0] -= 5
        for bh in blackholes:
            bh[0] -= 4
        for orb in orbs:
            orb[0] -= 5

        # Remove off-screen objects
        planets = [p for p in planets if p[0] + p[2] > 0]
        blackholes = [bh for bh in blackholes if bh[0] + bh[2] > 0]
        orbs = [o for o in orbs if o[0] + o[2] > 0]

        # Collision detection
        player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
        for p in planets:
            if player_rect.colliderect(pygame.Rect(p[0], p[1], p[2], p[3])):
                pygame.time.delay(1000)
                return False  # Game over
        for bh in blackholes:
            if player_rect.colliderect(pygame.Rect(bh[0], bh[1], bh[2], bh[2])):
                pygame.time.delay(1000)
                return False  # Game over
        for orb in orbs[:]:
            if player_rect.colliderect(pygame.Rect(orb[0], orb[1], orb[2], orb[2])):
                energy += 5
                orbs.remove(orb)

        # Increase energy gradually
        energy += 0.05
        if energy >= 100:
            return True  # Level complete

        # Increase score
        score += 1 / FPS

        # Draw player
        WIN.blit(AVATAR_IMG, (player_x, player_y))

        # Draw planets
        for p in planets:
            pygame.draw.ellipse(WIN, (150, 50, 50), (p[0], p[1], p[2], p[3]))

        # Draw blackholes
        for bh in blackholes:
            pygame.draw.circle(WIN, (0, 0, 0), (int(bh[0]+bh[2]/2), int(bh[1]+bh[2]/2)), bh[2]//2)

        # Draw orbs
        for o in orbs:
            pygame.draw.circle(WIN, ORB_COLOR, (int(o[0]+o[2]/2), int(o[1]+o[2]/2)), o[2]//2)

        # Draw energy bar
        pygame.draw.rect(WIN, WHITE, (10, 10, 200, 20), 2)
        pygame.draw.rect(WIN, ENERGY_BAR_COLOR, (12, 12, 2*energy, 16))

        # Draw score
        font = pygame.font.SysFont(None, 30)
        score_text = font.render(f"Score: {int(score)}", True, YELLOW)
        WIN.blit(score_text, (WIDTH-130, 10))

        pygame.display.update()
