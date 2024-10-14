# coding: utf-8
from sqlalchemy import DECIMAL, DateTime  # API Logic Server GenAI assist
from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

########################################################################################################################
# Classes describing database for SqlAlchemy ORM, initially created by schema introspection.
#
# Alter this file per your database maintenance policy
#    See https://apilogicserver.github.io/Docs/Project-Rebuild/#rebuilding
#
# Created:  October 14, 2024 15:58:25
# Database: sqlite:////tmp/tmp.sSslbCzzCi/restaurant/database/db.sqlite
# Dialect:  sqlite
#
# mypy: ignore-errors
########################################################################################################################
 
from database.system.SAFRSBaseX import SAFRSBaseX
from flask_login import UserMixin
import safrs, flask_sqlalchemy
from safrs import jsonapi_attr
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.sql.sqltypes import NullType
from typing import List

db = SQLAlchemy() 
Base = declarative_base()  # type: flask_sqlalchemy.model.DefaultMeta
metadata = Base.metadata

#NullType = db.String  # datatype fixup
#TIMESTAMP= db.TIMESTAMP

from sqlalchemy.dialects.sqlite import *



class Customer(SAFRSBaseX, Base):
    """
    description: Customer details including name and contact information.
    """
    __tablename__ = 'customers'
    _s_collection_name = 'Customer'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)

    # parent relationships (access parent)

    # child relationships (access children)
    OrderList : Mapped[List["Order"]] = relationship(back_populates="customer")
    ReservationList : Mapped[List["Reservation"]] = relationship(back_populates="customer")
    ReviewList : Mapped[List["Review"]] = relationship(back_populates="customer")
    BillList : Mapped[List["Bill"]] = relationship(back_populates="customer")



class Ingredient(SAFRSBaseX, Base):
    """
    description: Stores information about ingredients used in menus.
    """
    __tablename__ = 'ingredients'
    _s_collection_name = 'Ingredient'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    quantity_in_stock = Column(Float, nullable=False)

    # parent relationships (access parent)

    # child relationships (access children)
    InventoryList : Mapped[List["Inventory"]] = relationship(back_populates="ingredient")
    SupplyOrderList : Mapped[List["SupplyOrder"]] = relationship(back_populates="ingredient")



class Restaurant(SAFRSBaseX, Base):
    """
    description: Stores restaurant information, including name and location.
    """
    __tablename__ = 'restaurants'
    _s_collection_name = 'Restaurant'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)

    # parent relationships (access parent)

    # child relationships (access children)
    ChefList : Mapped[List["Chef"]] = relationship(back_populates="restaurant")
    InventoryList : Mapped[List["Inventory"]] = relationship(back_populates="restaurant")
    MenuList : Mapped[List["Menu"]] = relationship(back_populates="restaurant")
    ReservationList : Mapped[List["Reservation"]] = relationship(back_populates="restaurant")
    RestaurantTableList : Mapped[List["RestaurantTable"]] = relationship(back_populates="restaurant")
    ReviewList : Mapped[List["Review"]] = relationship(back_populates="restaurant")



class Chef(SAFRSBaseX, Base):
    """
    description: Information about chefs, including name and restaurant ID.
    """
    __tablename__ = 'chefs'
    _s_collection_name = 'Chef'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    restaurant_id = Column(ForeignKey('restaurants.id'), nullable=False)

    # parent relationships (access parent)
    restaurant : Mapped["Restaurant"] = relationship(back_populates=("ChefList"))

    # child relationships (access children)



class Inventory(SAFRSBaseX, Base):
    """
    description: Maintains inventory records including restaurant ID and ingredient ID.
    """
    __tablename__ = 'inventory'
    _s_collection_name = 'Inventory'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    restaurant_id = Column(ForeignKey('restaurants.id'), nullable=False)
    ingredient_id = Column(ForeignKey('ingredients.id'), nullable=False)
    quantity = Column(Float, nullable=False)

    # parent relationships (access parent)
    ingredient : Mapped["Ingredient"] = relationship(back_populates=("InventoryList"))
    restaurant : Mapped["Restaurant"] = relationship(back_populates=("InventoryList"))

    # child relationships (access children)



class Menu(SAFRSBaseX, Base):
    """
    description: Stores menu information, including restaurant ID and item details.
    """
    __tablename__ = 'menus'
    _s_collection_name = 'Menu'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    restaurant_id = Column(ForeignKey('restaurants.id'), nullable=False)
    item_name = Column(String, nullable=False)
    price = Column(Float, nullable=False)

    # parent relationships (access parent)
    restaurant : Mapped["Restaurant"] = relationship(back_populates=("MenuList"))

    # child relationships (access children)



class Order(SAFRSBaseX, Base):
    """
    description: Stores orders placed by customers, including order date and status.
    """
    __tablename__ = 'orders'
    _s_collection_name = 'Order'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    customer_id = Column(ForeignKey('customers.id'), nullable=False)
    order_date = Column(DateTime, nullable=False)
    status = Column(String, nullable=False)

    # parent relationships (access parent)
    customer : Mapped["Customer"] = relationship(back_populates=("OrderList"))

    # child relationships (access children)
    BillList : Mapped[List["Bill"]] = relationship(back_populates="order")



class Reservation(SAFRSBaseX, Base):
    """
    description: Stores reservation details, including customer ID and restaurant ID.
    """
    __tablename__ = 'reservations'
    _s_collection_name = 'Reservation'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    customer_id = Column(ForeignKey('customers.id'), nullable=False)
    restaurant_id = Column(ForeignKey('restaurants.id'), nullable=False)
    reservation_date = Column(DateTime, nullable=False)

    # parent relationships (access parent)
    customer : Mapped["Customer"] = relationship(back_populates=("ReservationList"))
    restaurant : Mapped["Restaurant"] = relationship(back_populates=("ReservationList"))

    # child relationships (access children)



class RestaurantTable(SAFRSBaseX, Base):
    """
    description: Information about tables in the restaurant.
    """
    __tablename__ = 'restaurant_tables'
    _s_collection_name = 'RestaurantTable'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    restaurant_id = Column(ForeignKey('restaurants.id'), nullable=False)
    capacity = Column(Integer, nullable=False)

    # parent relationships (access parent)
    restaurant : Mapped["Restaurant"] = relationship(back_populates=("RestaurantTableList"))

    # child relationships (access children)



class Review(SAFRSBaseX, Base):
    """
    description: Stores reviews given by customers for restaurants.
    """
    __tablename__ = 'reviews'
    _s_collection_name = 'Review'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    customer_id = Column(ForeignKey('customers.id'), nullable=False)
    restaurant_id = Column(ForeignKey('restaurants.id'), nullable=False)
    rating = Column(Integer, nullable=False)
    comment = Column(Text)

    # parent relationships (access parent)
    customer : Mapped["Customer"] = relationship(back_populates=("ReviewList"))
    restaurant : Mapped["Restaurant"] = relationship(back_populates=("ReviewList"))

    # child relationships (access children)



class SupplyOrder(SAFRSBaseX, Base):
    """
    description: Details of supply orders made for ingredients.
    """
    __tablename__ = 'supply_orders'
    _s_collection_name = 'SupplyOrder'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    ingredient_id = Column(ForeignKey('ingredients.id'), nullable=False)
    order_date = Column(DateTime, nullable=False)
    quantity = Column(Float, nullable=False)

    # parent relationships (access parent)
    ingredient : Mapped["Ingredient"] = relationship(back_populates=("SupplyOrderList"))

    # child relationships (access children)



class Bill(SAFRSBaseX, Base):
    """
    description: Stores billing information, including customer ID and total amount.
    """
    __tablename__ = 'bills'
    _s_collection_name = 'Bill'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    customer_id = Column(ForeignKey('customers.id'), nullable=False)
    order_id = Column(ForeignKey('orders.id'), nullable=False)
    total_amount = Column(Float, nullable=False)

    # parent relationships (access parent)
    customer : Mapped["Customer"] = relationship(back_populates=("BillList"))
    order : Mapped["Order"] = relationship(back_populates=("BillList"))

    # child relationships (access children)
