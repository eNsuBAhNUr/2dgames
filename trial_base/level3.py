import pygame
import random
import os
import time

WIDTH, HEIGHT = 900, 600
FPS = 60
BG_COLOR = (10, 10, 25)
METEOR_COLOR = (255, 80, 80)
ORB_COLOR = (80, 180, 255)
ENERGY_BAR_COLOR = (80, 255, 120)
WHITE = (255, 255, 255)

pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("LEVEL 1 — TEST BUILD")


# -------------------------
# OPTIONAL SOUND SUPPORT
# -------------------------
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


# -------------------------
# LOAD AVATAR (OPTIONAL)
# -------------------------
AVATAR_PATH = "abstract_avatar.png"

if os.path.exists(AVATAR_PATH):
    AVATAR_IMG = pygame.image.load(AVATAR_PATH).convert_alpha()
else:
    AVATAR_IMG = None


def clamp(v, a, b):
    return max(a, min(b, v))



# ============================================================
#                    LEVEL 1 TEST FUNCTION
# ============================================================
def run_level1_test():
    clock = pygame.time.Clock()

    player_x, player_y = WIDTH // 2, HEIGHT - 160
    pw, ph = 64, 64   # starting size
    speed = 5         # movement stays the SAME always

    MIN_SIZE = 30
    MAX_SIZE = 150

    energy = 0
    display_energy = 0

    meteors = []
    orbs = []

    meteor_timer = 0
    meteor_interval = 50

    orb_timer = 0
    orb_interval = 140

    shake_time = 0
    shake_mag = 0

    start = time.time()

    while True:
        dt = clock.tick(FPS)

        # -------------------------
        # EVENT
        # -------------------------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        keys = pygame.key.get_pressed()

        # -------------------------
        # MOVEMENT (speed unchanged)
        # -------------------------
        if keys[pygame.K_LEFT]:
            player_x -= speed
        if keys[pygame.K_RIGHT]:
            player_x += speed
        if keys[pygame.K_UP]:
            # ZOOM IN (grow)
            pw *= 1.02
            ph *= 1.02
            pw = min(pw, MAX_SIZE)
            ph = min(ph, MAX_SIZE)
        if keys[pygame.K_DOWN]:
            # ZOOM OUT (shrink)
            pw *= 0.98
            ph *= 0.98
            pw = max(pw, MIN_SIZE)
            ph = max(ph, MIN_SIZE)

        # clamp inside screen with new size
        player_x = clamp(player_x, 0, WIDTH - pw)
        player_y = clamp(player_y, 0, HEIGHT - ph)

        # -------------------------
        # DIFFICULTY SCALING
        # -------------------------
        elapsed = time.time() - start
        meteor_speed = 4 + elapsed * 0.02

        # -------------------------
        # SPAWN METEORS
        # -------------------------
        meteor_timer += 1
        if meteor_timer >= meteor_interval:
            size = random.randint(30, 70)
            x = random.randint(0, WIDTH - size)
            meteors.append([x, -size, size, meteor_speed])
            meteor_timer = 0
            meteor_interval = max(20, int(meteor_interval * 0.995))

        # -------------------------
        # SPAWN ORBS
        # -------------------------
        orb_timer += 1
        if orb_timer >= orb_interval:
            ox = random.randint(30, WIDTH - 30)
            orbs.append([ox, -20, 20, 3.5])
            orb_timer = 0

        # -------------------------
        # MOVE OBJECTS
        # -------------------------
        for m in meteors:
            m[1] += m[3]
        for o in orbs:
            o[1] += o[3]

        meteors = [m for m in meteors if m[1] < HEIGHT + 80]
        orbs = [o for o in orbs if o[1] < HEIGHT + 40]

        # -------------------------
        # COLLISION CHECK
        # -------------------------
        prect = pygame.Rect(player_x, player_y, pw, ph)

        hit = False
        for m in meteors:
            if prect.colliderect(pygame.Rect(m[0], m[1], m[2], m[2])):
                hit = True
                break

        if hit:
            if HIT_SND: HIT_SND.play()
            shake_time = 0.5
            shake_mag = 8
            energy = max(0, energy - 10)

        # ORBS
        for o in orbs[:]:
            if prect.colliderect(pygame.Rect(o[0], o[1], o[2], o[2])):
                orbs.remove(o)
                energy = min(100, energy + 12)
                if ORB_SND: ORB_SND.play()

        # passive energy gain
        energy = min(100, energy + 0.02)
        display_energy += (energy - display_energy) * 0.08

        # -------------------------
        # DRAW EVERYTHING
        # -------------------------
        WIN.fill(BG_COLOR)

        # screen shake
        sx = sy = 0
        if shake_time > 0:
            shake_time -= dt / 1000
            sx = random.randint(-shake_mag, shake_mag)
            sy = random.randint(-shake_mag, shake_mag)
            shake_mag = max(0, shake_mag - 1)

        # meteors
        for m in meteors:
            pygame.draw.ellipse(WIN, METEOR_COLOR,
                                (m[0] + sx, m[1] + sy, m[2], m[2]))

        # orbs
        for o in orbs:
            pygame.draw.circle(WIN, ORB_COLOR,
                               (o[0] + sx, o[1] + sy), o[2] // 2)

        # player
        if AVATAR_IMG:
            scaled_img = pygame.transform.scale(
                AVATAR_IMG, (int(pw), int(ph))
            )
            WIN.blit(scaled_img, (player_x + sx, player_y + sy))
        else:
            pygame.draw.rect(
                WIN, WHITE,
                (player_x + sx, player_y + sy, pw, ph)
            )

        # energy bar
        pygame.draw.rect(WIN, WHITE, (10, 10, 240, 20), 2)
        pygame.draw.rect(
            WIN,
            ENERGY_BAR_COLOR,
            (12, 12, int(display_energy * 2.36), 16)
        )

        pygame.display.update()

        # -------------------------
        # WIN CONDITION
        # -------------------------
        if energy >= 100:
            if WIN_SND: WIN_SND.play()
            pygame.time.delay(700)
            print("LEVEL 1 TEST COMPLETED SUCCESSFULLY")
            return True



# ============================================================
#                      RUN DIRECTLY
# ============================================================
if __name__ == "__main__":
    run_level1_test()
