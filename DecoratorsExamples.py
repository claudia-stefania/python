from Decorators import do_twice
from Decorators import my_decorator
from Decorators import timer


# @my_decorator
@do_twice
def say_whee():
    print("Whee!")


@do_twice
def greet(name):
    print(f"Hello {name}")


@do_twice
def return_greeting(name):
    print("Creating greeting")
    return f"Hi {name}"


# print(return_greeting("Adam"))
# hi_adam = return_greeting("Adam")
# print(hi_adam)
# print(return_greeting.__name__)


@timer
def my_factorial(number):
    factorial = 1
    for i in range(1, number + 1):
        factorial = factorial * i
    print("The factorial of", number, "is", factorial)


@timer
def my_fibonacci(how_many_numbers):
    n1, n2 = 0, 1
    count = 0

    # check if the number of terms is valid
    if how_many_numbers <= 0:
        print("Please enter a positive integer")
    elif how_many_numbers == 1:
        print("Print ", how_many_numbers, "numbers from Fibonacci :")
        print(n1)
    else:
        print("Fibonacci sequence:")
        while count < how_many_numbers:
            print(n1)
            nth = n1 + n2
            # update values
            n1 = n2
            n2 = nth
            count += 1


my_factorial(100000)
print("##################################")
# my_fibonacci(100)

# say_whee()
# greet("World")