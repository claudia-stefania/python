import Jokes

# myJoke = Jokes.Joke('jokes/programming/random')
# myJoke.jokes()
#
# myTenJokes = Jokes.Joke('jokes/programming/ten')
# myTenJokes.jokes()

for path in ['random_ten', 'jokes/ten', 'jokes/programming/random', 'jokes/programming/ten']:
    myJoke = Jokes.Joke(path)
    myJoke.jokes()
    print()
    print('###################################################################################')
    print()

