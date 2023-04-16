from functools import reduce
# import numpy as np
# import pandas as pd
import re

location = '../58585-0.txt'
with open(location, 'r', encoding="utf8") as f:
    prophet = f.read().split(' ')
#
# prophet = prophet[568::]  # Devuelve una lista en la que cada elemento es una palabra del texto
#
#
# def reference(x):
#
#     # Your code here:
#     text = r'\{[^}]*\}'
#     x = re.sub(text, "", x)
#     return x
#
#
# prophet_reference = map(reference, prophet)  # Devuelve una lista en la que cada elemento es una palabra del texto sin los {}
#
#
# def line_break(x):
#     '''
#     Input: A string
#     Output: A list of strings split on the line break (\n) character
#
#     Example:
#     Input: 'the\nbeloved'
#     Output: ['the', 'beloved']
#     '''
#
#     e = x.split('\n')
#
#     return e
#
#
# prophet_line = map(line_break, prophet_reference)
# prophet_flat = []
# for i in prophet_line:
#     for e in i:
#         prophet_flat.append(e)
#
# prophet_flat = " ".join(prophet_flat)
#
#
#
word_list = ['and', 'the', 'a', 'an']
#
#
# def word_filter(x):
#     # Your code here:
#     for i in x:
#         i = i.lower()
#         if i in word_list:
#             return False
#         else:
#             return True
#
#
# prophet_filter = []
# prophet_filter.append(filter(word_filter, prophet))
#
# print(prophet_filter)


def concat_space(a, b):

    return a + ' ' + b

x = reduce(concat_space, word_list)
print(x)