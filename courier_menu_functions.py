
'''functions for courier menu'''

from os import system 
import time

def replace_courier(couriers):
    system('cls')
    #replaces item in list
    replace_item = input('Enter the name of the courier you would like to replace or 0 to cancel: ').title()
    system('cls')
    name_in_list = False
    for courier in couriers:
        if replace_item in courier.values() and replace_item != '0':
            name = input('Enter new name of the courier or leave field blank to keep the same: ').title()
            system('cls')
            number = input('Enter new phone number of the courier or leave field blank to keep the same: ')
            if name != '':
                courier['Name'] = name
                system('cls')
                print('Name has been updated')
                time.sleep(2)
            if number != None:
                courier['Phone Number'] = number
                system('cls')
                print('Phone number has been updated')
                name_in_list = True
                time.sleep(2)
    else:
        if name_in_list == False and replace_item != '0':
            print(f'{replace_item} not in list.')
            time.sleep(2)
    system('cls')
    return couriers

def delete_courier(couriers):
    #deletes courier from courier listd
    print()
    system('cls')
    del_item = input('Enter the courier you would like to delete or 0 to cancel: ').title()
    system('cls')
    count = 0
    res = False
    for courier in couriers:
        if del_item in courier.values() and del_item != '0':
            del couriers[count]
            print(f'{del_item} has been deleted.')
            res = True
            time.sleep(2)
        count += 1
    if res == False and del_item != '0':
        print(f'{del_item} not in list.')
        time.sleep(2)
    system('cls')
    return couriers

def add_new_courier(couriers):
    #adds new item to courier list
    print()
    system('cls')
    new_courier = input('Enter the name of the new courier: ').title()
    res = False
    for courier in couriers:
        if new_courier in courier.values():
            system('cls')
            print(f'{new_courier} already in list')
            res = True
    if res == False:
        system('cls')
        phone = input('Enter the phone number of new courier: ')
        courier_dict = {
            'Name': new_courier,
            'Phone Number': phone
        }
        system('cls')
        couriers.append(courier_dict)
        print(f'{new_courier} has been added')
    #pause and show message
    time.sleep(2)
    system('cls')
    return couriers
