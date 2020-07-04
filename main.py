"""
    Warehouse program
    Functionality:
        -  menu
        1: Register things to a catalog
            id (auto generated)
            title
            category
            price
            stock

        2: List the items on the catalog
"""

from menu import clear, print_menu, print_header
from item import Item
import pickle

# global variables
catalog = []
data_file = 'warehouse.data'


# functions

def save_catalog():
    global data_file # must import global variables into the funtion
    writer = open(data_file, 'wb') # open or create a file and write binary
    pickle.dump(catalog, writer)
    writer.close() # close the file
    print('** Item Saved **')

def read_catalog():
    global data_file
    try:
        reader = open(data_file, 'rb') # reads binary file
        temp_list = pickle.load(reader)

        for item in temp_list:
            catalog.append(item)

        print('** Data Loaded ** ' + str(len(catalog)) + ' Items loaded....')


    except:
        print('** ERROR ** - Could not load data from data file')


def register_item():
    print_header('Register New Item')
    try:
        title = input('Item Title: ')
        category = input('Category: ')
        price = float(input('Price: '))
        stock = int(input('Amount of Stock: '))

        # create an instance of Item
        new_item = Item(1, title, category, price, stock)
        catalog.append(new_item)


        print('** Item Created **')

    except:
        print("** ERROR ** - Verify values and try again")

def view_catalog():
    print_header('Catalog')
    print('Item'.rjust(2) + '   ' + 'Title'.ljust(25) + '   ' + 'Category'.ljust(15) + '   ' + 'Price'.rjust(15) + '   ' + 'Stock'.rjust(5))
    for i in catalog:

        print(str(i.id).rjust(4) 
        + ' | ' + i.title.ljust(25) 
        + ' | ' + i.category.ljust(15)
        + ' | ' + str(i.price).rjust(15)
        + ' | ' + str(i.stock).rjust(5))


# instructions

read_catalog()
input('Press Enter to begin')

opt = ''
while(opt != 'x'):
    clear()
    print_menu()

    opt = input('Please select an option: ')

    if(opt == '1'):
        register_item()
        save_catalog()
    elif(opt == '2'):
        view_catalog()
        


    input('...Press Enter to Continue...')