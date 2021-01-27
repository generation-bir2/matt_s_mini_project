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
            