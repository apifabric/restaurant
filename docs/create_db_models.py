import decimal

import logging



logging.getLogger('sqlalchemy.engine.Engine').disabled = True  # remove for additional logging

import sqlalchemy



from sqlalchemy.sql import func  # end imports from system/genai/create_db_models_inserts/create_db_models_prefix.py

from logic_bank.logic_bank import Rule

from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ForeignKey, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

# Define the base class
Base = declarative_base()

# Define the Restaurant class
class Restaurant(Base):
    """
    description: Stores restaurant information, including name and location.
    """
    __tablename__ = 'restaurants'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)

# Define the Menu class
class Menu(Base):
    """
    description: Stores menu information, including restaurant ID and item details.
    """
    __tablename__ = 'menus'
    id = Column(Integer, primary_key=True, autoincrement=True)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'), nullable=False)
    item_name = Column(String, nullable=False)
    price = Column(Float, nullable=False)

# Define the Chef class
class Chef(Base):
    """
    description: Information about chefs, including name and restaurant ID.
    """
    __tablename__ = 'chefs'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'), nullable=False)

# Define the Customer class
class Customer(Base):
    """
    description: Customer details including name and contact information.
    """
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

# Define the Reservation class
class Reservation(Base):
    """
    description: Stores reservation details, including customer ID and restaurant ID.
    """
    __tablename__ = 'reservations'
    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'), nullable=False)
    reservation_date = Column(DateTime, nullable=False)

# Define the Review class
class Review(Base):
    """
    description: Stores reviews given by customers for restaurants.
    """
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'), nullable=False)
    rating = Column(Integer, nullable=False)
    comment = Column(Text)

# Define the Ingredient class
class Ingredient(Base):
    """
    description: Stores information about ingredients used in menus.
    """
    __tablename__ = 'ingredients'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    quantity_in_stock = Column(Float, nullable=False)

# Define the SupplyOrder class
class SupplyOrder(Base):
    """
    description: Details of supply orders made for ingredients.
    """
    __tablename__ = 'supply_orders'
    id = Column(Integer, primary_key=True, autoincrement=True)
    ingredient_id = Column(Integer, ForeignKey('ingredients.id'), nullable=False)
    order_date = Column(DateTime, nullable=False)
    quantity = Column(Float, nullable=False)

# Define the Table class
class Table(Base):
    """
    description: Information about tables in the restaurant.
    """
    __tablename__ = 'restaurant_tables'
    id = Column(Integer, primary_key=True, autoincrement=True)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'), nullable=False)
    capacity = Column(Integer, nullable=False)

# Define the Order class
class Order(Base):
    """
    description: Stores orders placed by customers, including order date and status.
    """
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    order_date = Column(DateTime, nullable=False)
    status = Column(String, nullable=False)

# Define the Inventory class
class Inventory(Base):
    """
    description: Maintains inventory records including restaurant ID and ingredient ID.
    """
    __tablename__ = 'inventory'
    id = Column(Integer, primary_key=True, autoincrement=True)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'), nullable=False)
    ingredient_id = Column(Integer, ForeignKey('ingredients.id'), nullable=False)
    quantity = Column(Float, nullable=False)

# Define the Bill class
class Bill(Base):
    """
    description: Stores billing information, including customer ID and total amount.
    """
    __tablename__ = 'bills'
    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    total_amount = Column(Float, nullable=False)

# Create a new SQLite database (or connect to an existing one)
engine = create_engine('sqlite:///system/genai/temp/create_db_models.sqlite')
Base.metadata.create_all(engine)

# Create a sessionmaker
Session = sessionmaker(bind=engine)
session = Session()

# Add sample data
restaurants = [
    Restaurant(name="Gourmet Kitchen", location="Downtown"),
    Restaurant(name="Bistro Bliss", location="Uptown")
]

customers = [
    Customer(name="John Doe", email="john.doe@email.com"),
    Customer(name="Jane Smith", email="jane.smith@email.com")
]

menus = [
    Menu(restaurant_id=1, item_name="Mushroom Risotto", price=12.50),
    Menu(restaurant_id=2, item_name="Grilled Cheese Sandwich", price=8.00)
]

chefs = [
    Chef(name="Gordon Ramsay", restaurant_id=1),
    Chef(name="Jamie Oliver", restaurant_id=2)
]

reservations = [
    Reservation(customer_id=1, restaurant_id=1, reservation_date=datetime.datetime.now()),
    Reservation(customer_id=2, restaurant_id=2, reservation_date=datetime.datetime.now())
]

reviews = [
    Review(customer_id=1, restaurant_id=1, rating=5, comment="Excellent food and service."),
    Review(customer_id=2, restaurant_id=2, rating=4, comment="Great ambiance but food was a bit cold.")
]

ingredients = [
    Ingredient(name="Tomato", quantity_in_stock=200.0),
    Ingredient(name="Cheddar Cheese", quantity_in_stock=150.0)
]

supply_orders = [
    SupplyOrder(ingredient_id=1, order_date=datetime.datetime.now(), quantity=50.0),
    SupplyOrder(ingredient_id=2, order_date=datetime.datetime.now(), quantity=30.0)
]

restaurant_tables = [
    Table(restaurant_id=1, capacity=4),
    Table(restaurant_id=2, capacity=2)
]

orders = [
    Order(customer_id=1, order_date=datetime.datetime.now(), status="Completed"),
    Order(customer_id=2, order_date=datetime.datetime.now(), status="Pending")
]

inventory = [
    Inventory(restaurant_id=1, ingredient_id=1, quantity=50.0),
    Inventory(restaurant_id=2, ingredient_id=2, quantity=30.0)
]

bills = [
    Bill(customer_id=1, order_id=1, total_amount=25.00),
    Bill(customer_id=2, order_id=2, total_amount=15.00)
]

# Add all entries to the session
session.add_all(restaurants + customers + menus + chefs + reservations + reviews +
                ingredients + supply_orders + restaurant_tables + orders + inventory + bills)

# Commit the transaction
session.commit()

# Close the session
session.close()

print("Database and sample data created successfully!")
