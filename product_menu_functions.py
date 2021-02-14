'''Functions for product menu'''

from os import system 
import time

def replace_product(cur, con):
    system('cls')
    #replaces item in list
    replace_item = input('Enter the name of the product you would like to replace or 0 to cancel: ').title()
    system('cls')
    name_in_list = False
    cur.execute('SELECT name, price FROM products')
    products = cur.fetchall()
    for product in products:
        if replace_item in product.values() and replace_item != '0':
            name = input('Enter new name of the product or leave field blank to keep the same: ').title()
            system('cls')
            price = input('Enter new price of the product or leave field blank to keep the same: ')
            if name != '':
                cur.execute(f'''UPDATE products
                                SET name = '{name}'
                                WHERE name = '{replace_item}' ''')
                con.commit()
                system('cls')
                print('Name has been updated')
                time.sleep(2)
            if price != '':
                price = float(price)
                cur.execute(f'''UPDATE products
                                SET price = '{price}'
                                WHERE name = '{replace_item}' ''')
                con.commit()
                system('cls')
                print('Price has been updated')
            name_in_list = True
    else:
        if name_in_list == False:
            print(f'{replace_item} not in list.')
    time.sleep(2)
    system('cls')

def delete_product(cur, con):
    #deletes product from produst list
    print()
    system('cls')
    del_item = input('Enter the product you would like to delete or 0 to cancel: ').title()
    system('cls')
    cur.execute('SELECT name, price FROM products')
    products = cur.fetchall()
    res = False
    for product in products:
        if del_item in product.values() and del_item != '0':
            cur.execute(f'''DELETE FROM products
                            WHERE name = '{del_item}' ''')
            con.commit()
            res = True
            print(f'{del_item} has been deleted')
    if res == False and del_item != '0':
        print(f'{del_item} not in list.')
    time.sleep(2)
    system('cls')

def add_new_product(cur, con):
    #adds new item to product list as a dictionary
    print()
    system('cls')
    new_product = input('Enter the name of the new product: ').title()
    system('cls')
    res = False
    cur.execute('SELECT name FROM products')
    products = cur.fetchall()
    for product in products:
        if new_product in product.values():
            print(f'{new_product} already in list')
            res = True
            break
    if res == False:
        price = float(input('Enter the price of the product: '))
        system('cls')
        cur.execute('''INSERT INTO products(name,price)
                        VALUES(%s,%s)''',(new_product,price))
        con.commit()
        print(f'{new_product} has been added')
    #pause program to show message
    time.sleep(2)
    system('cls')
