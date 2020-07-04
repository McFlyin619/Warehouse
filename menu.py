import os

# functions
def print_menu():
    print('-' * 40)
    print('Warehouse Control System')
    print('-' * 40)

    print('[1] Register new items')
    print('[2] View Catalog')
    print('[3] Update Stock')
    print('[x] Close')

def print_header(title):
    clear()
    print('-' * 77)
    print(' ' + title)
    print('-' * 77)


def clear():
    return os.system('cls' if os.name == 'nt' else 'clear')