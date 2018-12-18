"""
A simple substitution cipher consists of substituting every plaintext character for a different ciphertext
character.
-plain alphabet : abcdefghijklmnopqrstuvwxyz
-cipher alphabet: phqgiumeaylnofdxjkrcvstzwb
Create a function that will take a text, cipher alphabet, and encipher/decipher
that will use the cipher alphabet to code/decode based off of it.
"""

def cipher(text, cipher_alphabet, option='encipher'):
    result = ""
    plain_alphabet = "abcdefghijklmnopqrstuvwxyz" #provided alphabet
    if option == "encipher":
        for char in text:
            if char == " ": # can be expanded upon to be able to encode other non-alphabet characters
                result += " "
            else:
                char_index = plain_alphabet.find(char) #finds the alphabet index of the character, and adds the cipher equivalent
                result += cipher_alphabet[char_index]
        return(result)
    elif option == "decipher":
        for char in text:
            if char == " ":
                result += " "
            else:
                char_index = cipher_alphabet.find(char)
                result += plain_alphabet[char_index]
        return(result)

cipher_alphabet = "phqgiumeaylnofdxjkrcvstzwb"
print(cipher("defend the east wall of the castle", cipher_alphabet, "encipher"))
print(cipher("giuifg cei iprc tpnn du cei qprcni", cipher_alphabet, "decipher"))
