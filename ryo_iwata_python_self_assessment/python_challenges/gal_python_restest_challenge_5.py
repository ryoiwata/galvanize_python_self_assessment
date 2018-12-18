"""
Challenge 5 of Python Retest

Write a function that manually sorts a list of integers.
Do not use the built-in sorted() function or the .sort()
string method. Write out your entire algorithm.
"""

def manual_sort(data_list):
    result = []
    num_list = data_list
    for num in range(len(num_list)): #used range instead of a list so that it can be changed
        result.append(min(num_list))
        num_list.remove(min(num_list))
    return(result)

print(manual_sort([4,6,9,1,2,6]))
