from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from tables import Base, User, Employee, Customer, Feature, Package, Stage, Order

engine = create_engine('sqlite:///:memory:', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)

def add_employee(email):
    user = User(email=email)
    session.add(user)
    session.commit()
    session.add(Employee(user_id=user.id))
    session.commit()

def add_customer(email, name, phone):
    user = User(email=email)
    session.add(user)
    session.commit()
    session.add(Customer(user_id=user.id, name=name, phone=phone))
    session.commit()

def add_package(features_num, price):
    session.add(Package(features=features_num, price=price))
    session.commit()

def add_stage(name):
    session.add(Stage(name=name))
    session.commit()

def add_order(customer_id, package_id, name, description):
    session.add(Order(customer_id=customer_id, package_id=package_id, name=name, description=description))
    session.commit()

def add_feature(order_id, name, description):
    session.add(Feature(order_id=order_id, name=name, description=description))
    session.commit()

def view_customer(email):
    for customer in session.query(Customer).filter(User.id==Customer.user_id).filter(User.email==email):
        return customer.id

def view_order(order_id):
    for order in session.query(Order).filter(Order.id==order_id):
        return order

def view_all_orders(customer_id):
    orders = []

    for order in session.query(Order).filter(Order.customer_id==customer_id):
        orders.append(order)

    return orders

add_employee('dakoatatyson@gmail.com')

add_customer("jonedoe@gmail.com", 'Doe Incorporated', "1-***-***-****")

add_package(1,250.00)
add_package(3,500.00)
add_package(5,1000.00)

add_stage("DESIGN")
add_stage("PAYMENT")
add_stage("PROCCESSING")
add_stage("PAID")
add_stage("DEVELOP")
add_stage("COMPLETE")
add_stage("CANCELED")

add_order(1, 2, 'Project 1', 'Web App were users can make orders for a butcher shop')

add_feature(1, 'Order System', 'A feature where the customers can plcae there order and keep track of them. ')
add_feature(1, 'Live Chat', 'A live chatting box hwere users can talk to employees in real time.')
add_feature(1, 'Log In', 'A feature where customers can log in to view all their purchases and save payemnt information securly.')

#for user in session.query(User).order_by(User.id):
#    print(user)

#for customer in session.query(Customer).order_by(Customer.id):
#    print(customer)

#for order in session.query(Order).order_by(Order.id):
#    print(order)
#    for feature in session.query(Feature).filter(Feature.order == order).order_by(Feature.id):
#        print(feature)


