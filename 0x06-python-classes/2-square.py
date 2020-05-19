#!/usr/bin/python3
''' 2-Square
    Create class for create and instance of a class
    adding aprivate variable (size)
    adding exceptions
'''


class Square:
    '''
    Square - adding exceptions
    @Atributtes: 1
    private:
        size
    public:
    '''
    def __init__(self, size=0):
        try:
            if size <= 0:
                raise Exception("size must be >= 0")
        except TypeError:
            raise Exception("size must be an integer")
        self.__size = size
