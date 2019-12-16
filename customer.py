import db
import security

def get_customer(email, name, phone):
    if(security.verify_customer(email)):
        return db.view_customer(email)
    else:
        db.add_customer(email, name, phone)
        return db.view_customer(email)
    
def new_order(email, customer_name, phone, package_id, order_name, description):
    customer = get_customer(email, customer_name, phone)
    db.add_order(customer, package_id, order_name, description)

def view_order(order_id):
    print(db.view_order(order_id))
    for feature in db.view_order(order_id).features:
        print(feature)

def view_all_orders(customer_id):
    orders = db.view_customer_orders(customer_id)
    for order in orders:
        print(order)

def request_order_cancelation(customer_id, order_id):
    db.add_request(customer_id, order_id, 'Cancel Order')

    
