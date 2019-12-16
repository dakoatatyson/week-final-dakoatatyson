from db import session
from sqlalchemy.sql import exists
from tables import User

def verify_customer(email):
    return session.query(User.email).filter(exists().where(User.email==email)).count() > 0

