
# Running Ball & POV Dodging Game

## Overview

This project is a simple Python game built using Pygame. It includes two modes:

1. Mode A — Side-Scrolling Runner:
   A ball jumps over obstacles from a side view.

2. Mode B — POV Driving / First-Person Dodging:
   A top-down perspective where the player moves left and right to avoid falling obstacles.

The project emphasizes basic game mechanics, obstacle interaction, scoring, and player controls. All graphics are simple shapes—no images required.

---

## Setup

### Requirements

 Python 3.12+
 Pygame 2.6+
 Mac / Windows / Linux

### Install Pygame

```bash
python3 -m pip install pygame
```

---

## Running the Games

### Mode A

```bash
python3 mode_a.py
```

### Mode B

```bash
python3 mode_b.py
```

---

## Controls

### Mode A — Side Runner

 UP Arrow: Jump
 Quit: Close window
 Restart: Press R after Game Over

### Mode B — POV Dodging

 LEFT Arrow: Move left
 RIGHT Arrow: Move right
 Quit: Close window
 Restart: Press R after Game Over

---

## Game Features

### Common Features

 Player movement: Smooth control with arrow keys.
 Obstacles: Move across the screen (Mode A: horizontal, Mode B: vertical).
 Collision detection: Game freezes immediately when player hits an obstacle to visualize the loss.
 Restart: Press R to restart the game after Game Over.
 Score display: Shown in real-time at the top-left.

### Mode A Specific

 Side-scrolling runner style
 Jumping ball
 Obstacles appear from the right and move left
 Score increases slowly over time (1 / FPS)
 Ground collision prevents falling below floor

### Mode B Specific

 POV / top-down driving style
 Player moves left/right
 Obstacles fall from top
 Obstacle speed increases gradually over time
 Score increases slowly over time, same as Mode A

---

## Game Mechanics

### Obstacles

 Represented as simple rectangles
 Spawn randomly and move continuously
 Removed when off-screen
 Collision triggers freeze and Game Over

### Score System

 Time-based: Incremented gradually each frame (1 / FPS)
 Displayed: Top-left of the screen
 Mode B now behaves like Mode A in scoring

### Collision & Freeze

 The game immediately stops moving all elements on collision
 Game Over text appears
 Restart option with R key

---

## Future Enhancements (Planned / Suggested)

 Lane system for Mode B (3 lanes like Temple Run)
 Power-ups (slow motion, shields, points multiplier)
 Health system (allow multiple hits before Game Over)
 Sound effects (jump, collision, score)
 Background effects / parallax scrolling
 Difficulty selection menu
 Start menu to choose Mode A / Mode B

---

## Project Structure

```
/game_project/
├── mode_a.py        # Side-scrolling ball runner
├── mode_b.py        # POV dodging game
├── README.md        # Project documentation
└── requirements.txt # (optional) Pygame version pinning
```

---

## Installation Tips (Mac / Linux / Windows)

1. Install Python 3.12+
2. Install Pygame:

   ```bash
   python3 -m pip install pygame
   ```
3. Navigate to project folder
4. Run your chosen mode:

   ```bash
   python3 mode_a.py   # Mode A
   python3 mode_b.py   # Mode B
   ```

---

## Notes

 No external images or assets are required.
 All graphics are generated using Pygame primitives (rectangles, circles).
 Works on both x86_64 and arm64 Macs, as well as Linux and Windows.
