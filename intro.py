import pygame
from settings import WIN, WIDTH, HEIGHT, BLACK, YELLOW, FPS

# ------------------------- INTRO 1 -------------------------

def run_intro():
    font = pygame.font.SysFont(None, 36)
    intro_lines = [
        "AN UNKNOWN ENTITY HAS LANDED",
        "IN THE FAR REACHES OF THE COSMOS...",
        "DRIFTING AMIDST METEOR SHOWERS",
        "AND GALACTIC STORMS...",
        "WILL IT SURVIVE THE COSMIC CHAOS?",
        "COLLECT ENERGY ORBS TO SUSTAIN LIFE",
        "OR PERISH AMIDST THE STARS..."
    ]
    line_spacing = 60
    text_surfaces = [font.render(line, True, YELLOW) for line in intro_lines]

    y_offset = HEIGHT + 200
    scroll_speed = 1.5

    clock = pygame.time.Clock()
    intro_done = False

    while not intro_done:
        clock.tick(FPS)
        WIN.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        # Draw scrolling text
        for i, text in enumerate(text_surfaces):
            WIN.blit(text, (WIDTH//2 - text.get_width()//2,
                            y_offset + i * line_spacing))

        y_offset -= scroll_speed

        # Finish when gone above screen
        if y_offset + len(text_surfaces) * line_spacing < -100:
            intro_done = True

        pygame.display.update()


# ------------------------- AFTER LEVEL 1 -------------------------

def run_monologue_after_level1():
    font = pygame.font.SysFont(None, 34)
    lines = [
        "HE HAS SURVIVED...",
        "BUT WAS THAT A FLUKE?",
        "HAS THE REAL BATTLE EVEN BEGUN?",
        "WHAT LIES AHEAD?",
        "NO ONE KNOWS...",
        "THE COSMOS WATCHES IN SILENCE..."
    ]

    text_surfaces = [font.render(line, True, YELLOW) for line in lines]

    line_spacing = 60
    y_offset = HEIGHT + 150
    scroll_speed = 1.5

    clock = pygame.time.Clock()
    done = False

    while not done:
        clock.tick(FPS)
        WIN.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        for i, text in enumerate(text_surfaces):
            WIN.blit(text, (WIDTH//2 - text.get_width()//2,
                            y_offset + i * line_spacing))

        y_offset -= scroll_speed

        if y_offset + len(text_surfaces) * line_spacing < -120:
            done = True

        pygame.display.update()


# ------------------------- AFTER LEVEL 2 (NEW) -------------------------

def run_monologue_after_level2():
    font = pygame.font.SysFont(None, 34)
    lines = [
        "TWICE HE HAS FOUGHT...",
        "TWICE HE HAS SURVIVED...",
        "BUT SURVIVAL IS NOT VICTORY.",
        "THE UNIVERSE SHIFTS—UNEASY...",
        "SOMETHING STIRS WITHIN THE STORM...",
        "THE FINAL TRIAL AWAITS..."
    ]

    text_surfaces = [font.render(line, True, YELLOW) for line in lines]

    line_spacing = 60
    y_offset = HEIGHT + 150
    scroll_speed = 1.5

    clock = pygame.time.Clock()
    done = False

    while not done:
        clock.tick(FPS)
        WIN.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        for i, text in enumerate(text_surfaces):
            WIN.blit(text, (WIDTH//2 - text.get_width()//2,
                            y_offset + i * line_spacing))

        y_offset -= scroll_speed

        if y_offset + len(text_surfaces) * line_spacing < -120:
            done = True

        pygame.display.update()
