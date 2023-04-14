from functools import reduce
# import numpy as np
# import pandas as pd
import re

location = '../58585-0.txt'
with open(location, 'r', encoding="utf8") as f:
    prophet = f.read().split(' ')

prophet = prophet[568::]  # Devuelve una lista en la que cada elemento es una palabra del texto


def reference(x):

    # Your code here:
    text = r'\{[^}]*\}'
    x = re.sub(text, "", x)
    return x


prophet_reference = map(reference, prophet)  # Devuelve una lista en la que cada elemento es una palabra del texto sin los {}


def line_break(x):
    '''
    Input: A string
    Output: A list of strings split on the line break (\n) character

    Example:
    Input: 'the\nbeloved'
    Output: ['the', 'beloved']
    '''

    e = x.split('\n')

    return e


prophet_line = map(line_break, prophet_reference)

# print(list(prophet_line))
for i in prophet_line:
    print(i)
    for e in i:  # i = ['the', 'beloved,']
        z = [' '.join(e).replace(',', '')]
        print(z)
x = " ".join(prophet_line)

print(x)
