"""
Write a function that counts the number of times a given letter appears in a document.
The output should be in a dictionary.

Names of file must include the type of file at the end (i.e. .txt for txt files)
"""

def file_opener(file_name):
    opened_text_file = open(file_name, "r")
    text_file_output = opened_text_file.read()
    opened_text_file.close()
    return(text_file_output)

def letter_counter(file_name,letters_to_count):
    result = {}
    text_to_be_counted = file_opener(file_name)
    for char in text_to_be_counted:
        if char in letters_to_count:
            if char in result:
                result[char] += 1
            elif char not in result:
                result[char] = 1
    return(result)

print(letter_counter("file.txt", "aeiou"))
