'''Functions for product menu'''

from os import system 
import time

def replace_product(products):
    system('cls')
    #replaces item in list

    replace_item = input('Enter the name of the product you would like to replace or 0 to cancel: ').title()
    system('cls')
    if replace_item in products and replace_item != '0':
        new_item = input('Enter the name of the product you would like to replace it with: ').title()
        products[products.index(replace_item)] = new_item
        system('cls')
        print('Product has been replaced.')
        time.sleep(2)
    elif replace_product not in products and replace_item != '0':
        print('Product not in list.')
        time.sleep(2)
    system('cls')
    return products

def delete_product(products):
    #deletes product from produst list
    print()
    system('cls')
    del_item = input('Enter the product you would like to delete or 0 to cancel: ').title()
    system('cls')
    if del_item in products and del_item != '0':
        del products[products.index(del_item)]
        print('Product has been deleted.')
    elif del_item not in products and del_item != '0':
        print('Product not in list.')
    time.sleep(2)
    system('cls')
    return products

def add_new_product(products):
    #adds new item to product list
    print()
    system('cls')
    new_product = input('Enter the name of the new product: ').title()
    if new_product not in products:
        products.append(new_product)
        system('cls')
        print('Your product has been added.')
    else:
        system('cls')
        print('Product already in list')
    #pause program to show message
    time.sleep(2)
    system('cls')
    return products
