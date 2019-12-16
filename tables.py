from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, Float
from sqlalchemy import Sequence
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

class Feature(Base):
    __tablename__ = 'features'
    id = Column(Integer, Sequence('order_id_seq'), primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.id'))
    name = Column(String(50))
    description = Column(Text)

    order = relationship("Order", back_populates="features")

    def __repr__(self):
        return "ID: %s NAME: %s\nDESCRIPTION: %s" % (self.id, self.name, self.description)

class Package(Base):
    __tablename__ = 'packages'
    id = Column(Integer, Sequence('order_id_seq'), primary_key=True)
    features = Column(Integer)
    price = Column(Float)

    def __repr__(self):
        return "ID: %s NUMBER OF FEATURES: %s PRICE: %s" % (self.id, self.features, self.price)

class Stage(Base):
    __tablename__ = 'stages'
    id = Column(Integer, Sequence('stage_id_seq'), primary_key=True)
    name = Column(String(20))

    def __repr__(self):
        return "ID: %s NAME: %s" % (self.id, self.name)

class User(Base): 
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    email = Column(String(50), unique=True)

    def __repr__(self):
        return "ID: %s EMAIL: %s" % (self.id, self.email)

class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, Sequence('employee_id_seq'), primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))

    def __repr__(self):
        return "ID: %s USER: %s" % (self.id, self.user_id)

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, Sequence('customer_id_seq'), primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    name = Column(String(50), unique=True)
    phone = Column(String(14), unique=True)

    def __repr__(self):
        return "ID: %s USER: %s Name: %s Phone: %s" % (self.id, self.user_id, self.name, self.phone)

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, Sequence('customer_id_seq'), primary_key=True)
    customer_id = Column(Integer, ForeignKey('stages.id'))
    stage_id = Column(Integer, ForeignKey('customers.id'), default=1)
    package_id = Column(Integer, ForeignKey('packages.id'))
    name = Column(String(50))
    description = Column(Text())
    features = relationship("Feature", order_by=Feature.id, back_populates="order")
    balance = Column(Float(), nullable=False, default=0.00)

    def __repr__(self):
        return "ID: %s Customer: %s Name: %s\nDescription: %s" % (self.id, self.customer_id, self.name, self.description)