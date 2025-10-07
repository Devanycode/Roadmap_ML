def add(*args: int):    
    total = 0
    for number in args:
        total += number 
    print(total)
    print(sum(args))    # Ya que el argumento es una tupla 

add(1, 2, 3, 4, 5, 6, 7)

def calculate(**kwargs):
    print(kwargs)


calculate(add=3, multiply= 3)

class Car:

    def __init__(self, **kwargs):
        self.make = kwargs["make"]
        self.model = kwargs["model"]

my_car = Car(make="Nissan", model="GT-T")
print(my_car.model)

