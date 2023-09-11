from tkinter import Button, Label, Tk
from PIL import Image, ImageTk
from src.game import game_instance


class RockPaperScissorsApp:
    def __init__(self, game):
        self.game = game
        self.root = Tk()
        self.root.title("Rock, Paper, Scissors Game")
        self.root.configure(background='#9b59b6')
        self.rock = ImageTk.PhotoImage(Image.open('src/static/rock.png'))
        self.paper = ImageTk.PhotoImage(Image.open('src/static/paper.png'))
        self.scissors = ImageTk.PhotoImage(Image.open('src/static/scissors.png'))
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

create_app = RockPaperScissorsApp(game_instance)