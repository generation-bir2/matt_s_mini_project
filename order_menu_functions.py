'''order menu functions'''
from os import system
import time 

#Create new order
def create_new_order(orders):
    order_dict = {}
    system('cls')
    name = input('Please enter the name of the customer: ').title()
    system('cls')
    address = input('Please enter the address of the customer: ')
    system('cls')
    phone_number = input('Please enter the phone number of the customer: ')
    system('cls')
    order_dict[name] = {
        'Address': address,
        'Phone Number': phone_number,
        'Status': 'Preparing'}
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
        if order_name in order.keys():
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
        elif order_name not in order.keys() and order_name != '0':
            system('cls')
            print('Name not in list')
            time.sleep(2)
    system('cls')
    return orders
            
#updates order
def update_order(orders):
    system('cls')
    for order in orders:
        print(f'Order: {order}')
    print()
    order_to_update = input('Enter the name of the order you would like to update or 0 to cancel: ').title()
    for order in orders:
        if order_to_update in order.keys():
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
                    order[new_name] = order.pop(order_to_update)
                    print('Name has been updated')
                    time.sleep(2)
                    break
                elif user == 1:
                    system('cls')
                    new_address = input('Enter the new address: ')
                    order[order_to_update]['Address'] = new_address
                    system('cls')
                    print('Address has been updated')
                    time.sleep(2)
                    break
                elif user == 2:
                    system('cls')
                    new_number = input('Enter the new phone number: ')
                    order[order_to_update]['Phone Number'] = new_number
                    system('cls')
                    print('Phone number has been updated')
                    time.sleep(2)
                    break
        elif order_to_update not in order.keys() and order_to_update != '0':
            system('cls')
            print('Name not in list')
            time.sleep(2)
    system('cls')
    return orders

def delete_order(orders):
    system('cls')
    for order in orders:
        print(f'Order: {order}')
    print()
    del_order = input('Enter name on order to delete or 0 to cancel: ').title()
    for order in orders:
        if del_order in order.keys():
            system('cls')
            del order[del_order]
            print('Order has been deleted')
            time.sleep(2)
        elif del_order not in order.keys() and del_order != '0':
            system('cls')
            print('Order not in list')
            time.sleep(2)
    system('cls')
    return orders
            
    