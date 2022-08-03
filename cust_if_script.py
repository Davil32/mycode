#!/usr/bin/env python3

message = 'The senior discount is '

# wrap age in a float() to accept decimals as numbers
age = float(input("What is your age?"))

# if input value was higher or equal to 65
if age >= 65:
    message = message + '$40.'
elif age >= 55:
    message = message + '$25.'
elif age >= 45:
    message = message + '$15.'
elif age >= 35:
    message = message + '$0.'
else:
    message = message + 'for 45 and over, children under 6 are free.'
print(message)
