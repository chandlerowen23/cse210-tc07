from time import sleep
from game import constants
from game.score import Score
from game.word import Word
from game.speed import Speed
from game.guess import Guess

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


        #this code works but repeats, probably from the speed.py i have loops
        guess = self._input_service.get_letter()
        letters = ""
        letters += guess
        x = self._guess.get_guess(letters)
        
        direction = self._input_service.get_direction()
        self._speed.move_words(direction)

        

    def _do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means checking for a collision and updating the score.

        Args:
            self (Director): An instance of Director.
        """

        self._speed.always_five_words()
        self._guess.reset()
        #we are comparing strings to see how many were typed correctly but it doesnt seem to change.
        guess_list = self._guess.guess_list_check()
        pulled_list = self._speed.get_used()
        self.check_correct(guess_list, pulled_list)
        size = self._speed.get_size()
        self._score.add_points(self.correct * 10)
        #print(size)
        #segments = self._snake.get_all()
        #print('this is christ',segments,'---')
        #points = self._food.get_points()

        if size != 5:
            self._speed.get_five_words(self)

    def check_correct(self, guess, used):
        for i in guess:
            for k in used:
                if i == k:
                    used.pop(k)
                    guess.pop(i)
                    self._score.get_points(10)


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
        #example
        #self._output_service.draw_actors(self._snake.get_all())
        #self._output_service.draw_actor(self._speed.get_all())
        self._output_service.flush_buffer()

    
            
