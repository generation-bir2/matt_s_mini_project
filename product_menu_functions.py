'''Functions for product menu'''

from os import system 
import time

def replace_product(products):
    system('cls')
    #replaces item in list
    replace_item = input('Enter the name of the product you would like to replace or 0 to cancel: ').title()
    system('cls')
    name_in_list = False
    for product in products:
        if replace_item in product.values() and replace_item != '0':
            name = input('Enter new name of the product or leave field blank to keep the same: ')
            system('cls')
            price = float(input('Enter new price of the product or leave field blank to keep the same: '))
            if name != '':
                product['Name'] = name
                system('cls')
                print('Name has been updated')
                time.sleep(2)
            if price != None:
                product['Price'] = price
                system('cls')
                print('Price has been updated')
            name_in_list = True
    else:
        if name_in_list == False:
            print(f'{replace_item} not in list.')
    time.sleep(2)
    system('cls')
    return products

def delete_product(products):
    #deletes product from produst list
    print()
    system('cls')
    del_item = input('Enter the product you would like to delete or 0 to cancel: ').title()
    system('cls')
    count = 0
    res = False
    for product in products:
        if del_item in product.values() and del_item != '0':
            del products[count]
            print(f'{del_item} has been deleted.')
            res = True
        count += 1
    if res == False:
        print(f'{del_item} not in list.')
    time.sleep(2)
    system('cls')
    return products

def add_new_product(products):
    #adds new item to product list as a dictionary
    print()
    system('cls')
    new_product = input('Enter the name of the new product: ').title()
    system('cls')
    res = False
    for product in products:
        if new_product in product.values():
            print(f'{new_product} already in list')
            res = True
            break
    if res == False:
        price = float(input('Enter the price of the product: '))
        system('cls')
        product_dict = {
            'Name': new_product,
            'Price': price
        }
        products.append(product_dict)
        print(f'{new_product} has been added')
    #pause program to show message
    time.sleep(2)
    system('cls')
    return products
