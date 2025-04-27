import pygame

from game_constants import GRID_ROWS, GRID_COLS, GRID_SIZE

"""
The snake has a body. The body is a list of segments (positions). Each segment is a tuple of (row, column) coordinates.
The first segment is the head of the snake. The last segment is the tail of the snake.
The snake moves in the direction of the head. The tail follows the head.
The snake can move in four directions: up, down, left, and right.
The snake can also change direction. The snake cannot move in the opposite direction of its current direction.
The snake can only move in the direction of the last key pressed.
The snake can only move in one direction at a time.

"""

class Snake:
    """Class representing the snake in the game."""

    def __init__(self, colour):
        """Initialize the snake with a given colour and starting position."""
        self.colour = colour
        self.size = GRID_SIZE  # Size of each segment of the snake
        self.direction_x = 1  # Direction of movement in the x-axis
        self.direction_y = 0
        self.body = [(12,12), (11,12), (10,12)]  # Initial position of the snake's body segments

    def __str__ ( self ):
        """Return a string representation of the snake."""
        line1 =  f"A snake - colour: {self.colour}\n"
        line2 =  f"Segments:"
        for segment in self.body:
            line2 += f" {"row: ", segment[0], "column: ", segment[1]}"
            
        return line1 + line2 +'\n'

    def get_body(self):
        """Return the list of segments that make up the snake's body."""
        return self.body
    
    def get_head(self):
        """Return the position of the snake's head."""
        return self.body[0]

    def move(self, dx=0, dy=0):
        """Move the snake in the specified direction."""
        if dx == 0 and dy == 0:
            return
        
        # Snake cannot reverse direction 
        if (dx == -self.direction_x and dy == -self.direction_y):
            dx = self.direction_x
            dy = self.direction_y
        
        self.body.insert(0, (self.get_head()[0] + dx, self.get_head()[1] + dy))  # Add new head position to the front of the body
        self.body.pop() # Remove the last segment of the body to maintain the same length

        self.direction_x = dx  # Update the direction of movement in the x-axis
        self.direction_y = dy  # Update the direction of movement in the y-axis

    def is_on_screen(self):
        """Check if the snake is within the screen bounds."""
        return 0 <= self.body[0][0] < GRID_ROWS and 0 <= self.body[0][1] <= GRID_COLS
    
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
