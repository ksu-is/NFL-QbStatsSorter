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
