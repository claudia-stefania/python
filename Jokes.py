import requests

ROOT_END_POINT = 'https://official-joke-api.appspot.com'


class GetJoke:

    def get_jokes(self, path):
        return requests.get(ROOT_END_POINT + path)

    # def __display_jokes(self, joke_dictionary):
    #     for joke in joke_dictionary:
    #         print("They say : " + joke.get('setup'))
    #         print("And the joke is: " + joke.get('punchline'))
    #         print()

    def display_jokes(self, joke_dictionary):
        for joke in joke_dictionary:
            print("They say : " + joke.get('setup'))
            print("And the joke is: " + joke.get('punchline'))
            print()

    def get_random_jokes(self):
        # jokes = self.get_jokes("/random_ten")
        # return self.__jokes(jokes)
        return self.get_jokes("/random_ten").json()

    def get_ten_jokes(self):
        # jokes = self.get_jokes("/jokes/ten")
        # return self.__display_jokes(jokes)
        return self.get_jokes("/jokes/ten").json()

    def get_jokes_about_programming_random(self):
        # jokes = self.get_jokes("/jokes/programming/random")
        # return self.__display_jokes(jokes)
        return self.get_jokes("/jokes/programming/random").json()

    def get_ten_jokes_about_programing(self):
        # jokes = self.get_jokes("/jokes/programming/ten")
        # return self.__display_jokes(jokes)
        return self.get_jokes("/jokes/programming/ten").json()


jokes = GetJoke().get_ten_jokes_about_programing()
GetJoke().display_jokes(jokes)

# joke = GetJoke()
# joke.get_random_jokes()
# joke.get_ten_jokes()
# joke.get_jokes_about_programming_random()
# joke.verify_jokes_type(joke.get_ten_jokes_about_programing(), "programming")
