r"""
    Vigenere Cipher is a method of encrypting alphabetic text.
    The encryption of the original text is done using the
    Vigenère table
"""


def keyword_equal_length(string, keyword):
    if len(string) == len(keyword):
        return keyword

    key_list = []
    for i in range(len(string)):
        idx = i % len(keyword)
        key_list.append(keyword[idx])
    return "".join(key_list)


print(keyword_equal_length("DAVIDBANDA", "AARON"))
