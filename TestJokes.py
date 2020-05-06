from Jokes import GetJoke


class TestForJokes:

    # def __init__(self):
    #     self.get_joke = GetJoke()

    # def verify_jokes_number(self):
    #     if len(self.get_joke.get_random_jokes()) != 10:
    #         return "Number of jokes is not 10!"
    #     return "There are 10 jokes!"
    #
    # def verify_jokes_type(self, expected_type):
    #     checker = True
    #     for joke_child in self.get_joke.get_jokes_about_programming_random():
    #         if joke_child.get('type') != expected_type:
    #             print("Joke: \"" + joke_child.get('setup') + "\" does not have expected type: " + expected_type)
    #             checker = False
    #
    #     if checker:
    #         print("All jokes have expected type: " + expected_type)

    def verify_jokes_type(self, jokes_dictionary, expected_type):
        checker = True
        for joke_child in jokes_dictionary:
            if joke_child.get('type') != expected_type:
                print("Joke: \"" + joke_child.get('setup') + "\" does not have expected type: " + expected_type)
                checker = False

        if checker:
            print("All jokes have expected type: " + expected_type)

    def verify_jokes_number(self, jokes_dictionary):
        if len(jokes_dictionary) != 10:
            return "Number of jokes is not 10!"
        return "There are 10 jokes!"


# TestForJokes().verify_jokes_type("programming")

my_jokes = GetJoke().get_ten_jokes_about_programing()
TestForJokes().verify_jokes_type(my_jokes, "programming")

your_jokes = GetJoke().get_ten_jokes()
print(TestForJokes().verify_jokes_number(my_jokes))
