'''Menus'''
from order_menu_functions import *
from product_menu_functions import *
from courier_menu_functions import *
from customer_menu_functions import *
from os import system
import time
import pymysql
from tabulate import tabulate

def customer_menu(cur, con):
    menu = True
    system('cls')
    #customer menu
    while menu == True:
        print()
        print('Welcome to the orders menu')
        print('Select one of the following options')
        print()
        #Menu Options
        print('0)Return to main menu\n1)Show customers\n2)Create new customer \n3)Update customer\n4)Delete customer')
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
            cur.execute('SELECT * FROM customers')
            customers = cur.fetchall()
            print(tabulate(customers, headers = 'keys' ))
        elif user == 2:
            add_customer(cur, con)
        elif user == 3:
            update_customer(cur, con)
        elif user == 4:
            delete_customer(cur, con)
        else:
            system('cls')
            print('please select one of the options.')
            time.sleep(2)
            system('cls')
        
    return cur, con
        

def order_menu(cur, con):
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
        if user == 0:
            menu = False
        elif user == 1:
            system('cls')
            cur.execute('SELECT * FROM orders ORDER BY status')
            orders = cur.fetchall()
            print(tabulate(orders, headers = 'keys' ))
        elif user == 2:
            create_new_order(cur, con)
        elif user == 3:
            update_order_status(cur, con)
        elif user == 4: 
            update_order(cur, con)
        elif user == 5:
            delete_order(cur, con)
        else:
            system('cls')
            print('please select one of the options.')
            time.sleep(2)
            system('cls')
    return cur, con
        
def courier_menu(cur, con):
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
            menu =False
        elif user == 1:
            system('cls')
            cur.execute('SELECT id, name, phone_number FROM couriers')
            couriers = cur.fetchall()
            print(tabulate(couriers, headers = 'keys' ))
        elif user == 2:
            add_new_courier(cur, con)
        elif user == 3:
            replace_courier(cur, con)
        elif user == 4: 
            delete_courier(cur, con)
        else:
            system('cls')
            print('please select one of the options.')
            time.sleep(2)
            system('cls')
    return cur, con

def product_menu(cur, con):
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
            cur.execute('SELECT id, name, price FROM products')
            products = cur.fetchall()
            print(tabulate(products, headers = 'keys' ))
        elif user == 2:
            add_new_product(cur, con)
        elif user == 3:
            replace_product(cur, con)
        elif user == 4: 
            delete_product(cur, con)
        else:
            system('cls')
            print('please select one of the options.')
            time.sleep(2)
            system('cls')
    return cur, con
            
    
def main_menu(cur, con):
    system('cls')
    #Main Menu
    menu = True
    while menu == True:
        #Menu
        print()
        print('Welcome to the main menu')
        print('Select one of the following options')
        print()
        print('0)Save & Exit App\n1)View Product Menu\n2)View Courier Menu\n3)View Customer Menu\n4)View Order Menu')
        print()
        #if user inputs string except a Value Error
        while True:
            try:
                user = int(input('Enter Option [0|1|2|3|4]: '))
            except ValueError:
                print('Please Enter [0|1|2|3|4].')
            else:
                break
        print()
        #if user selects 0
        if user == 0:
            menu = False
        #if user selects 1
        elif user == 1:
            cur, con = product_menu(cur, con)
        elif user == 2:
            cur, con = courier_menu(cur, con)
        elif user == 3:
            cur, con = customer_menu(cur, con)
        elif user == 4:
            cur,con = order_menu(cur,con)
        #if user selects anything else
        else:
            print('Must select one of the options.')
            print()
        system('cls')
    return cur, con