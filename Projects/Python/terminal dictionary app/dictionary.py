import json
from difflib import get_close_matches


dic_data = json.load(open("076 data.json"))
user_word = input("Search for a word: ")


def translate(word):
    if word.lower() in dic_data:
        definition = "\n".join(dic_data[word.lower()])
        return definition
    elif len(get_close_matches(word,dic_data.keys())) > 0:
        #comparing the word provided with the keywords in json data
        close_match = get_close_matches(word,dic_data.keys())[0]
        user = input("do you mean %s instead  Y or N: "  % close_match)
        if user == "Y":
            return("\n".join(dic_data[close_match]))
        elif user == "N":
            return("sorry, word not found")
        else:
            return("invalid entry")
    else:
        return("word not found!!!, please check your word")

print(translate(user_word))
