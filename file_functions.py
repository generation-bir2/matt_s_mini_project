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
        # for product in products:
        #     product_file.write(f'{product}\n')
        fieldname = ['Name', 'Price']
        writer = csv.DictWriter(product_file, fieldnames=fieldname)
        writer.writeheader()
        writer.writerows(products)
            
            
def create_courier_list():
    couriers = []
    try:
        with open('courier_file.csv','r') as courier_file:
            for courier in courier_file:
                couriers.append(courier.rstrip())
    except FileNotFoundError:
        system('cls')
        print('No courier file exists')
        time.sleep(2)
    return couriers

def save_couriers(couriers):
    with open('courier_file.csv', 'w') as courier_file:
        for courier in couriers:
            courier_file.write(f'{courier}\n')
    
def create_order_list():
    orders = []
    try:
        with open('order_file.csv','r') as order_file:
            for order in order_file:
                orders.append(order.rstrip())
    except FileNotFoundError:
        system('cls')
        print('No order file exists')
        time.sleep(2)
    return orders

def save_orders(orders):
    with open('order_file.csv', 'w') as order_file:
        for order in orders:
            order_file.write(f'{order}\n')
