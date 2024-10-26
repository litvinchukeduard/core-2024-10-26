from collections import UserDict, UserList


class MyList(UserList):
    pass


class MyDict(UserDict):
    '''
    {'Ihor': Record}
    '''
    def find(self, name: str):
        # return self[name]
        return self.items()



# my_list = list([1, 2, 3, 4, 5])
my_list = MyList([1, 2, 3, 4, 5])
# my_list_two = [6, 7, 8, 9]
my_list_two = MyList([6, 7, 8, 9])

print(my_list + my_list_two)
print(my_list[1])
print(my_list[1:5])
