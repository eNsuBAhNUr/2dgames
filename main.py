import pygame
from intro import (
    run_intro,
    run_monologue_after_level1,
    run_monologue_after_level2
)

from levels.level1 import run_level1
from levels.level2 import run_level2
from levels.level3 import run_level3

from settings import WIN

pygame.init()
font = pygame.font.SysFont(None, 40)


def show_center_text(text, duration=3000):
    WIN.fill((0, 0, 0))
    rendered = font.render(text, True, (255, 255, 0))
    rect = rendered.get_rect(center=(WIN.get_width()//2, WIN.get_height()//2))
    WIN.blit(rendered, rect)
    pygame.display.update()
    pygame.time.delay(duration)


def main():
    print(">>> STARTING INTRO")
    run_intro()

    # -------- LEVEL 1 LOOP --------
    print(">>> ENTERING LEVEL 1 LOOP")
    level1_cleared = False
    while not level1_cleared:
        print(">>> RUNNING LEVEL 1")
        level1_cleared = run_level1()
        if not level1_cleared:
            print(">>> LEVEL 1 FAILED — RESTARTING")

    print(">>> LEVEL 1 SUCCESS — SHOWING MONOLOGUE 1")
    run_monologue_after_level1()

    # -------- LEVEL 2 LOOP --------
    print(">>> ENTERING LEVEL 2 LOOP")
    level2_cleared = False
    while not level2_cleared:
        print(">>> RUNNING LEVEL 2")
        level2_cleared = run_level2()
        if not level2_cleared:
            print(">>> LEVEL 2 FAILED — RESTARTING")

    print(">>> LEVEL 2 SUCCESS — SHOWING MONOLOGUE 2")
    run_monologue_after_level2()

    # -------- LEVEL 3 LOOP --------
    print(">>> ENTERING LEVEL 3 LOOP")
    level3_cleared = False
    while not level3_cleared:
        print(">>> RUNNING LEVEL 3")
        level3_cleared = run_level3()
        if not level3_cleared:
            print(">>> LEVEL 3 FAILED — RESTARTING")

    print(">>> GAME COMPLETE")
    show_center_text("YOU SURVIVED THE COSMIC TRIALS...", 5000)

    pygame.quit()


if __name__ == "__main__":
    main()
