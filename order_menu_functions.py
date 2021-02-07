'''order menu functions'''
from os import system
import time 

#Create new order
def create_new_order(orders, products, couriers):
    system('cls')
    name = input('Please enter the name of the customer: ').title()
    system('cls')
    address = input('Please enter the address of the customer: ')
    system('cls')
    phone_number = input('Please enter the phone number of the customer: ')
    system('cls')
    product_idx = []
    item = 1
    while item != 0:
        for count, product in enumerate(products, start= 1):
            print(f'{count}: {product["Name"]}')
        while True:
            try:
                item = int(input('Enter the index of the product you want to order, or 0 to continue: '))
            except ValueError:
                print('Please select a number')
            else:
                break
        system('cls')
        if item != 0:
            product_idx.append(item)
    courier_idx = []
    for count, courier in enumerate(couriers, start= 1):
        print(f'{count}: {courier["Name"]}')
    while True:
        try:
            item = int(input('Enter the index of the courier you want to add to the order: '))
        except ValueError:
            print('Please select a number')
        else:
            break
    courier_idx.append(item)    
    system('cls')
    order_dict= {
        'Name': name,
        'Address': address,
        'Phone Number': phone_number,
        'Status': 'Preparing',
        'Items': product_idx,
        'Courier': courier_idx
        }
    orders.append(order_dict)
    print('Your order has been added')
    time.sleep(2)
    system('cls')
    
    return orders

#update order status
def update_order_status(orders):
    system('cls')
    for order in orders:
        print(f'Order: {order}')
    print()
    order_name = input('Enter the name of the person who\'s order you would like to update or 0 to cancel: ').title()
    for order in orders:
        if order_name in order.values():
            menu = True
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
                        order['Status'] = 'Out for delivery'
                        system('cls')
                        print('Status updated')
                        time.sleep(2)
                        menu = False
                elif user == 1:
                        order['Status'] = 'Delivered'
                        system('cls')
                        print('Status updated')
                        time.sleep(2)
                        menu = False
    if order_name not in order.values() and order_name != '0':
        system('cls')
        print(f'{order_name} not in list')
        time.sleep(2)
    system('cls')
    
    return orders
            
            
            
#updates order
def update_order(orders, products,couriers):
    res = False
    system('cls')
    for order in orders:
        print(f'Order: {order}')
        print()
    order_to_update = input('Enter the name of the order you would like to update or 0 to cancel: ').title()
    for order in orders:
        if order_to_update == order['Name']:
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
                for count, product in enumerate(products, start= 1):
                    print(f'{count}: {product["Name"]}')
                while True:
                    try:
                        item = int(input('Enter the index of the product you want to order, or 0 to continue: '))
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
            for count, courier in enumerate(couriers, start= 1):
                print(f'{count}: {courier["Name"]}')
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
                order['Name'] = name
            if address != '':
                order['Address'] = address
            if phone_number != '':
                order['Phone Number'] = phone_number
            if product_idx != []:
                order['Items'] = product_idx
            if courier_idx != []:
                order['Courier'] = courier_idx
    if order_to_update not in order.values() and order_to_update != '0' and res == False:
        system('cls')
        print(f'{order_to_update} not in list')
        time.sleep(2)
    system('cls')

    return orders

def delete_order(orders):
    system('cls')
    res = False
    for order in orders:
        print(f'Order: {order}')
    print()
    del_order = input('Enter name on order to delete or 0 to cancel: ').title()
    for order in orders:
        if del_order in order.values():
            system('cls')
            del order
            print('Order has been deleted')
            time.sleep(2)
            res = True
    if del_order not in order.values() and del_order != '0' and res == False:
        system('cls')
        print(f'{del_order} not in list')
        time.sleep(2)
    
    system('cls')
    
    return orders
            
    