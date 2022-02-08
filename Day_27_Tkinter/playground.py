def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total


print(add(1, 2, 3, 4, 5, 6, 7, 8))


def calculate(n, **kwargs):
    # for key,value in kwargs.items()
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")

my_car = Car(make="Nissan")
print(my_car.model)

def test(*args):
    print(args)

test(1, 2, 3, 4)
