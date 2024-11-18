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
