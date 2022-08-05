# Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12



expected_string = input('Enter the Element : ')

def myfunc(a):
    
    upper_letters = ''
    lower_letters = ""

    for i in expected_string:
        if i.isupper():
            upper_letters += i
    
        elif i.islower():
            lower_letters +=i

    print(upper_letters)
    print(lower_letters)
    print(len(upper_letters))
    print(len(lower_letters))

myfunc(expected_string)

