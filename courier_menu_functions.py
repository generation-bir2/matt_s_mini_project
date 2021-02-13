
'''functions for courier menu'''

from os import system 
import time

def replace_courier(cur, con):
    system('cls')
    #replaces item in list
    replace_item = input('Enter the name of the courier you would like to replace or 0 to cancel: ').title()
    system('cls')
    name_in_list = False
    cur.execute('SELECT name, phone_number FROM couriers')
    couriers = cur.fetchall()
    for courier in couriers:
        if replace_item in courier.values() and replace_item != '0':
            name_in_list = True
            name = input('Enter new name of the courier or leave field blank to keep the same: ').title()
            system('cls')
            number = input('Enter new phone number of the courier or leave field blank to keep the same: ')
            if name != '':
                cur.execute(f'''UPDATE couriers
                                SET name = '{name}'
                                WHERE name = '{replace_item}' ''')
                con.commit()
                system('cls')
                print('Name has been updated')
                time.sleep(2)
            if number != '':
                cur.execute(f'''UPDATE couriers
                                SET phone_number = '{number}'
                                WHERE name = '{replace_item}' ''')
                con.commit()    
                system('cls')
                print('Phone number has been updated')
                name_in_list = True
                time.sleep(2)
    if name_in_list == False and replace_item != '0' and res == False:
        print(f'{replace_item} not in list.')
        time.sleep(2)
    system('cls')

def delete_courier(cur, con):
    #deletes courier from courier listd
    print()
    system('cls')
    del_item = input('Enter the courier you would like to delete or 0 to cancel: ').title()
    system('cls')
    cur.execute('SELECT name FROM couriers')
    couriers = cur.fetchall()
    res = False
    for courier in couriers:
        if del_item in courier.values() and del_item != '0':
            cur.execute(f'''DELETE FROM couriers
                            WHERE name = '{del_item}' ''')
            con.commit()
            print(f'{del_item} has been deleted.')
            res = True
            time.sleep(2)
    if res == False and del_item != '0':
        print(f'{del_item} not in list.')
        time.sleep(2)
    system('cls')

def add_new_courier(cur, con):
    #adds new item to courier list
    print()
    system('cls')
    new_courier = input('Enter the name of the new courier: ').title()
    res = False
    cur.execute('SELECT name FROM couriers')
    couriers = cur.fetchall()
    for courier in couriers:
        if new_courier in courier.values():
            system('cls')
            print(f'{new_courier} already in list')
            res = True
            break
    if res == False:
        system('cls')
        phone = input('Enter the phone number of new courier: ')
        cur.execute('''INSERT INTO couriers(name, phone_number)
                        VALUES(%s,%s)''',(new_courier, phone))
        con.commit()
        system('cls')
        print(f'{new_courier} has been added')
    #pause and show message
    time.sleep(2)
    system('cls')
