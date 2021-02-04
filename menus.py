'''Menus'''
from order_menu_functions import *
from product_menu_functions import *
from courier_menu_functions import *
from os import system
import time

def order_menu(orders):
    system('cls')
    #Order menu
    menu = True
    while menu == True:
        print()
        print('Welcome to the orders menu')
        print('Select one of the following options')
        print()
        #Menu Options
        print('0)Return to main menu\n1)Show orders\n2)Create new order \n3)Update Order status\n4)Update Order\n5)Delete Order')
        print()
        #user enters option, if value error re-enter option
        while True:
            try:
                user = int(input('Enter Option [0|1|2|3|4|5]: '))
            except ValueError:
                print('Please Enter [0|1|2|3|4|5].')
            else:
                break
        print()
        if user == 0:
            menu = False
        elif user == 1:
            system('cls')
            #prints courier list
            for order in orders:
                print(f'Order: {order}')
        elif user == 2:
            orders = create_new_order(orders)
        elif user == 3:
            orders = update_order_status(orders)
        elif user == 4: 
            orders = update_order(orders)
        elif user == 5:
            orders = delete_order(orders)
        else:
            system('cls')
            print('please select one of the options.')
            time.sleep(2)
            system('cls')
    return orders
        
def courier_menu(couriers):
    system('cls')
    #Courier Menu
    menu = True
    while menu == True:
        print()
        print('Welcome to the courier menu')
        print('Select one of the following options')
        print()
        #Menu Options
        print('0)Return to main menu\n1)Show couriers\n2)Create new courier \n3)Update courier\n4)Delete courier')
        print()
        #user enters option, if value error re-enter option
        while True:
            try:
                user = int(input('Enter Option [0|1|2|3|4]: '))
            except ValueError:
                print('Please Enter [0|1|2|3|4].')
            else:
                break
        print()
        if user == 0:
            menu = False
        elif user == 1:
            system('cls')
            #prints courier list
            for courier in couriers:
                print(f'Courier: {courier["Name"]} {courier["Phone Number"]}')
        elif user == 2:
            couriers = add_new_courier(couriers)
        elif user == 3:
            couriers = replace_courier(couriers)
        elif user == 4: 
            couriers = delete_courier(couriers)
        else:
            system('cls')
            print('please select one of the options.')
            time.sleep(2)
            system('cls')
    return couriers
    

def product_menu(products):
    system('cls')
    #Product Menu
    menu = True
    while menu == True:
        print()
        print('Welcome to the product menu')
        print('Select one of the following options')
        print()
        #Menu Options
        print('0)Return to main menu\n1)Show Products\n2)Create new product\n3)Replace product\n4)Delete product')
        print()
        #user enters option, if value error re-enter option
        while True:
            try:
                user = int(input('Enter Option [0|1|2|3|4]: '))
            except ValueError:
                print('Please Enter [0|1|2|3|4].')
            else:
                break
        print()
        if user == 0:
            menu = False
        elif user == 1:
            #print product list
            system('cls')
            for product in products:
                print(f'Product: {product["Name"]} £{product["Price"]}')
        elif user == 2:
            products = add_new_product(products)
        elif user == 3:
            products = replace_product(products)
        elif user == 4: 
            products = delete_product(products)
        else:
            system('cls')
            print('please select one of the options.')
            time.sleep(2)
            system('cls')
    return products
            
            
    
def main_menu(products, couriers, orders):
    system('cls')
    #Main Menu
    menu = True
    while menu == True:
        #Menu
        print()
        print('Welcome to the main menu')
        print('Select one of the following options')
        print()
        print('0)Save & Exit App\n1)View Product Menu\n2)View Courier Menu\n3)View Order Menu')
        print()
        #if user inputs string except a Value Error
        while True:
            try:
                user = int(input('Enter Option [0|1|2|3]: '))
            except ValueError:
                print('Please Enter [0|1|2|3].')
            else:
                break
        print()
        #if user selects 0
        if user == 0:
            menu = False
        #if user selects 1
        elif user == 1:
            products = product_menu(products)
        elif user == 2:
            couriers = courier_menu(couriers)
        elif user == 3:
            orders = order_menu(orders)
        #if user selects anything else
        else:
            print('Must select one of the options.')
            print()
        system('cls')
    return products, couriers, orders