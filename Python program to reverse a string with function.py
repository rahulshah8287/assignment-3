# Write a Python program to reverse a string.

# Sample String : "1234abcd"

# Expected Output : "dcba4321"

from unittest import result


expected_string = input('Enter the Element : ')

def reverse_string():
    result_string = " "
    for i in expected_string:
        result_string = i + result_string
    print(f'reverse string is {result_string}')

reverse_string()
