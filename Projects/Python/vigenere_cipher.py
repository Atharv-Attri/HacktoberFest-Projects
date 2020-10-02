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


def ciphertext_vigenere(string, keyword):
    cipher_text = []
    for i in range(len(string)):
        letter = 65 + (ord(string[i]) + ord(keyword[i])) % 26
        cipher_text.append(chr(letter))
    print("".join(cipher_text))


ciphertext_vigenere("DAVIDAARON", "AARONAARON")
