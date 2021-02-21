import random
import os

from game import constants
from game.actor import Actor
from game.point import Point

class Speed:
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
    
    def get_all_words(self):
        PATH = os.path.dirname(os.path.abspath(__file__))
        LIBRARY = open(PATH + "/words.txt").read().splitlines()
        list_words = LIBRARY
        return list_words

    def get_five_words(self):
        list_words = self.get_all_words()
        for i in range(5):
            rand = random.choice(list_words)
            self._word_list.append(rand)
        print(self._word_list)

    def always_five_words(self):
        list_words = self.get_all_words()
        if len(self._word_list) < 5:
            rand = random.choice(list_words)
            self._word_list.append(rand)
            print("adding to the list")
            

    def grow_tail(self):
        """Grows the speed's tail by one segment.
        
        Args:
            self (speed): An instance of speed.
        
        tail = self._segments[-1]
        offset = tail.get_velocity().reverse()
"""     
        random_x = 0
        random_y = 0
        random_x = random.randint(1, 50)
        random_y = random.randint(1, 20)
        x = int(constants.MAX_X - random_x)
        y = int(constants.MAX_Y - random_y)

        
        
        random_word = ''
        words = ''
        palabra = ''
        oficially = ''
        five_words = []
        for words in range(5):
            random_word = random.choice(list_words)
            five_words.append(random_word)
            word1 = five_words[0]
        palabra = ''.join(word1)
        oficially += palabra
        text = oficially 
        position = Point(x - 10, y)
        velocity = Point(1, 0)
        self._add_segment(text, position, velocity)
        
    
    def move_head(self, direction):
        """Moves the speed in the given direction.

        Args:
            self (speed): An instance of speed.
            direction (Point): The direction to move.
        """
        count = len(self._segments) - 1
        for n in range(count, -1, -1):
            segment = self._segments[n]
            if n > 0:
                leader = self._segments[n - 1]
                velocity = leader.get_velocity()
                segment.set_velocity(velocity)
            else:
                segment.set_velocity(direction)
            segment.move_next()

    def _add_segment(self, text, position, velocity):
        """Adds a new segment to the speed using the given text, position and velocity.

        Args:
            self (speed): An instance of speed.
            text (string): The segment's text.
            position (Point): The segment's position.
            velocity (Point): The segment's velocity.
        """
        segment = Actor()
        segment.set_text(text)
        segment.set_position(position)
        segment.set_velocity(velocity)
        self._segments.append(segment)


    def get_size(self):
        """
        
        Gets the speed's body.
        
        Args:
            self (speed): An instance of speed.

        Returns:
            list: The speed's body.
        """
        leng = len(self._segments)
        return leng


'''
            text = oficially 
            position = Point(x - n, y)
            velocity = Point(1, 0)
            self._add_segment(text, position, velocity)
'''

    
        