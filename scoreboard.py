from turtle import Turtle
FONT = ("Arial", 20, "normal") 
ALIGNMENT = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,220)
        self.update_scoreboard()
        self.hideturtle()
    
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align = ALIGNMENT, font = FONT)

    def game_over(self):
        self.goto(0 ,0)
        self.write("GAME OVER", align = ALIGNMENT, font = FONT)
    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()