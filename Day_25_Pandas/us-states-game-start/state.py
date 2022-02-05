from turtle import Turtle


class State(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('black')
        self.hideturtle()

    def update_state(self, x, y, state):
        self.goto(x, y)
        self.write(state, False, align='center', font=("Arial", 8, "normal"))
