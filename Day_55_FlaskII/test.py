
def logging_decorator(function):
    def wrapper(*args):
        print(f"You called {function.__name__}{args}")
        print(f"It returned: {function(*args)}")
        return function(*args)

    return wrapper


@logging_decorator
def a_function(*args):
    return sum(args)

a_function(1, 2, 3)


def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return

        func(a, b)
    return inner


@smart_divide
def divide(a, b):
    print(a/b)

divide(2,0)