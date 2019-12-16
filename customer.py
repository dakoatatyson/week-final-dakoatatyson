import db
from db import Customer, Order
import security

current_customer_id = None

def reset_customer():
    current_customer_id = None

def set_customer(email, name, phone):
    global current_customer_id
    if(security.verify_customer(email)):
        current_customer_id = db.view_customer(email)
    else:
        db.add_customer(email, name, phone)
        current_customer_id = db.view_customer(email)

def create_order(package_id, name, description):
    db.add_order(current_customer_id, package_id, name, description)

def new_order(email, customer_name, phone, package_id, order_name, description):
    set_customer(email, customer_name, phone)
    create_order(package_id, order_name, description)
    reset_customer()

def view_order(order_id):
    print(db.view_order(order_id))
    print(db.view_order(order_id).features)

def view_all_orders(customer_id):
    orders = db.view_all_orders(customer_id)
    for order in orders:
        print(order)
