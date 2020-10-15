#Python program to encrypt and decrypt morse code

# Dictionary representing the morse code chart 
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-'} 

#function for encrypting message into morse code
def encrypt (message):
    cipher = ''
    for letter in message:
        #Compares with dictionary and adds the corresponding morse code
        if letter != ' ':
            cipher += MORSE_CODE_DICT[letter] + ' '
        #1 space different character 2 space different word
        else:
            cipher += ' '
    return cipher                

#function for decrypting message from morse code
def decrypt (message):
    message += ' '
    decipher = ''
    morse = ''
    for letter in message:
        #checks for space and morse code of single character
        if letter!= ' ':
            i = 0
            morse += letter
        #i = 1 new character i = 2 new word    
        else:
            i += 1
            if i==2:
                decipher += ' '
            else:
                decipher += list (MORSE_CODE_DICT.keys())[list (MORSE_CODE_DICT.values()).index(morse)]
                morse = ''
    return decipher                        

def main():
    print ("Encryption and Decryption in Morse Code:")
    print ("1. Encryption")
    print ("2. Decryption")
    choice = input ("Enter your choice:")
    if(choice == '1'):
        print("Info : only capital letters is used for morse code")
        message = input ("Enter the message to be encrypted:")
        result = encrypt(message)
        print (result)

    elif(choice == '2'):
        message = input ("Enter the message to be decrypted:")
        result = decrypt(message)
        print (result)

    else:
        print ("Incorrect choice")    

if __name__ == '__main__':
    main()        
