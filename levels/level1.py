import pygame
import random
from settings import WIN, WIDTH, HEIGHT, FPS, BG_COLOR, METEOR_COLOR, ORB_COLOR, ENERGY_BAR_COLOR, WHITE

pygame.init()

def run_level1():
    clock = pygame.time.Clock()

    # Player
    player_x = 100
    player_y = HEIGHT // 2
    player_w = 50
    player_h = 50
    player_speed = 5

    # Energy bar
    energy = 0
    score = 0

    # Meteors and Orbs
    meteors = []
    meteor_timer = 0
    meteor_interval = 50

    orbs = []
    orb_timer = 0
    orb_interval = 130

    game_over = False

    while True:
        clock.tick(FPS)
        WIN.fill(BG_COLOR)

        # EVENTS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        # MOVEMENT
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            player_y -= player_speed
        if keys[pygame.K_DOWN]:
            player_y += player_speed

        player_y = max(0, min(HEIGHT - player_h, player_y))

        # SPAWN METEORS
        meteor_timer += 1
        if meteor_timer >= meteor_interval:
            m_y = random.randint(0, HEIGHT - 40)
            meteors.append([WIDTH, m_y, 40, 40])
            meteor_timer = 0

        # SPAWN ORBS
        orb_timer += 1
        if orb_timer >= orb_interval:
            o_y = random.randint(20, HEIGHT - 20)
            orbs.append([WIDTH, o_y, 20])
            orb_timer = 0

        # MOVE OBJECTS
        for m in meteors:
            m[0] -= 6

        for o in orbs:
            o[0] -= 5

        # REMOVE OFF-SCREEN
        meteors = [m for m in meteors if m[0] + m[2] > 0]
        orbs = [o for o in orbs if o[0] + o[2] > 0]

        # COLLISIONS
        player_rect = pygame.Rect(player_x, player_y, player_w, player_h)

        for m in meteors:
            if player_rect.colliderect(pygame.Rect(m[0], m[1], m[2], m[3])):
                pygame.time.delay(1000)
                return False   # FAIL

        for o in orbs[:]:
            if player_rect.colliderect(pygame.Rect(o[0], o[1], o[2], o[2])):
                energy += 5
                orbs.remove(o)

        # INCREASE ENERGY SLOWLY
        energy += 0.1

        # LEVEL COMPLETE CHECK
        if energy >= 100:
            return True

        # DRAW PLAYER
        pygame.draw.rect(WIN, WHITE, (player_x, player_y, player_w, player_h))

        # DRAW METEORS
        for m in meteors:
            pygame.draw.ellipse(WIN, METEOR_COLOR, (m[0], m[1], m[2], m[3]))

        # DRAW ORBS
        for o in orbs:
            pygame.draw.circle(WIN, ORB_COLOR, (int(o[0] + o[2]/2), int(o[1] + o[2]/2)), o[2] // 2)

        # ENERGY BAR
        pygame.draw.rect(WIN, WHITE, (10, 10, 200, 20), 2)
        pygame.draw.rect(WIN, ENERGY_BAR_COLOR, (12, 12, 2 * energy, 16))

        pygame.display.update()
