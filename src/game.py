import random
class game:
    def __init__(self):
        self.choices = ["rock", "paper", "scissor"]
        self.reset_scores()

    def reset_scores(self):
        self.scores = {"TIE": 0, "WIN": 0, "LOSE": 0}

    def play(self, user_choice):
        ai_choice = random.choice(self.choices)
        if user_choice == ai_choice:
            self.scores["TIE"] += 1
            return "It's a tie!", ai_choice
        elif (
            (user_choice == "rock" and ai_choice == "scissor") or
            (user_choice == "scissor" and ai_choice == "paper") or
            (user_choice == "paper" and ai_choice == "rock")
        ):
            self.scores["WIN"] += 1
            return "You win!", ai_choice
        else:
            self.scores["LOSE"] += 1
            return "You lose :(", ai_choice
        
        
game_instance = game()