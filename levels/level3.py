import pygame
import random
import time
import os

# Import shared settings from the main settings file
from settings import (
    WIN, WIDTH, HEIGHT, FPS,
    BG_COLOR, METEOR_COLOR, ORB_COLOR,
    ENERGY_BAR_COLOR, WHITE
)

# Optional sound generation (only if numpy exists)
try:
    import numpy as np
    HAS_NUMPY = True
except:
    HAS_NUMPY = False

pygame.mixer.init() if pygame.mixer.get_init() is None else None


def make_tone(freq=440, duration=0.12, volume=0.5):
    if not HAS_NUMPY:
        return None
    sr = 44100
    t = np.linspace(0, duration, int(sr * duration), False)
    wave = np.sin(freq * 2 * np.pi * t)
    audio = (wave * (32767 * volume)).astype(np.int16)
    stereo = np.column_stack((audio, audio))
    return pygame.sndarray.make_sound(stereo)


HIT_SND  = make_tone(180, 0.18, 0.8)
ORB_SND  = make_tone(1000, 0.06, 0.4)
WIN_SND  = make_tone(1200, 0.20, 0.5)


# Load avatar if exists next to settings
AVATAR_PATH = os.path.join("images", "abstract_avatar.png")
if os.path.exists(AVATAR_PATH):
    AVATAR_IMG = pygame.image.load(AVATAR_PATH).convert_alpha()
else:
    AVATAR_IMG = None


def clamp(v, a, b):
    return max(a, min(b, v))


# ================================================================
#                           LEVEL 3
# ================================================================
def run_level3():
    clock = pygame.time.Clock()

    # Player starting position
    player_x, player_y = WIDTH // 2, HEIGHT - 160
    pw, ph = 64, 64
    speed = 5  # stays constant

    MIN_SIZE = 30
    MAX_SIZE = 150

    energy = 0
    display_energy = 0

    meteors = []
    orbs = []

    meteor_timer = 0
    meteor_interval = 45

    orb_timer = 0
    orb_interval = 120

    shake_time = 0
    shake_mag = 0

    start = time.time()

    while True:
        dt = clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        keys = pygame.key.get_pressed()

        # Movement (speed unchanged)
        if keys[pygame.K_LEFT]:
            player_x -= speed
        if keys[pygame.K_RIGHT]:
            player_x += speed

        # Zoom in/out effect
        if keys[pygame.K_UP]:
            pw *= 1.02
            ph *= 1.02
            pw = min(pw, MAX_SIZE)
            ph = min(ph, MAX_SIZE)

        if keys[pygame.K_DOWN]:
            pw *= 0.98
            ph *= 0.98
            pw = max(pw, MIN_SIZE)
            ph = max(ph, MIN_SIZE)

        # Stay in screen
        player_x = clamp(player_x, 0, WIDTH - pw)
        player_y = clamp(player_y, 0, HEIGHT - ph)

        # Difficulty scaling
        elapsed = time.time() - start
        meteor_speed = 4 + elapsed * 0.03

        # Spawn meteors
        meteor_timer += 1
        if meteor_timer >= meteor_interval:
            size = random.randint(30, 70)
            x = random.randint(0, WIDTH - size)
            meteors.append([x, -size, size, meteor_speed])
            meteor_timer = 0
            meteor_interval = max(18, int(meteor_interval * 0.992))

        # Spawn orbs
        orb_timer += 1
        if orb_timer >= orb_interval:
            ox = random.randint(30, WIDTH - 30)
            orbs.append([ox, -20, 20, 4])
            orb_timer = 0

        # Move objects
        for m in meteors:
            m[1] += m[3]
        for o in orbs:
            o[1] += o[3]

        meteors = [m for m in meteors if m[1] < HEIGHT + 80]
        orbs = [o for o in orbs if o[1] < HEIGHT + 40]

        # Collision detection
        prect = pygame.Rect(player_x, player_y, pw, ph)

        # Meteor hits
        got_hit = False
        for m in meteors:
            if prect.colliderect(pygame.Rect(m[0], m[1], m[2], m[2])):
                got_hit = True
                break

        if got_hit:
            if HIT_SND: HIT_SND.play()
            shake_time = 0.5
            shake_mag = 8
            energy = max(0, energy - 12)

        # Orb collection
        for o in orbs[:]:
            if prect.colliderect(pygame.Rect(o[0], o[1], o[2], o[2])):
                orbs.remove(o)
                energy = min(100, energy + 10)
                if ORB_SND: ORB_SND.play()

        # Passive energy
        energy = min(100, energy + 0.015)
        display_energy += (energy - display_energy) * 0.08

        # Draw frame
        WIN.fill(BG_COLOR)

        # Screen shake
        sx = sy = 0
        if shake_time > 0:
            shake_time -= dt / 1000
            sx = random.randint(-shake_mag, shake_mag)
            sy = random.randint(-shake_mag, shake_mag)
            shake_mag = max(0, shake_mag - 1)

        # Draw meteors
        for m in meteors:
            pygame.draw.ellipse(WIN, METEOR_COLOR,
                                (m[0] + sx, m[1] + sy, m[2], m[2]))

        # Draw orbs
        for o in orbs:
            pygame.draw.circle(WIN, ORB_COLOR,
                               (o[0] + sx, o[1] + sy), o[2] // 2)

        # Draw player (avatar or rectangle)
        if AVATAR_IMG:
            scaled = pygame.transform.scale(AVATAR_IMG, (int(pw), int(ph)))
            WIN.blit(scaled, (player_x + sx, player_y + sy))
        else:
            pygame.draw.rect(WIN, WHITE,
                             (player_x + sx, player_y + sy, pw, ph))

        # Energy bar
        pygame.draw.rect(WIN, WHITE, (10, 10, 240, 20), 2)
        pygame.draw.rect(
            WIN, ENERGY_BAR_COLOR,
            (12, 12, int(display_energy * 2.36), 16)
        )

        pygame.display.update()

        # Win condition
        if energy >= 100:
            if WIN_SND: WIN_SND.play()
            pygame.time.delay(800)
            return True
