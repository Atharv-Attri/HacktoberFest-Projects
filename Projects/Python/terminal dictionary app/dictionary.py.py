import json
#python module that compares sequence
from difflib import get_close_matches

#json file
dic_data = json.load(open("076 data.json"))
user_word = input("Search for a word: ")


def translate(word):
    if word.title() in dic_data:
        definition = "\n".join(dic_data[word.title()])
        return definition
    elif word.upper() in dic_data:
        definition = "\n".join(dic_data[word.upper()])
        return definition
    elif word.lower() in dic_data:
        definition = "\n".join(dic_data[word.lower()])
        return definition
    elif len(get_close_matches(word,dic_data.keys())) > 0:
        #comparing the word provided with the keywords in json data
        close_match = get_close_matches(word,dic_data.keys())[0]
        user = input("did you mean %s instead  yes or no: "  % close_match)
        if user == "yes":
            return("\n".join(dic_data[close_match]))
        elif user == "no":
            return("the word does not exist")
        else:
            return("please check your entry")
    else:
        return("word not found!!!, please check your word")

print(translate(user_word))
