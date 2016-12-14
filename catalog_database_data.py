#category_database_data.py
#This file is responsible for preloading the category database with information

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base, User, Category, Item
engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

user1 = User(name = "Ariana Lopez", email = "arianalopez30@gmail.com")
session.add(user1)

user2 = User(name = "Alaina Lopez", email = "alainalopez@hotmail.com")
session.add(user2)

user3 = User(name = "Mike  Wayne", email = "mikewayne@hotmail.com")
session.add(user3)

user4 = User(name = "Thomas Nyguen", email = "thomasngyuen@hotmail.com")
session.add(user4)

category1 = Category(name = "WWE")
session.add(category1)

category2 = Category(name = "Ring of Honor")
session.add(category2)

category3 = Category(name = "TNA")
session.add(category3)

item1 = Item(name = "T-shirt", description="New day booty'Os shirt", user_id = 1, category_id = 2)
session.add(item1)

item2 = Item(name = "Tickets", description="ROH show on Tuesday", user_id = 4, category_id = 3)
session.add(item2)

session.commit()