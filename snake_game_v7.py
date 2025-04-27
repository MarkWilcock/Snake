import sys
import pygame
from snake import Snake
from game_constants import COLOUR_BLACK, COLOUR_GREEN
from game_constants import SCREEN_WIDTH, SCREEN_HEIGHT
from game_constants import FRAME_RATE
from game_constants import  KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT
from game_constants import KEY_COLOUR_MAP
from game_constants import SNAKE_DIRECTION_UP, SNAKE_DIRECTION_DOWN, SNAKE_DIRECTION_LEFT, SNAKE_DIRECTION_RIGHT
from game_constants import  GRID_SIZE


"""
Change the functionality so that the snake continues to move in the direction of the last key pressed, even when the key is released.
"""

# Initialize Pygame
pygame.init()
# Initialize the mixer module (which is used for sound)
pygame.mixer.init()  

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the title of the window
pygame.display.set_caption("Python Snake Game")

clock = pygame.time.Clock()

colour = COLOUR_GREEN  # Default colour

# Create an instance of the snake class and draw it
slippy = Snake(colour)
print(slippy)  # Print the snake object to see its initial state    

game_over = False

def draw_snake(screen, slippy):
    for segment in slippy.get_body():
        x_pos = int(segment[0] * GRID_SIZE)
        y_pos = int(segment[1] * GRID_SIZE)
        pygame.draw.rect(screen, slippy.colour, [x_pos, y_pos, GRID_SIZE, GRID_SIZE])

dir_x = 0
dir_y = 0

while not game_over:
    for event in pygame.event.get():
        #print(event)  # Print the event to see what is happening
        if event.type == pygame.QUIT:
            game_over = True
        if slippy.is_on_screen() == False:
            game_over = True

        if event.type == pygame.KEYDOWN:
            if event.key in KEY_COLOUR_MAP:
                slippy.colour = KEY_COLOUR_MAP[event.key]
            elif event.key == KEY_UP:
                dir_x, dir_y = 0, -1
            elif event.key == KEY_DOWN:    
                dir_x, dir_y = 0, 1
            elif event.key == KEY_LEFT:    
                dir_x, dir_y = -1, 0
            elif event.key == KEY_RIGHT:    
                dir_x, dir_y = 1, 0

    slippy.move(dir_x, dir_y)  # Move the snake in the last direction pressed

    screen.fill(COLOUR_BLACK)
    draw_snake(screen, slippy)
    pygame.display.update()
    clock.tick(FRAME_RATE) # Limit the frame rate to SNAKE_SPEED FPS 

pygame.quit()
sys.exit() # to make absolutely sure all things are closed down properly
