from flask import Flask

app = Flask(__name__)


# Wrapper functions
def make_bold(function):
    def wrapper():
        output = function()
        output = f"<b>{output}</b>"
        return output

    return wrapper


def make_emphasis(function):
    def wrapper():
        output = function()
        output = f"<em>{output}</em>"
        return output

    return wrapper


def make_underline(function):
    def wrapper():
        output = function()
        output = f"<u>{output}</u>"
        return output

    return wrapper


@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
           '<p>This is a paragraph!</p>' \
           '<img src="https://media.giphy.com/media/ERy32lxHhXfpu/giphy.gif">'


@app.route("/bye")
@make_bold
@make_emphasis
@make_underline
def say_bye():
    return "Bye!"


@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name}, you are {number} years old!"


if __name__ == "__main__":
    app.run(debug=True)
