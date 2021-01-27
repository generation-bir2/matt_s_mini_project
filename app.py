'''main app'''
from file_functions import *
from menus import *

#create product list to pass through program
products = create_product_list()

#creates courier list to pass through the program
couriers = create_courier_list()

#run main menu passing courier data and product data
products, couriers = main_menu(products, couriers)

#saves products to txt file
save_products(products)

#saves couriers to txt file
save_couriers(couriers)
