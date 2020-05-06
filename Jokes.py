import requests

ROOT_END_POINT = 'https://official-joke-api.appspot.com/'


class Joke:
    path = ''

    def __init__(self, path):
        self.path = path

    def jokes(self):
        jokesDictionary = requests.get(ROOT_END_POINT + self.path).json()
        for joke in jokesDictionary:
            print("They say : " + joke.get('setup'))
            print("And the joke is: " + joke.get('punchline'))
            print()


# myJoke = Joke('random_joke')
# myJoke.jokes()

jokes = Joke('jokes/ten')
jokes.jokes()
