'''file functions'''
import time
from os import system
import csv

def create_product_list():
    products = []
    try:
        with open('product_file.csv','r') as product_file:
            csv_reader = csv.DictReader(product_file)
            for row in csv_reader:
                products.append(row)
    except FileNotFoundError:
        system('cls')
        print('No product file exists')
        time.sleep(2)
    return products

def save_products(products):
    with open('product_file.csv', 'w') as product_file:
        fieldname = ['Name', 'Price']
        writer = csv.DictWriter(product_file, fieldnames=fieldname)
        writer.writeheader()
        writer.writerows(products)
            
            
def create_courier_list():
    couriers = []
    try:
        with open('courier_file.csv','r') as courier_file:
            csv_reader = csv.DictReader(courier_file)
            for row in csv_reader:
                couriers.append(row)
    except FileNotFoundError:
        system('cls')
        print('No courier file exists')
        time.sleep(2)
    return couriers

def save_couriers(couriers):
    with open('courier_file.csv', 'w') as courier_file:
        fieldname = ['Name','Phone Number']
        writer = csv.DictWriter(courier_file, fieldnames=fieldname)
        writer.writeheader()
        writer.writerows(couriers)
    
def create_order_list():
    orders = []
    try:
        with open('order_file.csv','r') as order_file:
            csv_reader = csv.DictReader(order_file)
            for row in csv_reader:
                orders.append(row)
    except FileNotFoundError:
        system('cls')
        print('No order file exists')
        time.sleep(2)
    return orders

def save_orders(orders):
    with open('order_file.csv', 'w') as order_file:
        fieldname = [
            'Name',
            'Address',
            'Phone Number',
            'Status',
            'Items',
            'Courier'
        ]
        writer = csv.DictWriter(order_file, fieldnames=fieldname)
        writer.writeheader()
        writer.writerows(orders)
