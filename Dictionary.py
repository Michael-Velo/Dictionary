import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def translate(word):

    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s? Y for yes or N for no: " % get_close_matches(word, data.keys())[0])
        if yn == 'Y':
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == 'N':
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist.Please double check it."

while True:
    word = input("Enter word: ").lower()
    if word == "\end":
        print('Program has ended.Goodbye!')
        break

    output = translate(word)

    if type(output) == list:
        for item in output:
            print(item)
    else:
        print(output)
