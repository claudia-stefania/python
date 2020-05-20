from decorators.Decorators import do_twice, debug


# the decorators are being executed in the order they are listed.
# In other words, @debug calls @do_twice, which calls greet(),
# or debug(do_twice(greet()))
@debug
@do_twice
def greet(name):
    print(f"Hello {name}")


greet("Marcus")
