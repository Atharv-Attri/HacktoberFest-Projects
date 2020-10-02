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
    """
    >>> string = 'HACKTOBERFEST'
    >>> keyword = 'GITHUB'
    >>> keyword = keyword_equal_length(string, keyword)
    >>> cipher_text = ciphertext_vigenere(string, keyword)
    >>> print(cipher_text)
    NIVRNPHMKMYTZ
    """
    cipher = []
    for i in range(len(string)):
        letter = 65 + (ord(string[i]) + ord(keyword[i])) % 26
        cipher.append(chr(letter))
    return "".join(cipher)


def menu():
    exit = False

    while not exit:
        print('String: ', end='')
        string = input()
        print('Keyword: ', end='')
        keyword = input()

        string = string.upper()
        keyword = keyword.upper()

        keyword = keyword_equal_length(string, keyword)
        cipher_text = ciphertext_vigenere(string, keyword)
        print(cipher_text, '\n')

        print('Continue? Y : N ', end='')
        exit_chr = input()

        if exit_chr.upper() == 'N':
            exit = True


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    menu()
