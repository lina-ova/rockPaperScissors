from tkinter import Button, Label, Tk
import random
from PIL import Image, ImageTk


# Game Logic
class Game:
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

# GUI
class RockPaperScissorsApp:
    def __init__(self, game):
        self.game = game
        self.root = Tk()
        self.root.title("Rock, Paper, Scissors Game")
        self.root.configure(background='#9b59b6')
        self.rock = ImageTk.PhotoImage(Image.open('static/rock.png'))
        self.paper = ImageTk.PhotoImage(Image.open('static/paper.png'))
        self.scissors = ImageTk.PhotoImage(Image.open('static/scissors.png'))
        self.images = {
            'rock': self.rock, 
            'paper': self.paper, 
            'scissor': self.scissors
        }
        
        self.user_label=Label(self.root, image=self.scissors, bg='#9b59b6')
        self.user_label.grid(row=1, column=0)
        self.ai_label=Label(self.root, image=self.rock, bg='#9b59b6')
        self.ai_label.grid(row=1, column=4)
        
        ## Scores
        self.userScore=Label(self.root, text=0, font=100, bg='#9b59b6', fg='white')
        self.userScore.grid(row=1, column=3)
        self.aiScore=Label(self.root, text=0, font=100, bg='#9b59b6', fg='white')
        self.aiScore.grid(row=1,column=1)
        
        ##Indicators
        self.user_indicator= Label(self.root, font=50, text='USER', bg='#9b59b6', fg='white').grid(row=0,column=1 )
        self.ai_indicator= Label(self.root, font=50, text='COMPUTER', bg='#9b59b6', fg='white').grid(row=0, column=3)
                
        ## messages
        self.msg = Label(self.root, font=50, bg='#9b59b6', fg='white')
        self.msg.grid(row=3, column=2)
        
        ##Buttons 
        rock=Button(self.root, width=20, height=2, text='ROCK', bg='#FF3E4D', fg='white', command=lambda:self.play_move('rock')).grid(row=2, column=1)
        paper=Button(self.root, width=20, height=2, text='PAPER', bg='#FAD02E', fg='white', command=lambda:self.play_move('paper')).grid(row=2, column=2)
        scissors=Button(self.root, width=20, height=2, text='SCISSORS', bg='#0ABDE3', fg='white', command=lambda:self.play_move('scissor')).grid(row=2, column=3)


    def play_move(self, user_input):
        
        decision, ai_choice = self.game.play(user_input)
        self.user_label.configure(image=self.images[user_input])
        self.ai_label.configure(image=self.images[ai_choice])
        self.msg.configure(text=decision)
        self.userScore.configure(text=self.game.scores['WIN'])
        self.aiScore.configure(text=self.game.scores['LOSE'])

    def run(self):
        self.root.mainloop()

game_instance = Game()
app = RockPaperScissorsApp(game_instance)
app.run()
