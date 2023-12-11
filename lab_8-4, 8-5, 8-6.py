"""
Create a Python file named lab_8-4.py

*** You must write a comment for every chunk of code you write from now on along with your author tag***

Write a function count_a(word) that takes in a string word and returns the number of a's in the word. 
The function should count both lowercase (a) and uppercase (A)
"""
# Liam O'Hara

def count_a(word):
    # This is Counting both lowercase and uppercase 'a's
    return word.lower().count('a')

# Example:
word = "Alabama"
result = count_a(word)
print(f"The number of 'a's in '{word}' is: {result}")

"""
Create a Python file named lab_8-5.py

Write a function factorial(num) that takes in a number num 
and returns the product of all numbers from 1 up to and including num
"""
# Liam O'Hara

def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)
result = factorial(9)
print(result)

"""
Create a Python file named lab_8-6.py

Write a function is_palindrome(word) that takes in a string word 
and returns the true if the word is a palindrome, false otherwise. 

A palindrome is a word that is spelled the same forwards and backwards.
"""
# Liam O'Hara

def is_palindrome(word):
    # This will make the word undercase
    lowercase_word = word.lower()
    
    # reverse_word reverses the undercased word through slicing
    reversed_word = lowercase_word[::-1]
    
    return lowercase_word == reversed_word

word_to_check = "word"
result = is_palindrome(word_to_check)

# Print the result
print(f"The word '{word_to_check}' is a palindrome: {result}")