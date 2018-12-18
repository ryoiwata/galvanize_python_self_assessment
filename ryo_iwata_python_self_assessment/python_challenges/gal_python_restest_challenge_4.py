"""
Challenge 4 of Python Retest

Implement a function that counts the number of isograms in a list of strings.
An isogram is a word that has no repeating letters, consecutive or nonconsecutive.
"""

def count_isograms(list_of_words):
    result = 0
    for word in list_of_words:
        char_dict = {}
        for char in word: #creates a dictionary with letters valued with the frequency of it
            if char.lower() in char_dict:
                char_dict[char.lower()] += 1
            else:
                char_dict[char.lower()] = 1
        char_values = list(char_dict.values()) #list function must be used because dictionary values can not be iterated through
        if all(val <= 1 for val in char_values): # all function allows all items in a list to be compared at once
            result += 1
    return(result)
print(count_isograms(['conduct', 'letter', 'contract', 'hours', 'interview']))
#result is 1 because only hours is an isogram
