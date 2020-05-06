import requests

# response = requests.get('https://official-joke-api.appspot.com/random_joke')
#
# jsonResponse = response.json()
#
# # print(response.content)
# # print(response.text)
#
# print(jsonResponse)
#
# print("The question? : " + jsonResponse['setup'])
# print("The question? : " + jsonResponse.get('setup'))
#
# print("And the joke : " + jsonResponse['punchline'])

responseWithJokes = requests.get('https://official-joke-api.appspot.com/jokes/ten')
jokesDictionary = responseWithJokes.json()

print(jokesDictionary)

# print(jsonResponseTen[0].get('setup'))
# print(jsonResponseTen[0].get('punchline'))

for joke in jokesDictionary:
    print("The question? : " + joke.get('setup'))
    print("And the joke : " + joke.get('punchline'))
    print()