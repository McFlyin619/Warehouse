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

        write data to a file
        load data from the file

        3: Update the stock manually
            - display the list of items
            - ask user tot choose an id
            - read the id
            - travel the catalog array and find the item with id = id
            - ask for new stock value 
            - update stock

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
        id = 1
        if(len(catalog) > 0):
            last = catalog[-1]
            id = last.id + 1 
        new_item = Item(id, title, category, price, stock)
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
        print('-' * 77)

def update_stock():
    view_catalog()
    update_id = input('Choose an item id: ')
    
    found = False
    for item in catalog:
        if(str(item.id) == update_id):
            found = True
            new_stock = input("Please provide new stock number: ")
            item.stock = int(new_stock)

    if(not found):
        print('** ERROR ** - Selected id does not exist')       


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
    elif(opt == '3'):
        update_stock()
        save_catalog()
        


    input('...Press Enter to Continue...')