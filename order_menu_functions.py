'''order menu functions'''
from os import system
import time 

#Create new order
def create_new_order(cur, con):
    system('cls')
    name = input('Please enter the name of the customer: ').title()
    system('cls')
    address = input('Please enter the address of the customer: ')
    system('cls')
    phone_number = input('Please enter the phone number of the customer: ')
    system('cls')
    product_idx = []
    item = 1
    cur.execute('SELECT id, name FROM products')
    products = cur.fetchall()
    while item != 0:
        for product in products:
            print(f"ID:{product['id']}          {product['name']}")
        print()
        while True:
            try:
                item = int(input('Enter the id of the product you want to order, or 0 to continue: '))
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
    for courier in couriers:
        print(f"ID:{courier['id']}          {courier['name']}")
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
    cur.execute('''INSERT INTO orders(customer_name, customer_address, customer_phone, courier, status, items)
                    VALUES(%s,%s,%s,%s,%s,%s)''',(name, address, phone_number, courier_idx , status, product_idx))
    con.commit()
    system('cls')
    print('Your order has been added')
    time.sleep(2)
    system('cls')
    

#update order status1
def update_order_status(cur, con):
    res = True
    system('cls')
    cur.execute('SELECT customer_name FROM orders')
    orders = cur.fetchall()
    for order in orders:
        print(f"Order: {order['customer_name']}")
    print()
    order_name = input('Enter the name of the person who\'s order you would like to update or 0 to cancel: ').title()
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
                                        WHERE customer_name = '{order_name}' ''')
                        con.commit()
                        system('cls')
                        print('Status updated')
                        time.sleep(2)
                        menu = False
                elif user == 1:
                        cur.execute(f'''UPDATE orders
                                        SET  status = 'Delivered'
                                        WHERE customer_name = '{order_name}' ''')
                        con.commit()
                        system('cls')
                        print('Status updated')
                        time.sleep(2)
                        menu = False
    if res == True and order_name != '0':
        system('cls')
        print(f'{order_name} not in list')
        time.sleep(2)
    system('cls')
            
            
            
#updates order
def update_order(cur, con):
    res = False
    system('cls')
    cur.execute('SELECT * FROM orders')
    orders = cur.fetchall()
    for order in orders:
        print(f'Order: {order}')
        print()
    order_to_update = input('Enter the name of the order you would like to update or 0 to cancel: ').title()
    for order in orders:
        if order_to_update == order['customer_name']:
            system('cls')
            name = input('Please enter the name of the customer or leave blank to skip: ').title()
            system('cls')
            address = input('Please enter the address of the customer or leave blank to skip: ')
            system('cls')
            phone_number = input('Please enter the phone number of the customer or leave blank to skip: ')
            system('cls')
            product_idx = []
            item = 1
            while item != 0:
                cur.execute('SELECT id, name FROM products')
                products = cur.fetchall()
                for product in products:
                    print(f"ID:{product['id']}          {product['name']}")
                while True:
                    try:
                        item = int(input('Enter the  of the product you want to order, or 0 to continue: '))
                    except '':
                        break
                    except ValueError:
                        print('Please select a number')
                    else:
                        break
                system('cls')
                if item != 0:
                    product_idx.append(item)
            courier_idx = []
            cur.execute('SELECT id, name FROM couriers')
            couriers = cur.fetchall()
            for courier in couriers:
                print(f"ID:{courier['id']}          {courier['name']}")
            while True:
                try:
                    item = int(input('Enter the index of the courier you want to add to the order or 0 to continue: '))
                except ValueError:
                    print('Please select a number')
                else:
                    break
            if item != 0:
                courier_idx.append(item) 
            if name != '':
                cur.execute(f'''UPDATE orders
                                SET customer_name = '{name}'
                                WHERE customer_name = '{order_to_update}' ''')
                con.commit()
            if address != '':
                cur.execute(f'''UPDATE orders
                                SET customer_address = '{address}'
                                WHERE customer_name = '{order_to_update}' ''')
                con.commit()
            if phone_number != '':
                cur.execute(f'''UPDATE orders
                                SET customer_phone = '{phone_number}'
                                WHERE customer_name = '{order_to_update}' ''')
                con.commit()
            if product_idx != []:
                cur.execute(f'''UPDATE orders
                                SET items = '{product_idx}'
                                WHERE customer_name = '{order_to_update}' ''')
                con.commit()
            if courier_idx != []:
                cur.execute(f'''UPDATE orders
                                SET courier = '{courier_idx}'
                                WHERE customer_name = '{order_to_update}' ''')
                con.commit()
    if order_to_update not in order.values() and order_to_update != '0' and res == False:
        system('cls')
        print(f'{order_to_update} not in list')
        time.sleep(2)
    system('cls')

    return orders

def delete_order(cur, con):
    system('cls')
    res = False
    cur.execute('SELECT * FROM orders')
    orders = cur.fetchall()
    for order in orders:
        print(f'Order: {order}')
    print()
    del_order = input('Enter name on order to delete or 0 to cancel: ').title()
    for order in orders:
        if del_order in order.values():
            system('cls')
            cur.execute(f'''DELETE FROM orders
                            WHERE customer_name = '{del_order}' ''')
            con.commit()
            print('Order has been deleted')
            time.sleep(2)
            res = True
    if del_order not in order.values() and del_order != '0' and res == False:
        system('cls')
        print(f'{del_order} not in list')
        time.sleep(2)
    
    system('cls')
    
    return orders
            
    