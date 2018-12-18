"""
codewars.com/kata/5287e858c6b5a9678200083c

A Narcissistic Number is a number which is the sum of its own digits,
each raised to the power of the number of digits in a given base.
Return True or False based on whether the number is narcissistic
"""

def narcissistic(value):
    sum = 0
    for char in str(value): #must be string to be iterable
        sum += int(char) ** len(str(value))
    return(sum == value)

print(narcissistic(89)) # is not narcissistic b/c 8^2 + 9^2 = 64 + 81 != 89
print(narcissistic(153)) # is narcissistic b/c  1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
