'''order menu functions'''
from os import system
import time 
from tabulate import tabulate

#Create new order
def create_new_order(cur, con):
    system('cls')
    cur.execute('SELECT customer_name, customer_id FROM customers')
    customers = cur.fetchall()
    print(tabulate(customers, headers = 'keys' ))
    print()
    customer = 0
    while True:
        try:
            customer = int(input('Enter the id of the customer you want to add to the order: '))
        except ValueError:
            print('Please select a number')
        else:
            break
    system('cls')
    product_idx = []
    item = 1
    cur.execute('SELECT id, name FROM products')
    products = cur.fetchall()
    while item != 0:
        print(tabulate(products, headers = 'keys' ))
        print()
        while True:
            try:
                item = int(input('Enter the id of the product you want to order or 0 to continue: '))
            except ValueError:
                print('Please select a number')
            else:
                break
        system('cls')
        if item != 0:
            product_idx.append(item)
    courier_idx = 0
    cur.execute('SELECT id, name FROM couriers')
    couriers = cur.fetchall()
    print(tabulate(couriers, headers = 'keys' ))
    print()
    while True:
        try:
            item = int(input('Enter the id of the courier you want to add to the order: '))
        except ValueError:
            print('Please select a number')
        else:
            break
    courier_idx = item  
    status = 'Preparing'
    product_idx = (f'{product_idx}')
    cur.execute('''INSERT INTO orders(customer_id, courier, status, items)
                    VALUES(%s,%s,%s,%s)''',(customer, courier_idx , status, product_idx))
    con.commit()
    system('cls')
    print('Your order has been added')
    time.sleep(2)
    system('cls')
    

#update order status1
def update_order_status(cur, con):
    res = True
    system('cls')
    cur.execute('''SELECT o.customer_id, c.customer_name
                    FROM orders o
                    JOIN customers c
                    ON o.customer_id = c.customer_id''')
    orders = cur.fetchall()
    print(tabulate(orders, headers = 'keys' ))
    print()
    order_name = int(input('Enter the id of order you would like to update or 0 to cancel: '))
    for order in orders:
        if order_name in order.values():
            menu = True
            res = False
            while menu == True:
                system('cls')
                print('0)Out for delivery\n1)Delivered')
                print()
                while True:
                    try:
                        user = int(input('Enter Option [0|1]: '))
                    except ValueError:
                        print('Please Enter [0|1].')
                    else:
                        break
                if user == 0:
                        cur.execute(f'''UPDATE orders
                                        SET status = 'Out for delivery'
                                        WHERE customer_id = {order_name} ''')
                        con.commit()
                        system('cls')
                        print('Status updated')
                        
                        time.sleep(2)
                        menu = False
                elif user == 1:
                        cur.execute(f'''UPDATE orders
                                        SET  status = 'Delivered'
                                        WHERE customer_id = {order_name} ''')
                        con.commit()
                        system('cls')
                        print('Status updated')
                        time.sleep(2)
                        menu = False
    if res == True and order_name != 0:
        system('cls')
        print(f'{order_name} not in list')
        time.sleep(2)
    system('cls')
            
            
            
#updates order
def update_order(cur, con):
    res = False
    system('cls')
    cur.execute('''SELECT o.customer_id, c.customer_name
                    FROM orders o
                    JOIN customers c
                    ON o.customer_id = c.customer_id''')
    orders = cur.fetchall()
    print(tabulate(orders, headers = 'keys' ))
    print()
    order_to_update = int(input('Enter the id of the order you would like to update or 0 to cancel: '))
    system('cls')
    for order in orders:
        if order_to_update == order['customer_id']:
            res = True
            cur.execute('SELECT customer_id, customer_name FROM customers')
            customers = cur.fetchall()
            print(tabulate(customers, headers = 'keys' ))
            print()
            customer = 0
            while True:
                try:
                    customer = int(input('Enter the id of the customer you want to add to the order or 0 to continue: '))
                except ValueError:
                    print('Please select a number')
                else:
                    break
            system('cls')
            product_idx = []
            item = 1
            while item != 0:
                cur.execute('SELECT id, name FROM products')
                products = cur.fetchall()
                print(tabulate(products, headers = 'keys' ))
                print()
                while True:
                    try:
                        item = int(input('Enter the id of the product you want to order or 0 to continue: '))
                    except ValueError:
                        print('Please select a number')
                    else:
                        break
                system('cls')
                if item != 0:
                    product_idx.append(item)
            cur.execute('SELECT id, name FROM couriers')
            couriers = cur.fetchall()
            print(tabulate(couriers, headers = 'keys' ))
            print()
            courier = 0
            while True:
                try:
                    courier = int(input('Enter the id of the courier you want to add to the order or 0 to continue: '))
                except ValueError:
                    print('Please select a number')
                else:
                    break
            if customer != 0:
                cur.execute(f'''UPDATE orders
                                SET customer_id = '{customer}'
                                WHERE customer_id = '{order_to_update}' ''')
            if product_idx != []:
                cur.execute(f'''UPDATE orders
                                SET items = '{product_idx}'
                                WHERE customer_id = '{order_to_update}' ''')
                con.commit()
            if courier != 0:
                cur.execute(f'''UPDATE orders
                                SET courier = '{courier}'
                                WHERE customer_id = '{order_to_update}' ''')
                con.commit()
    if order_to_update != 0 and res == False:
        system('cls')
        print(f'{order_to_update} not in list')
        time.sleep(2)
    system('cls')


def delete_order(cur, con):
    system('cls')
    res = False
    cur.execute('SELECT * FROM orders')
    orders = cur.fetchall()
    print(tabulate(orders, headers = 'keys' ))
    print()
    del_order = int(input('Enter order id to delete or 0 to cancel: '))
    for order in orders:
        if del_order in order.values():
            system('cls')
            cur.execute(f'''DELETE FROM orders
                            WHERE id = '{del_order}' ''')
            con.commit()
            print('Order has been deleted')
            time.sleep(2)
            res = True
    if del_order != 0 and res == False:
        system('cls')
        print(f'{del_order} not in list')
        time.sleep(2)
    
    system('cls')

            
    