from time import sleep
from asciimatics.event import KeyboardEvent
from game import constants
from game.score import Score
from game.word import Word
from game.speed import Speed
from game.guess import Guess
from game.actor import Actor

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        words (words): The snake's target.
        input_service (InputService): The input mechanism.
        keep_playing (boolean): Whether or not the game can continue.
        output_service (OutputService): The output mechanism.
        score (Score): The current score.
        snake (Snake): The player or snake.
    """

    def __init__(self, input_service, output_service):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self._word = Word()
        self._input_service = input_service
        self._keep_playing = True
        self._output_service = output_service
        self._score = Score()
        self._speed = Speed()
        self._guess = Guess()
        self._actor = Actor()
        
        self.correct = 0
        
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        self._speed.get_five_words()
        while self._keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
            sleep(constants.FRAME_LENGTH)
          

    def _get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means getting the desired direction and moving the snake.

        Args:
            self (Director): An instance of Director.
        """


        #Get input keyboard
        guess = self._input_service.get_letter()
        letters = ""
        letters += guess
        x = self._guess.get_guess(letters)
        
        # It gives direction to the words
        direction = self._input_service.get_direction()
        self._speed.move_words(direction)
       



    def _do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means checking for a collision and updating the score.

        Args:
            self (Director): An instance of Director.
        """
        self.compare_words()
        
        self._speed.always_five_words()
        self._guess.reset()
        
        
        #Make sure there are 5 words displaying
        size = self._speed.get_size()
        if size != 5:
            self._speed.get_five_words(self)

    

    def _do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means checking if there are stones left and declaring 
        the winner.

        Args:
            self (Director): An instance of Director.
        """
        self._output_service.clear_screen()
        self._output_service.draw_actor(self._word)
        self._output_service.draw_actors(self._speed.get_all())
        self._output_service.draw_actor(self._score)
        self._output_service.draw_actor(self._guess)
        self._output_service.flush_buffer()
        
    def compare_words(self):
        
        # get the input guess word
        words_list = self._speed.get_all()
        guess = self._input_service.get_letter()
        letters = ""
        letters += guess
        guess = self._guess.get_guess(letters)
       
        # Compare the guess with our list of words displaying
        for i in words_list:
            if guess == i.get_text():
                self._speed.remove_words(guess)
                self._score.add_points(1)
        
        

    
            
