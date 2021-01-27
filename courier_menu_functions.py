
'''functions for courier menu'''

from os import system 
import time

def replace_courier(couriers):
    system('cls')
    #replaces item in list
    replace_item = input('Enter the name of the courier you would like to replace or 0 to cancel: ').title()
    system('cls')
    if replace_item in couriers and not '0':
        new_item = input('Enter the name of the courier you would like to replace them with: ').title()
        system('cls')
        couriers[couriers.index(replace_item)] = new_item
        print('Courier has been replaced.')
        time.sleep(2)
    elif replace_item not in couriers and not '0':
        print('Courier not in list.')
        time.sleep(2)
    system('cls')
    return couriers

def delete_courier(couriers):
    #deletes courier from courier list
    print()
    system('cls')
    del_item = input('Enter the courier you would like to delete or 0 to cancel: ').title()
    system('cls')
    if del_item in couriers and not '0':
        del couriers[couriers.index(del_item)]
        print('Courier has been deleted.')
    elif del_item not in couriers and not '0':
        print('Courier not in list.')
    time.sleep(2)
    system('cls')
    return couriers

def add_new_courier(couriers):
    #adds new item to courier list
    print()
    system('cls')
    new_courier = input('Enter the name of the new courier: ').title()
    couriers.append(new_courier)
    system('cls')
    print('Your courier has been added.')
    #pause and show message
    time.sleep(2)
    system('cls')
    return couriers
