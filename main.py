from classes import Machine

def main():
    machine = Machine({}, 0)
    while True:
        try:
            id = input("Please enter product number: ")
            amount = input("Please enter money: ")
            print(machine.buy_product(id, amount))
        except Exception as e:
            print(e)

if __name__ == '__main__':
    main()