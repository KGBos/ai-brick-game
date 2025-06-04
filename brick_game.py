import pygame

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

PADDLE_WIDTH_CELLS = 3
PADDLE_HEIGHT = 10
BALL_RADIUS = 5
BALL_SPEED = 4


def main() -> None:
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    # Border position for each row (last column owned by player 1)
    borders = [GRID_SIZE // 2 - 1 for _ in range(GRID_SIZE)]

    # Paddle positions (x coordinate of left side)
    paddle1_x = (borders[-1] - PADDLE_WIDTH_CELLS // 2) * CELL_SIZE
    paddle2_x = ((GRID_SIZE - 1) - PADDLE_WIDTH_CELLS // 2) * CELL_SIZE

    # Ball positions and velocities
    ball1_x = paddle1_x + PADDLE_WIDTH_CELLS * CELL_SIZE // 2
    ball1_y = HEIGHT - 30
    ball1_vx = BALL_SPEED
    ball1_vy = -BALL_SPEED

    ball2_x = paddle2_x + PADDLE_WIDTH_CELLS * CELL_SIZE // 2
    ball2_y = HEIGHT - 30
    ball2_vx = -BALL_SPEED
    ball2_vy = -BALL_SPEED

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    # AI paddle movement
        target1 = ball1_x - PADDLE_WIDTH_CELLS * CELL_SIZE // 2
        if target1 < 0:
            target1 = 0
        max_p1 = (borders[-1] + 1) * CELL_SIZE - PADDLE_WIDTH_CELLS * CELL_SIZE
        if target1 > max_p1:
            target1 = max_p1
        paddle1_x += (target1 - paddle1_x) * 0.2

        target2 = ball2_x - PADDLE_WIDTH_CELLS * CELL_SIZE // 2
        min_p2 = (borders[-1] + 1) * CELL_SIZE
        if target2 < min_p2:
            target2 = min_p2
        max_p2 = WIDTH - PADDLE_WIDTH_CELLS * CELL_SIZE
        if target2 > max_p2:
            target2 = max_p2
        paddle2_x += (target2 - paddle2_x) * 0.2

    # Update balls
        ball1_x += ball1_vx
        ball1_y += ball1_vy
        ball2_x += ball2_vx
        ball2_y += ball2_vy

    # Collisions for ball1
        if ball1_x - BALL_RADIUS <= 0:
            ball1_x = BALL_RADIUS
            ball1_vx = -ball1_vx
        row = int(ball1_y // CELL_SIZE)
        border_x = (borders[row] + 1) * CELL_SIZE
        if ball1_x + BALL_RADIUS >= border_x:
            ball1_x = border_x - BALL_RADIUS
            ball1_vx = -abs(ball1_vx)
            if borders[row] < GRID_SIZE - 1:
                borders[row] += 1
        if ball1_y - BALL_RADIUS <= 0:
            ball1_y = BALL_RADIUS
            ball1_vy = -ball1_vy
        if (
            ball1_y + BALL_RADIUS >= HEIGHT - PADDLE_HEIGHT
            and paddle1_x <= ball1_x <= paddle1_x + PADDLE_WIDTH_CELLS * CELL_SIZE
        ):
            ball1_y = HEIGHT - PADDLE_HEIGHT - BALL_RADIUS
            ball1_vy = -abs(ball1_vy)
        if ball1_y + BALL_RADIUS >= HEIGHT:
            ball1_y = HEIGHT - BALL_RADIUS
            ball1_vy = -abs(ball1_vy)

    # Collisions for ball2
        if ball2_x + BALL_RADIUS >= WIDTH:
            ball2_x = WIDTH - BALL_RADIUS
            ball2_vx = -ball2_vx
        row2 = int(ball2_y // CELL_SIZE)
        border_x2 = (borders[row2] + 1) * CELL_SIZE
        if ball2_x - BALL_RADIUS <= border_x2:
            ball2_x = border_x2 + BALL_RADIUS
            ball2_vx = abs(ball2_vx)
            if borders[row2] > 0:
                borders[row2] -= 1
        if ball2_y - BALL_RADIUS <= 0:
            ball2_y = BALL_RADIUS
            ball2_vy = -ball2_vy
        if (
            ball2_y + BALL_RADIUS >= HEIGHT - PADDLE_HEIGHT
            and paddle2_x <= ball2_x <= paddle2_x + PADDLE_WIDTH_CELLS * CELL_SIZE
        ):
            ball2_y = HEIGHT - PADDLE_HEIGHT - BALL_RADIUS
            ball2_vy = -abs(ball2_vy)
        if ball2_y + BALL_RADIUS >= HEIGHT:
            ball2_y = HEIGHT - BALL_RADIUS
            ball2_vy = -abs(ball2_vy)

    # Drawing
        screen.fill(BLACK)
        for r in range(GRID_SIZE):
            for c in range(GRID_SIZE):
                color = BLUE if c <= borders[r] else LIGHT_BLUE
                pygame.draw.rect(
                    screen, color, (c * CELL_SIZE, r * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                )
        # Grid lines
        for r in range(GRID_SIZE + 1):
            pygame.draw.line(screen, BLACK, (0, r * CELL_SIZE), (WIDTH, r * CELL_SIZE))
        for c in range(GRID_SIZE + 1):
            pygame.draw.line(screen, BLACK, (c * CELL_SIZE, 0), (c * CELL_SIZE, HEIGHT))

        pygame.draw.rect(
            screen,
            WHITE,
            (paddle1_x, HEIGHT - PADDLE_HEIGHT, PADDLE_WIDTH_CELLS * CELL_SIZE, PADDLE_HEIGHT),
        )
        pygame.draw.rect(
            screen,
            WHITE,
            (paddle2_x, HEIGHT - PADDLE_HEIGHT, PADDLE_WIDTH_CELLS * CELL_SIZE, PADDLE_HEIGHT),
        )
        pygame.draw.circle(screen, WHITE, (int(ball1_x), int(ball1_y)), BALL_RADIUS)
        pygame.draw.circle(screen, WHITE, (int(ball2_x), int(ball2_y)), BALL_RADIUS)

        pygame.display.flip()
        clock.tick(60)
    pygame.quit()


if __name__ == "__main__":
    main()
