
'''functions for courier menu'''

from os import system 
import time

def replace_courier(couriers):
    system('cls')
    #replaces item in list
    replace_item = input('Enter the name of the courier you would like to replace or 0 to cancel: ').title()
    system('cls')
    if replace_item in couriers and replace_item != '0':
        new_item = input(f'Enter the name of the courier you would like to replace {replace_item} with: ').title()
        system('cls')
        couriers[couriers.index(replace_item)] = new_item
        print(f'{replace_item} has been replaced with {new_item}.')
        time.sleep(2)
    elif replace_item not in couriers and replace_item != '0':
        print(f'{replace_item} not in list.')
        time.sleep(2)
    system('cls')
    return couriers

def delete_courier(couriers):
    #deletes courier from courier list
    print()
    system('cls')
    del_item = input('Enter the courier you would like to delete or 0 to cancel: ').title()
    system('cls')
    if del_item in couriers and del_item != '0':
        del couriers[couriers.index(del_item)]
        print(f'{del_item} has been deleted.')
    elif del_item not in couriers and del_item != '0':
        print(f'{del_item} not in list.')
    time.sleep(2)
    system('cls')
    return couriers

def add_new_courier(couriers):
    #adds new item to courier list
    print()
    system('cls')
    new_courier = input('Enter the name of the new courier: ').title()
    if new_courier not in couriers:
        couriers.append(new_courier)
        system('cls')
        print(f'{new_courier} has been added.')
    else:
        system('cls')
        print(f'{new_courier} already in list')
    #pause and show message
    time.sleep(2)
    system('cls')
    return couriers
