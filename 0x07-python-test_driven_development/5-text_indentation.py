#!/usr/bin/python3
"""[5-text_indentation]
"""


def text_indentation(text):
    """[text_indentation]

    Arguments:
        text {[string]} -- [text to indent]

    Raises:
        TypeError: [text must be a string]
    """
    if type(text) not in [str]:
        raise TypeError("text must be a string")
    x = False
    for i in text.strip():
        if i != ' ':
            x = True
        if x == True:
            print(i, end='')
        if i in '.:?':
            print('\n')
            x = False
