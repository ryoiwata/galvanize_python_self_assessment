"""
codewars.com/kata/56a5d994ac971f1ac500003e

given a array of strings and integer k,
return the longest combination of k strings(in the order of the array)
"""

def longest_consec(strarr, k):
    if k <= 0 or len(strarr) == 0 or k > len(strarr):
        return("")
    turn_num = 0
    list_of_combined_words = []
    for turn in range(len(strarr) - k + 1): # the range must be such that it's possible to have k combinations of words
        combined_word = ""
        for word in strarr[turn_num:turn_num + k]: #this allows strarr to be iterated through by k words at a time
            combined_word += word
        list_of_combined_words.append(combined_word)
        turn_num += 1
    return(max(list_of_combined_words, key = len))
print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2))
