'''order menu functions'''
from os import system
import time 

#Create new order
def create_new_order(orders, products):
    system('cls')
    name = input('Please enter the name of the customer: ').title()
    system('cls')
    address = input('Please enter the address of the customer: ')
    system('cls')
    phone_number = input('Please enter the phone number of the customer: ')
    system('cls')
    #####################################################################
    items = []
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
            items.append(item)
    system('cls')
    #####################################################################
    order_dict= {
        'Name': name,
        'Address': address,
        'Phone Number': phone_number,
        'Status': 'Preparing',
        'items': items}
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
                        order['Status'] == 'Out for delivery'
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
def update_order(orders):
    res = False
    system('cls')
    for order in orders:
        print(f'Order: {order}')
    print()
    order_to_update = input('Enter the name of the order you would like to update or 0 to cancel: ').title()
    for order in orders:
        if order_to_update == order['Name']:
            menu = True
            while menu == True:
                system('cls')
                print('0)Change Name\n1)Change Address\n2)Change Phone Number')
                print()
                while True:
                    try:
                        user = int(input('Enter Option [0|1|2]: '))
                    except ValueError:
                        print('Please Enter [0|1|2].')
                    else:
                        break
                if user == 0:
                    system('cls')               
                    new_name = input('Enter the new name: ').title()
                    system('cls')
                    order['Name'] = new_name
                    print('Name has been updated')
                    time.sleep(2)
                    res = True
                    break
                elif user == 1:
                    system('cls')
                    new_address = input('Enter the new address: ')
                    order['Address'] = new_address
                    system('cls')
                    print('Address has been updated')
                    time.sleep(2)
                    res = True
                    break
                elif user == 2:
                    system('cls')
                    new_number = input('Enter the new phone number: ')
                    order['Phone Number'] = new_number
                    system('cls')
                    print('Phone number has been updated')
                    time.sleep(2)
                    res = True
                    break
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
            
    