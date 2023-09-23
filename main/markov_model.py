
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

class MarkovModel:
    """
    Represents a Markov Model for predicting user moves
    and evaluating performance over a specified number of rounds.
    
    Attributes:
        order (int): The order of the Markov model.
        focus (int): The number of rounds to focus on for resetting the score.
        user_moves (list): A list to keep track of past user moves.
        score_history (list): A list to keep track of scores.
        ai_move (str): The AI's move in the current round.
    """

    def __init__(self, order, focus):
        """
        Initialize a new instance of the MarkovModel class.

        :param order: The order of the Markov model.
        :param focus: The number of rounds to focus on for resetting the score.
        """
        self.order = order
        self.focus = focus
        self.user_moves = []
        self.score_history = []
        self.ai_move = None  # it's good to keep this as None if not yet determined.

    def update(self, user_move):
        """
        Update the model with the latest user_move, maintain the length of 
        user_moves and score_history based on the order and focus respectively,
        and update the score based on the moves played.

        :param user_move: The user's move played in the current round.
        """
        # Maintain the lengths of user_moves and score_history.
        if len(self.user_moves) == self.order:
            self.user_moves.pop(0)
        if len(self.score_history) == self.focus:
            self.score_history.pop(0)

        # Append the latest move and score
        self.user_moves.append(user_move)
        self.score_history.append(self.evaluate_move(user_move))

    def evaluate_move(self, user_move):
        """
        Evaluate the latest move and update the score.
        
        :param user_move: The user's latest move.
        :return: The score for the latest round.
        """
        lose_conditions = [('rock', 'paper'), ('paper', 'scissors'), ('scissors', 'rock')]
        win_conditions = [('paper', 'rock'), ('scissors', 'paper'), ('rock', 'scissors')]

        if (self.ai_move, user_move) in lose_conditions:
            return -1
        if (self.ai_move, user_move) in win_conditions:
            return 1
        return 0  # Return 0 if it's a tie

    def get_prediction(self):
        """
        Predict the next user_move based on the history.

        :return: The predicted user_move.
        """
        # Implement prediction logic here based on the model's order and history
        return 'paper'  # Placeholder, replace with actual prediction logic.

    def get_score(self):
        """
        Calculate and return the current score of the model.

        :return: The current score of the model.
        """
        return sum(self.score_history)

    def reset(self):
        """
        Reset the model to its initial state by clearing user_moves and score_history.
        """
        self.user_moves.clear()
        self.score_history.clear()
