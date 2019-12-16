import db

def cancel_order(order_id):
    db.cancel_order(order_id)

def view_orders():
    orders = db.view_all_orders()
    for order in orders:
        print(order)
    