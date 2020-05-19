#!/usr/bin/python3
''' 3-Square
    Create class for create and instance of a class
    adding aprivate variable (size)
    adding exceptions
    adding area calculation
'''


class Square:
    '''
    Square - adding exceptions
    @Atributtes: 1
    private:
        size
    public:
    @methods:
    Area:
        receive (self) | return (self.size ** 2)
    '''
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise Exception("size must be an integer")
        elif size < 0:
            raise Exception("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        '''
        area - calculate area of size given
        return area(size)
        '''
        return self.__size ** 2
