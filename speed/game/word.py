import random
from game import constants
from game.actor import Actor
from game.point import Point

class Word(Actor):
    """A nutritious substance that snake's like. The responsibility of word is to keep track of its appearance and position. A word can move around randomly if asked to do so. 
    
    Stereotype:
        Information Holder

    Attributes: 
        _points (integer): The number of points the word is worth.
    """
    def __init__(self):
        """The class constructor. Invokes the superclass constructor, set's the 
        text and moves the word to a random position within the boundary of the 
        screen.
        
        Args:
            self (Actor): an instance of Actor.
        """
        super().__init__()
        self._points = 0
        self.set_text("- Buffer: ")
        self.reset()
    
    def get_points(self):
        """Gets the points this word is worth.
        
        Args:
            self (word): an instance of word.

        Returns:
            integer: The points this word is worth.
        """
        return self._points

    def reset(self):
        """Resets the word by moving it to a random position within the boundaries of the screen and reassigning the points to a random number.
        
        Args:
            self (word): an instance of word.
        """
        
        position = Point(0, 20)
        self.set_position(position)
        
