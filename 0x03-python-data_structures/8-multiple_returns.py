#!/usr/local/python3
def multiple_returns(sentence):
    strhandler = None
    lenght = 0
    if sentence != '':
        strhandler = sentence[0]
        lenght = len(sentence)

    return (lenght, strhandler)

