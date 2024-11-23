import pygame
import random

# Start pygame
pygame.init()

# Set up the game window
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pong Game')

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the paddles and ball
PADDLE_WIDTH, PADDLE_HEIGHT = 15, 100
BALL_SIZE = 15

# Paddle class
class Paddle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.speed = 7

def move(self, up=True):
        keys = pygame.key.get_pressed()
        if up:
            if keys[pygame.K_w] and self.rect.top > 0:
                self.rect.y -= self.speed
            if keys[pygame.K_s] and self.rect.bottom < HEIGHT:
                self.rect.y += self.speed
        else:
            if keys[pygame.K_UP] and self.rect.top > 0:
                self.rect.y -= self.speed
            if keys[pygame.K_DOWN] and self.rect.bottom < HEIGHT:
                self.rect.y += self.speed

    def draw(self, surface):
        pygame.draw.rect(surface, WHITE, self.rect)

# Ball class
class Ball:
    def __init__(self):
        self.rect = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
        self.x_speed = random.choice([5, -5])
        self.y_speed = random.choice([5, -5])

    def move(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.y_speed = -self.y_speed

    def reset(self):
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.x_speed = random.choice([5, -5])
        self.y_speed = random.choice([5, -5])

    def draw(self, surface):
        pygame.draw.ellipse(surface, WHITE, self.rect)

    def draw(self, surface):
        pygame.draw.rect(surface, WHITE, self.rect)

# Create simple game loop
def game_loop():
    clock = pygame.time.Clock()
    paddle_left = Paddle(30, HEIGHT // 2 - PADDLE_HEIGHT // 2)
    paddle_right = Paddle(WIDTH - 30 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2)
    ball = Ball()

    left_score, right_score = 0, 0
    font = pygame.font.Font(None, 36)

    running = True
    while running:
        screen.fill(BLACK)

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Move paddles and ball
        paddle_left.move(up=True)
        paddle_right.move(up=False)
        ball.move()

        # Collision with paddles
        if ball.rect.colliderect(paddle_left.rect) or ball.rect.colliderect(paddle_right.rect):
            ball.x_speed = -ball.x_speed

        # Score update
        if ball.rect.left <= 0:
            right_score += 1
            ball.reset()
        if ball.rect.right >= WIDTH:
            left_score += 1
            ball.reset()

        # Draw everything
        paddle_left.draw(screen)
        paddle_right.draw(screen)
        ball.draw(screen)

        # Draw the score
        score_text = font.render(f'{left_score} - {right_score}', True, WHITE)
        screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 20))

        # Refresh the screen
        pygame.display.flip()

        # Frame rate
        clock.tick(60)

    pygame.quit()

game_loop()
