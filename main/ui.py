"""Module that provides a visual interface."""
from tkinter import Button, Label, Tk
from PIL import Image, ImageTk
from main.game import game_instance


class RockPaperScissorsApp:
    """Class representing a graphical user interface for Rock, Paper, Scissors game."""

    def __init__(self, game):
        """Initialize the game interface."""
        self.game = game
        self.root = Tk()
        self.root.title("Rock, Paper, Scissors Game")
        self.root.configure(background='#9B59B6')

        # Initializing Images
        self.rock = ImageTk.PhotoImage(Image.open('main/static/rock.png'))
        self.paper = ImageTk.PhotoImage(Image.open('main/static/paper.png'))
        self.scissors = ImageTk.PhotoImage(Image.open('main/static/scissors.png'))

        # Image Dictionary
        self.images = {
            'rock': self.rock,
            'paper': self.paper,
            'scissors': self.scissors
        }

        # Labels
        self.user_label = Label(self.root, image=self.scissors, bg='#9b59b6')
        self.user_label.grid(row=1, column=0)

        self.ai_label = Label(self.root, image=self.rock, bg='#9b59b6')
        self.ai_label.grid(row=1, column=4)

        # Scores
        self.user_score = Label(self.root, text=0, font=100, bg='#9b59b6', fg='white')
        self.user_score.grid(row=1, column=1)

        self.ai_score = Label(self.root, text=0, font=100, bg='#9b59b6', fg='white')
        self.ai_score.grid(row=1, column=3)

        # Indicators
        self.user_indicator = Label(self.root, font=50, text='USER', bg='#9b59b6', fg='white')
        self.user_indicator.grid(row=0, column=1)

        self.ai_indicator = Label(self.root, font=50, text='COMPUTER', bg='#9b59b6', fg='white')
        self.ai_indicator.grid(row=0, column=3)

        # Message Label
        self.msg = Label(self.root, font=50, bg='#9b59b6', fg='white')
        self.msg.grid(row=3, column=2)

        # Buttons
        Button(self.root, width=20, height=2, text='ROCK', bg='#FF3E4D', fg='white',
               command=lambda: self.play_move('rock')).grid(row=2, column=1)
        Button(self.root, width=20, height=2, text='PAPER', bg='#FAD02E', fg='white',
               command=lambda: self.play_move('paper')).grid(row=2, column=2)

        Button(self.root, width=20, height=2, text='SCISSORS', bg='#0ABDE3', fg='white',
               command=lambda: self.play_move('scissors')).grid(row=2, column=3)

    def play_move(self, user_input):
        """Execute a play move."""
        decision, ai_choice = self.game.play(user_input)
        self.user_label.configure(image=self.images[user_input])
        self.ai_label.configure(image=self.images[ai_choice])
        self.msg.configure(text=decision)
        self.user_score.configure(text=self.game.scores['WIN'])
        self.ai_score.configure(text=self.game.scores['LOSE'])

    def run(self):
        """Run the Tkinter main loop."""
        self.root.mainloop()


create_app = RockPaperScissorsApp(game_instance)
