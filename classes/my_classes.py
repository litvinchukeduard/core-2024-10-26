from dataclasses import dataclass

# from colorama import Fore, Style, Back

# from classes.exceptions.no_such_product_exception import NoSuchProductException
# from . import COLOR_BLACK

# from unittest import 
'''
Написати систему, яка буде керувати автомати для їжі
'''

# raise ValueError("Exception happened")



'''
    {
        "Snickers": Product(30, "Snickers", 200),
        "Coca cola": Product(20, "Coca cola", 150),
    }
'''

'''
{
    "price": 10,
    "name": "Snickers",
    "cals": 100
}

{
    Product(30, "Snickers", 200): 100,
    Product(20, "Coca cola", 150): 101,
}
'''

"""
1: Snickers
2: Coca cola
"""

@dataclass
class Product:
    id: int
    price: int
    name: str
    calories: int

    # def __eq__

    def __hash__(self):
        return self.id

'''
machine[1] -> Product
raise NoSuchProductException

'''
class Machine:

    def __init__(self, products_dict: dict, starting_money: int):
        self.products_dict = products_dict
        self.__money = None
        self.money = starting_money

    @property
    def money(self):
        return f'Amount of money "{self.__money}"'
    
    @money.setter
    def money(self, new_value: int):
        if new_value < 0:
            raise ValueError("Value should be greater or equals to zero")
        self.__money = new_value

    def add_product(self, product: Product, amount: int):
        if product.price > 100:
            raise ValueError
        self.products_dict[product] = amount

    def buy_product(self, id: int, amount_of_money: int) -> tuple[Product, int]:
        product = self[id]
        if amount_of_money >= product.price: 
            change = amount_of_money - product.price
            self.products_dict[product] -= 1
            return (product, change)
        raise NoSuchProductException(id)
        
    def __getitem__(self, id: int) -> Product:
        for (product, quantity) in self.products_dict.items():
            if product.id == id:
                return product
        raise NoSuchProductException(id)
    
    def __setitem__(self, product: Product, amount: int):
        self.products_dict[product] = amount

    def __str__(self):
        return f'Machine(products_dict={self.products_dict}, money={self.money})'



if __name__ == '__main__':

    # product_one = Product(1, 30, "Snickers", 300)
    # product_two = Product(2, 20, "Coca Cola", 150)

    # print(product_one, product_two)

    # with self.assertThrows(IndexError):
        # machine = Machine(dict(), 0)
        # print(machine.buy_product(3, 100))
    # machine.add_product(product_one, 100)
    # # print(machine)
    


    # print(machine)
    #"hello" -> 2344533
    #"hello" -> 2344533

    # print({
    #     Product(1, 30, "Snickers", 200): 100,
    #     Product(2, 20, "Coca cola", 150): 101,
    # })

    # my_dict = {"name": "Ihor", "surname": "Surname"}
    # print(my_dict.items())
    # for (key, value) in my_dict.items():
    #     print(value)

    # my_list = [1, 2, 3]

    # my_dict = {"name": "Ihor"}
    # # print(my_list["name"])
    # print(my_dict["name"])

    machine = Machine(dict(), 0)

    # machine.__money = -1000
    # print(machine)
    # machine._Machine__money = -1000
    machine.money = 1000
    print(machine.money)
    machine.money = 1143445
    print(machine.money)
    # product_one = Product(1, 30, "Snickers", 300)
    # machine.add_product(product_one, 100)
    # # print(machine[1])
    # print(machine.buy_product(1, 1000))

    # product_two = Product(2, 20, "Coca Cola", 150)

    # machine[product_two] = 1000

    # print(machine.money)
    # machine.money = "-1000"
    # print(machine)
    # machine.money + 1
