import random
import os

from game import constants
from game.actor import Actor
from game.point import Point

class Speed():
    """A limbless reptile. The responsibility of speed is keep track of its segments. It contains methods for moving and growing among others.

    Stereotype:
        Structurer, Information Holder

    Attributes:
        _body (List): The speed's body (a list of Actor instances)
    """
    def __init__(self):
        """The class constructor.
        
        Args:
            self (speed): An instance of speed.
        """
        super().__init__()
        self._word_list = []
        self.all_used = []

    def get_all(self):
        return self._word_list
    
   
    
    def get_all_words(self):
        PATH = os.path.dirname(os.path.abspath(__file__))
        LIBRARY = open(PATH + "/words.txt").read().splitlines()
        list_words = LIBRARY
        return list_words

    def get_five_words(self):
        list_words = self.get_all_words()
        
        
        for i in range(5):
            
            # Create a random number for x and y
            random_x = random.randint(1, 50)
            random_y = random.randint(1, 20)
            x = int(constants.MAX_X - random_x)
            y = int(constants.MAX_Y - random_y)
            rand = random.choice(list_words)
            self.all_used.append(rand)
            text = rand
            position = Point(x, y)
            velocity = Point(random.randint(-1,1), random.randint(-1,1))
            self.add_words(text, position, velocity)
          

    def always_five_words(self):
        list_words = self.get_all_words()
        if len(self._word_list) < 5:
            rand = random.choice(list_words)
            self.all_used.append(rand)
            text = rand
            position = Point(30, 20)
            velocity = Point(random.randint(0,1), random.randint(0,1))
            self.add_words(text, position, velocity)
            
            

    def add_words(self, text, position, velocity):
        """Adds a new segment to the speed using the given text, position and velocity.

        Args:
            self (speed): An instance of speed.
            text (string): The segment's text.
            position (Point): The segment's position.
            velocity (Point): The segment's velocity.
        """
        segment = Actor()
        segment.set_text(str(text))
        segment.set_position(position)
        segment.set_velocity(velocity)
        self._word_list.append(segment)

    def get_size(self):
         
        
        leng = len(self._word_list)
        return leng
    
    def move_words(self, direction):
        """Moves the words in a constant direction.

        Args:
            self (Snake): An instance of snake.
            direction (Point): The direction to move.
        """
        count = len(self._word_list) - 1
        for n in range(count, -1, -1):
            segment = self._word_list[n]
            if n > 0:
                leader = self._word_list[n - 1]
                velocity = leader.get_velocity()
                segment.set_velocity(velocity)
            else:
                segment.set_velocity(direction)
            segment.move_next()
            
    def remove_words(self, guess):
        """
        This function look for the word in the list and remove it
        """
        for i in self._word_list:
            if guess == i.get_text():
                self._word_list.remove(i)
            
        
            
  
            
