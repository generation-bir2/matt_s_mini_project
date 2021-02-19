from os import system
import time
from tabulate import tabulate

def add_customer(cur,con):
    system('cls')
    name = input('Enter the name of the new customer: ').title()
    system('cls')
    address = input('Enter the customers address: ')
    system('cls')
    number = input('Enter the customers phone number:  ')
    system('cls')
    cur.execute('''INSERT INTO customers(customer_name, customer_address, customer_phone)
                    VALUES(%s, %s, %s)''', (name, address, number))
    con.commit()
    print('The customer has been added')
    time.sleep(2)
    system('cls')
    
    
def update_customer(cur, con):
    res = False
    system('cls')
    cur.execute('SELECT * FROM customers')
    customers = cur.fetchall()
    print(tabulate(customers, headers = 'keys' ))
    print()
    id = int(input('Enter the id of the order you would like to update or 0 to cancel: '))
    for customer in customers:
        if id == customer['customer_id']:
            system('cls')
            name = input('Please enter the name of the customer or leave blank to skip: ').title()
            system('cls')
            address = input('Please enter the address of the customer or leave blank to skip: ')
            system('cls')
            phone_number = input('Please enter the phone number of the customer or leave blank to skip: ')
            system('cls')
            if name != '':
                cur.execute(f'''UPDATE customers
                                SET customer_name = '{name}'
                                WHERE customer_id = '{id}' ''')
                con.commit()
                res = True
            if address != '':
                cur.execute(f'''UPDATE customers
                                SET customer_address = '{address}'
                                WHERE customer_id = '{id}' ''')
                con.commit()
                res = True
            if phone_number != '':
                cur.execute(f'''UPDATE customers
                                SET customer_phone = '{phone_number}'
                                WHERE customer_id = '{id}' ''')
                con.commit()
                res = True
    if id != 0 and res == False:
        system('cls')
        print(f'ID {id} not in list')
        time.sleep(2)
    system('cls')
    

def delete_customer(cur, con):
    system('cls')
    res = False
    cur.execute('SELECT * FROM customers')
    customers = cur.fetchall()
    print(tabulate(customers, headers = 'keys' ))
    print()
    del_customer = int(input('Enter id of customer to delete or 0 to cancel: '))
    for customer in customers:
        if del_customer in customer.values():
            system('cls')
            cur.execute(f'''DELETE FROM customers
                            WHERE customer_id = '{del_customer}' ''')
            con.commit()
            print('Customer has been deleted')
            time.sleep(2)
            res = True
    if del_customer != 0 and res == False:
        system('cls')
        print(f'{del_customer} not in list')
        time.sleep(2)
    
    system('cls')