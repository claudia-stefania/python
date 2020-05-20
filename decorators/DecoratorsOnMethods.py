from decorators.Decorators import do_twice, my_decorator, timer, repeat


# nested decorators
@my_decorator
@do_twice
def say_whee():
    print("Whee!")


# @do_twice
@repeat(num_times=7)
def greet(name):
    print(f"Hello {name}")


@do_twice
def return_greeting(name):
    print("Creating greeting")
    return f"Hi {name}"


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
