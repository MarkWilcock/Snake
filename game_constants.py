# Constant for screen dimensions and snake properties
import pygame

# Set up constants for colours
# Each colour is a tuple of Red, Green, Blue  values.  Each value can range from 0 to 255.
COLOUR_GREEN = (0, 255, 0)
COLOUR_BLACK = (0, 0, 0)
COLOUR_RED = (255, 0, 0)
COLOUR_BLUE = (0, 0, 255)
COLOUR_YELLOW = (255, 255, 0)
COLOUR_ORANGE = (255, 165, 0)

GRID_ROWS = 24  # Number of rows in the grid
GRID_COLS = 30  # Number of columns in the grid
GRID_SIZE = 20  # Size of each grid cell in pixels
SCREEN_WIDTH = GRID_COLS * GRID_SIZE  # Width of the screen in pixels
SCREEN_HEIGHT = GRID_ROWS * GRID_SIZE  # Height of the screen in pixels
SCREEN_CENTRE_X = SCREEN_WIDTH // 2
SCREEN_CENTRE_Y = SCREEN_HEIGHT // 2

FRAME_RATE = 10  # Frame rate in frames per second (FPS)

KEY_BLUE = pygame.K_b
KEY_GREEN = pygame.K_g
KEY_RED = pygame.K_r
KEY_YELLOW = pygame.K_y
KEY_ORANGE = pygame.K_o
KEY_UP = pygame.K_UP
KEY_DOWN = pygame.K_DOWN
KEY_LEFT = pygame.K_LEFT
KEY_RIGHT = pygame.K_RIGHT

KEY_COLOUR_MAP = {
    KEY_BLUE: COLOUR_BLUE,
    KEY_GREEN: COLOUR_GREEN,
    KEY_RED: COLOUR_RED,
    KEY_YELLOW: COLOUR_YELLOW,
    KEY_ORANGE: COLOUR_ORANGE,
}

#SNAKE_SIZE = 20
#SNAKE_SPEED = 10  # Speed of the snake in pixels per frame

SNAKE_DIRECTION_UP  = 10
SNAKE_DIRECTION_DOWN = 20
SNAKE_DIRECTION_LEFT = 30
SNAKE_DIRECTION_RIGHT = 40
SNAKE_DIRECTION_NONE = 50

DIRECTION_X = 1
DIRECTION_Y = 0
