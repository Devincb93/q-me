from sqlalchemy_serializer import SerializerMixin
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship, validates
import bcrypt
from config import db
from datetime import datetime

class Employee(db.Model, SerializerMixin):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True)
    employee_login = Column(String, nullable=False)
    employee_password = Column(String, nullable=False)


    @validates('employee_login')
    def validate_employee_login(self, key, username):
        if len(username) < 0:
            raise ValueError("Must enter a employee login")
        else:
            return username
        
    @validates('employee_password')
    def validate_employee_password(self, key, password):
        if len(password) < 7:
            raise ValueError("Password didn't meet character criteria")
        else:
            return password
        
class Customer(db.Model, SerializerMixin):
    __tablename__='customers'

    id = Column(Integer, primary_key=True)
    first_last_name = Column(String, nullable=False)
    phone_number = Column(Integer, min=10, max=10)
    email = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)

    @validates('first_last_name')
    def validate_names(self, key, first_lase_name):
        if len(first_lase_name) < 0:
            raise ValueError("Must enter a name to add to queue")
        else:
            return first_lase_name
    @validates('phone_number')
    def validate_number(self, key, phone_number):
        if len(phone_number) < 10:
            raise ValueError("Must enter a valid phone number")
        else:
            return phone_number
        
class Notification(db.Model, SerializerMixin):
    __tablename__='notifications'

    id = Column(Integer, primary_key=True)
    message = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

