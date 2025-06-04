# AI Brick Game

This is a simple two-player territory brick breaker written with **pygame**.

## Gameplay

- The board is a 20x20 grid divided into a blue zone (Player 1) and a light blue zone (Player 2).
- Each player controls a paddle at the bottom of their side. Paddles automatically track their own ball.
- Balls cannot cross the center line. When a ball hits the opponent's colored squares along the border it converts them to the player's color, expanding territory.
- The objective is to push the border deep into the opponent's zone.

## Running

First install pygame and then run the script:

```bash
pip install pygame
python brick_game.py
```

Close the window to exit the game.
