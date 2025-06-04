import pygame
import random

# Constants
GRID_SIZE = 20
CELL_SIZE = 30
WIDTH = GRID_SIZE * CELL_SIZE
HEIGHT = GRID_SIZE * CELL_SIZE

# Colors
BLUE = (0, 102, 204)
LIGHT_BLUE = (0, 204, 204)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

PADDLE_LENGTH_CELLS = 4

# Base speed for balls
# Increment added to speed whenever territory changes
BALL_SPEED_INC = 0.2
# Maximum allowed speed for balls
BALL_SPEED_MAX = 8

# How quickly the AI paddles track the ball
AI_TRACKING = 0.2

    font = pygame.font.SysFont(None, 24)

    def reset_game():
        nonlocal ball1_x, ball1_y, ball1_vx, ball1_vy
        nonlocal ball2_x, ball2_y, ball2_vx, ball2_vy
        nonlocal borders, paddle1_y, paddle2_y, ball_speed

        borders = [GRID_SIZE // 2 - 1 for _ in range(GRID_SIZE)]
        paddle1_y = HEIGHT // 2 - (PADDLE_LENGTH_CELLS * CELL_SIZE) // 2
        paddle2_y = HEIGHT // 2 - (PADDLE_LENGTH_CELLS * CELL_SIZE) // 2

        direction = random.choice([-1, 1])
        ball_speed = BALL_SPEED

        ball1_x = PADDLE_THICKNESS + BALL_RADIUS
        ball1_y = paddle1_y + (PADDLE_LENGTH_CELLS * CELL_SIZE) // 2
        ball1_vx = direction * ball_speed
        ball1_vy = direction * ball_speed

        ball2_x = WIDTH - PADDLE_THICKNESS - BALL_RADIUS
        ball2_y = paddle2_y + (PADDLE_LENGTH_CELLS * CELL_SIZE) // 2
        ball2_vx = -direction * ball_speed
        ball2_vy = direction * ball_speed

    # initialize game state
    borders: list[int]
    paddle1_y: float
    paddle2_y: float
    ball1_x: float
    ball1_y: float
    ball1_vx: float
    ball1_vy: float
    ball2_x: float
    ball2_y: float
    ball2_vx: float
    ball2_vy: float
    ball_speed: float

    reset_game()
    paused = False
    winner = None
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_p:
                    paused = not paused
                elif event.key == pygame.K_r:
                    winner = None
                    reset_game()
        if paused or winner:
            # Skip updates while paused or after game over
            screen.fill(BLACK)
            if winner:
                text = font.render(f"{winner} wins! Press R to restart", True, WHITE)
                rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
                screen.blit(text, rect)
            else:
                text = font.render("Paused - press P to resume", True, WHITE)
                rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
                screen.blit(text, rect)
            pygame.display.flip()
            clock.tick(60)
            continue
        target1 = max(0, min(target1, HEIGHT - PADDLE_LENGTH_CELLS * CELL_SIZE))
        paddle1_y += (target1 - paddle1_y) * AI_TRACKING
        target2 = max(0, min(target2, HEIGHT - PADDLE_LENGTH_CELLS * CELL_SIZE))
        paddle2_y += (target2 - paddle2_y) * AI_TRACKING

            ball1_vy = offset * ball_speed
            ball1_vx = ball_speed * ball1_vx / norm
            ball1_vy = ball_speed * ball1_vy / norm
                new_speed = min(BALL_SPEED_MAX, ball_speed + BALL_SPEED_INC)
                factor = new_speed / ball_speed
                ball1_vx *= factor
                ball1_vy *= factor
                ball_speed = new_speed
            ball2_vy = offset * ball_speed
            ball2_vx = ball_speed * ball2_vx / norm
            ball2_vy = ball_speed * ball2_vy / norm
                new_speed = min(BALL_SPEED_MAX, ball_speed + BALL_SPEED_INC)
                factor = new_speed / ball_speed
                ball2_vx *= factor
                ball2_vy *= factor
                ball_speed = new_speed

        if all(b == GRID_SIZE - 1 for b in borders):
            winner = "Player 1"
        elif all(b == -1 for b in borders):
            winner = "Player 2"
        p1_cells = sum(b + 1 for b in borders)
        p2_cells = GRID_SIZE * GRID_SIZE - p1_cells
        score1 = font.render(str(p1_cells), True, WHITE)
        score2 = font.render(str(p2_cells), True, WHITE)
        screen.blit(score1, (5, 5))
        screen.blit(score2, (WIDTH - score2.get_width() - 5, 5))

    # AI paddle movement (vertical)
        target1 = ball1_y - (PADDLE_LENGTH_CELLS * CELL_SIZE) // 2
        if target1 < 0:
            target1 = 0
        max_p1 = HEIGHT - PADDLE_LENGTH_CELLS * CELL_SIZE
        if target1 > max_p1:
            target1 = max_p1
        paddle1_y += (target1 - paddle1_y) * 0.2

        target2 = ball2_y - (PADDLE_LENGTH_CELLS * CELL_SIZE) // 2
        if target2 < 0:
            target2 = 0
        max_p2 = HEIGHT - PADDLE_LENGTH_CELLS * CELL_SIZE
        if target2 > max_p2:
            target2 = max_p2
        paddle2_y += (target2 - paddle2_y) * 0.2

    # Update balls
        ball1_x += ball1_vx
        ball1_y += ball1_vy
        ball2_x += ball2_vx
        ball2_y += ball2_vy

    # Collisions for ball1
        if ball1_y - BALL_RADIUS <= 0:
            ball1_y = BALL_RADIUS
            ball1_vy = -ball1_vy
        if ball1_y + BALL_RADIUS >= HEIGHT:
            ball1_y = HEIGHT - BALL_RADIUS
            ball1_vy = -ball1_vy
        if (
            ball1_x - BALL_RADIUS <= PADDLE_THICKNESS
            and paddle1_y <= ball1_y <= paddle1_y + PADDLE_LENGTH_CELLS * CELL_SIZE
        ):
            ball1_x = PADDLE_THICKNESS + BALL_RADIUS
            offset = (
                (ball1_y - (paddle1_y + PADDLE_LENGTH_CELLS * CELL_SIZE / 2))
                / (PADDLE_LENGTH_CELLS * CELL_SIZE / 2)
            )
            offset += random.uniform(-0.1, 0.1)
            ball1_vx = abs(ball1_vx)
            ball1_vy = offset * BALL_SPEED
            norm = (ball1_vx ** 2 + ball1_vy ** 2) ** 0.5
            ball1_vx = BALL_SPEED * ball1_vx / norm
            ball1_vy = BALL_SPEED * ball1_vy / norm
        if ball1_x - BALL_RADIUS <= 0:
            ball1_x = BALL_RADIUS
            ball1_vx = abs(ball1_vx)
        row = int(ball1_y // CELL_SIZE)
        border_x = (borders[row] + 1) * CELL_SIZE
        if ball1_x + BALL_RADIUS >= border_x:
            ball1_x = border_x - BALL_RADIUS
            ball1_vx = -abs(ball1_vx)
            if borders[row] < GRID_SIZE - 1:
                borders[row] += 1

    # Collisions for ball2
        if ball2_y - BALL_RADIUS <= 0:
            ball2_y = BALL_RADIUS
            ball2_vy = -ball2_vy
        if ball2_y + BALL_RADIUS >= HEIGHT:
            ball2_y = HEIGHT - BALL_RADIUS
            ball2_vy = -ball2_vy
        if (
            ball2_x + BALL_RADIUS >= WIDTH - PADDLE_THICKNESS
            and paddle2_y <= ball2_y <= paddle2_y + PADDLE_LENGTH_CELLS * CELL_SIZE
        ):
            ball2_x = WIDTH - PADDLE_THICKNESS - BALL_RADIUS
            offset = (
                (ball2_y - (paddle2_y + PADDLE_LENGTH_CELLS * CELL_SIZE / 2))
                / (PADDLE_LENGTH_CELLS * CELL_SIZE / 2)
            )
            offset += random.uniform(-0.1, 0.1)
            ball2_vx = -abs(ball2_vx)
            ball2_vy = offset * BALL_SPEED
            norm = (ball2_vx ** 2 + ball2_vy ** 2) ** 0.5
            ball2_vx = BALL_SPEED * ball2_vx / norm
            ball2_vy = BALL_SPEED * ball2_vy / norm
        if ball2_x + BALL_RADIUS >= WIDTH:
            ball2_x = WIDTH - BALL_RADIUS
            ball2_vx = -abs(ball2_vx)
        row2 = int(ball2_y // CELL_SIZE)
        border_x2 = (borders[row2] + 1) * CELL_SIZE
        if ball2_x - BALL_RADIUS <= border_x2:
            ball2_x = border_x2 + BALL_RADIUS
            ball2_vx = abs(ball2_vx)
            if borders[row2] > 0:
                borders[row2] -= 1

    # Drawing
        screen.fill(BLACK)
        for r in range(GRID_SIZE):
            for c in range(GRID_SIZE):
                color = BLUE if c <= borders[r] else LIGHT_BLUE
                pygame.draw.rect(
                    screen, color, (c * CELL_SIZE, r * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                )

        pygame.draw.rect(
            screen,
            WHITE,
            (0, paddle1_y, PADDLE_THICKNESS, PADDLE_LENGTH_CELLS * CELL_SIZE),
        )
        pygame.draw.rect(
            screen,
            WHITE,
            (WIDTH - PADDLE_THICKNESS, paddle2_y, PADDLE_THICKNESS, PADDLE_LENGTH_CELLS * CELL_SIZE),
        )
        pygame.draw.circle(screen, WHITE, (int(ball1_x), int(ball1_y)), BALL_RADIUS)
        pygame.draw.circle(screen, WHITE, (int(ball2_x), int(ball2_y)), BALL_RADIUS)

        pygame.display.flip()
        clock.tick(60)
    pygame.quit()


if __name__ == "__main__":
    main()
