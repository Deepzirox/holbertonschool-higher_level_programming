#!/usr/bin/python3
'''
1-my_list
'''
class MyList(list):
    '''
    Print sorted list
    '''
    def __getitem__(self, key):
        return super(MyList, self).__getitem__(key-1)

    def print_sorted(self):
        print(sorted(self))
