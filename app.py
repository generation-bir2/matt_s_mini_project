'''main app'''
from file_functions import *
from menus import *

#create product list to pass through program
products = create_product_list()

#creates courier list to pass through the program
couriers = create_courier_list()

#creates order list to pass through the program
orders = create_order_list()

#run main menu passing courier data and product data
products, couriers, orders = main_menu(products, couriers, orders)

#saves products to txt file
save_products(products)

#saves couriers to txt file
save_couriers(couriers)

#saves orders to txt file
save_orders(orders)