"""
    Markov Model Module
    ===================

    This module contains a class, `MarkovModel`, 
    for making predictions based on the history of user moves.
    It evaluates performance over a specified number of rounds and can reset its state.

    The `MarkovModel` class includes the following public methods:
    - `update`: Updates the model with the latest user move.
    - `get_prediction`: Predicts the next user move based on the history.
    - `get_score`: Calculates and returns the current score of the model.
    - `reset`: Resets the model to its initial state.

    Example:
    >>> model = MarkovModel(order=3, focus=5)
    >>> model.update('rock')
    >>> model.get_score()
    0
    >>> model.get_prediction()
    'rock'
    >>> model.reset()
"""
import random
from collections import defaultdict, deque


class MarkovModel:
    """
    A class that represents a Markov Model for predicting user moves
    in a game and evaluates the model's performance over specified rounds.
    
    Attributes:
        order (int): The order of the Markov model.
        focus (int): The number of rounds to consider for resetting the score.
        user_moves (deque[str]): A deque that keeps track of past user moves.
        score_history (deque[int]): A deque that keeps track of scores for each round.
        ai_move (str): The AI's predicted move in the current round.
        model (defaultdict): A dictionary to store sequences of moves and the count of the moves that follow them.
    """

    def __init__(self, order: int, focus: int):
        """
        Initializes a new instance of the MarkovModel class.

        :param order: The order of the Markov model.
        :param focus: The number of rounds to consider for resetting the score.
        """
        self.order = order
        self.focus = focus
        self.user_moves = deque(maxlen=order)
        self.score_history = deque(maxlen=focus)
        self.ai_move = None
        self.model = defaultdict(lambda: defaultdict(int))

    def update(self, user_move: str):
        """
        Updates the model with the latest user_move and maintains the length 
        and score_history based on the focus. It also updates the score based 
        on the moves played in the last round.

        :param user_move: The user's move played in the current round.
        """
        if len(self.user_moves) == self.order:
            key = tuple(self.user_moves)
            self.model[key][user_move] += 1

        # Add the move to history (if history exceeds 3 moves, the oldest will be removed)
        self.user_moves.append(user_move)
        self.score_history.append(self.evaluate_move(user_move))


    def evaluate_move(self, user_move: str):
        """
        Evaluates the latest user move and returns the score for the latest round. 
        1 if ai wins, 0 if it's a tie, -1 if user wins.

        :param user_move: The user's latest move.
        :return: The score for the latest round.
        """
        outcomes = {('rock', 'paper'): -1, ('paper', 'scissors'): -1, ('scissors', 'rock'): -1,
                    ('paper', 'rock'): 1, ('scissors', 'paper'): 1, ('rock', 'scissors'): 1}
        return outcomes.get((self.ai_move, user_move), 0)

    def get_prediction(self) -> str:
        """
        Predicts the next user move based on the history.

        :return: The predicted next user move.
        """

        key = tuple(self.user_moves)

        if len(self.user_moves) < self.order or not ( key in self.model and self.model[key]):
            self.ai_move = random.choice(['rock', 'paper', 'scissors'])
        else:
            prediction = max(self.model[key], key=self.model[key].get)
            self.ai_move = self.counter_move(prediction)

        return self.ai_move



    def counter_move(self, user_move: str):
        """
        Determines a move that will beat the predicted user move.

        :param user_move: Predicted next user move.
        :return: A move that will beat the user's predicted move.
        """
        return {'rock': 'paper', 'paper': 'scissors', 'scissors': 'rock'}.get(user_move, 'rock')

    def get_score(self):
        """
        Calculates and returns the current score of the model.

        :return: The current score of the model.
        """
        return sum(self.score_history)

    def reset(self):
        """
        Resets the model to its initial state.
        """
        self.user_moves.clear()
        self.score_history.clear()
        self.model = defaultdict(lambda: defaultdict(int))
