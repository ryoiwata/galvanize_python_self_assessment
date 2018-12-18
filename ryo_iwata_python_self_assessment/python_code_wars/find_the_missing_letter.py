"""
codewars.com/kata/5839edaa6754d6fec10000a2

Given an array of increasing letters(all caps or lower), return the missing letter
"""

import string
def find_missing_letter(chars):
    result = ""
    num = string.ascii_letters.find(chars[0]) #gets the alphabet index of the first letter in the array
    for letter in chars:
        if num == string.ascii_letters.find(letter):
            pass
        else:
            return(string.ascii_letters[num]) #using the ascii_letters helps keep track of the case
        num += 1
    return(result)

print(find_missing_letter(["a","b","d"]))
