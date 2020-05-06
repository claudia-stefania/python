import requests

ROOT_END_POINT = 'https://official-joke-api.appspot.com/'


class Joke:
    path = ''

    def __init__(self, path):
        self.path = ROOT_END_POINT + path

    def joke(self):
        response = requests.get(self.path)
        return response

    def jokes(self):
        jokesDictionary = self.joke().json()
        for joke in jokesDictionary:
            print("They say : " + joke.get('setup'))
            print("And the joke is: " + joke.get('punchline'))
            print()


# jokes = Joke('jokes/programming/random')
# jokes.jokes()
