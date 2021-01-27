'''file functions'''
import time
from os import system

def create_product_list():
    products = []
    try:
        with open('product_file.txt','r') as product_file:
            for product in product_file:
                products.append(product.rstrip())
        product_file.close()
    except FileNotFoundError:
        system('cls')
        print('No product file exists')
        time.sleep(2)
    return products

def save_products(products):
    with open('product_file.txt', 'w') as product_file:
        for product in products:
            product_file.write(f'{product}\n')
    product_file.close()
    
def create_courier_list():
    couriers = []
    try:
        with open('courier_file.txt','r') as courier_file:
            for courier in courier_file:
                couriers.append(courier.rstrip())
        courier_file.close()
    except FileNotFoundError:
        system('cls')
        print('No courier file exists')
        time.sleep(2)
    return couriers

def save_couriers(couriers):
    with open('courier_file.txt', 'w') as courier_file:
        for courier in couriers:
            courier_file.write(f'{courier}\n')
    courier_file.close()