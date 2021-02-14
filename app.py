'''main app'''
from menus import *

import pymysql
import os
from dotenv import load_dotenv
# Load environment variables from .env file

load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")
# Establish a database connection
con = pymysql.connect(
    host = host,
    user = user,
    password = password,
    database = database
)

cur = con.cursor(pymysql.cursors.DictCursor)

cur.execute('''CREATE TABLE IF NOT EXISTS products (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(30) NOT NULL,
    price FLOAT NOT NULL,
    PRIMARY KEY(id)
    );''')

cur.execute('''CREATE TABLE IF NOT EXISTS couriers (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(30) NOT NULL,
    phone_number VARCHAR(30) NOT NULL,
    PRIMARY KEY(id)
    );''')

cur.execute('''CREATE TABLE IF NOT EXISTS orders (
    id INT NOT NULL AUTO_INCREMENT,
    customer_name VARCHAR(30) NOT NULL,
    customer_address VARCHAR(250) NOT NULL,
    customer_phone VARCHAR(30) NOT NULL,
    courier INT NOT NULL,
    status VARCHAR(50) NOT NULL,
    items  VARCHAR(50) NOT NULL,
    PRIMARY KEY(id)
    );''')

cur = main_menu(cur, con)