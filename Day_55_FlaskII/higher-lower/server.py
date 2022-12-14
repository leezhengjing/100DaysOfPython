from flask import Flask
from random import randint

app = Flask(__name__)

random_number = randint(0, 9)

def make_h1(function):
    def wrapper():
        output = f"<h1>{function()}</h1>"
        return output
    return wrapper

@make_h1
@app.route('/')
def hello_world():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"


@app.route('/<int:number>')
def number_check(number):
    if number < random_number:
        return "<h1 style='color:red'>Too low, try again!</h1>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"
    elif number > random_number:
        return "<h1 style='color:purple'>Too high, try again!</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"
    else:
        return "<h1 style='color:green'>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"

if __name__ == "__main__":
    app.run(debug=True)