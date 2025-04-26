import pygame

from game_constants import SNAKE_SIZE, SNAKE_SPEED, SNAKE_DIRECTION_UP, SNAKE_DIRECTION_DOWN, SNAKE_DIRECTION_LEFT, SNAKE_DIRECTION_RIGHT, SNAKE_DIRECTION_NONE
from game_constants import SCREEN_WIDTH, SCREEN_HEIGHT

"""
The snake has a body. The body is a list of segments (positions). Each segment is a tuple of (x, y) coordinates.
The first segment is the head of the snake. The last segment is the tail of the snake.
The snake moves in the direction of the head. The tail follows the head.
The snake can move in four directions: up, down, left, and right.
The snake can also change direction. The snake cannot move in the opposite direction of its current direction.
The snake can only move in the direction of the last key pressed.
The snake can only move in one direction at a time.

"""

class Snake:
    """Class representing the snake in the game."""

    def __init__(self, colour, start_x, start_y):
        """Initialize the snake with a given colour and starting position."""
        #print(f"Snake class initialized colour: {colour}, start_x: {start_x}, start_y: {start_y}")
        self.colour = colour
        self.size = SNAKE_SIZE
        self.speed = SNAKE_SPEED
        self.direction = SNAKE_DIRECTION_NONE
        self._body = []  # List to store the snake's body segments
        # Initialize the snake's body with 3 segments. The first segment is the head, and the next two are the body segments.
        # The body segments are positioned to the left of the head.
        for i in range(3):
            self._body.append((start_x - i * self.size, start_y))

    def __str__ ( self ):
        """Return a string representation of the snake."""
        line1 =  f"A snake - colour: {self.colour}\n"
        line2 =  f"Segments:"
        for segment in self.body:
            line2 += f" {"x: ", segment[0], "y: ", segment[1]}"
            
        return line1 + line2 +'\n'

    @property
    def body(self):
        """Return the list of segments that make up the snake's body."""
        return self._body

    def move(self):
        """Move the snake in the specified direction."""
        if self.direction == SNAKE_DIRECTION_NONE:
            return
        
        new_head_x = 0
        new_head_y = 0
        if self.direction == SNAKE_DIRECTION_UP:
            new_head_x = self._body[0][0]
            new_head_y = self._body[0][1] - self.speed
        elif self.direction == SNAKE_DIRECTION_DOWN:
            new_head_x = self._body[0][0]
            new_head_y = self._body[0][1] + self.speed
        elif self.direction == SNAKE_DIRECTION_LEFT:
            new_head_x = self._body[0][0] - self.speed
            new_head_y = self._body[0][1] 
        elif self.direction == SNAKE_DIRECTION_RIGHT:
            new_head_x = self._body[0][0] + self.speed
            new_head_y = self._body[0][1] 

        self._body.insert(0, (new_head_x, new_head_y))  # Add new head position to the front of the body
        self._body.pop() # Remove the last segment of the body to maintain the same length

    def is_on_screen(self):
        """Check if the snake is within the screen bounds."""
        return 0 <= self.body[0][0] <= SCREEN_WIDTH - self.size and 0 <= self.body[0][1] <= SCREEN_HEIGHT - self.size
    

    # def move(self, dx, dy):
    #     """Move the snake in the specified direction."""
    #     self.x += dx * self.speed
    #     self.y += dy * self.speed


    # def draw(self, screen):
    #     """Draw the snake on the screen."""
    #     #pygame.draw.rect(screen, self.colour, [self.x, self.y, self.size, self.size])
    #     for segment in self.body:
    #         print(f"Drawing segment at: {segment}")
    #         # Draw each segment of the snake's body
    #         pygame.draw.rect(screen, self.colour, [segment[0], segment[1], self.size, self.size])

    # def get_segments(self):
    #     """Return the list of segments that make up the snake's body."""
    #     return [(segment[0], segment[1]) for segment in self.body]

