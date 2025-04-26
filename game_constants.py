# Constant for screen dimensions and snake properties
import pygame

# Set up constants for colours
# Each colour is a tuple of COLOUR_RED, COLOUR_GREEN,  Blue  values.  Each value can range from 0 to 255.
COLOUR_GREEN = (0, 255, 0)
COLOUR_BLACK = (0, 0, 0)
COLOUR_RED = (255, 0, 0)
COLOUR_BLUE = (0, 0, 255)
COLOUR_YELLOW = (255, 255, 0)
COLOUR_ORANGE = (255, 165, 0)

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
SCREEN_HEIGHT = 480
SCREEN_CENTRE_X = SCREEN_WIDTH // 2
SCREEN_CENTRE_Y = SCREEN_HEIGHT // 2

FRAME_RATE = 2  # Frame rate in frames per second (FPS)

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

SNAKE_SIZE = 20
SNAKE_SPEED = 10  # Speed of the snake in pixels per frame

SNAKE_DIRECTION_UP  = 10
SNAKE_DIRECTION_DOWN = 20
SNAKE_DIRECTION_LEFT = 30
SNAKE_DIRECTION_RIGHT = 40
SNAKE_DIRECTION_NONE = 50
