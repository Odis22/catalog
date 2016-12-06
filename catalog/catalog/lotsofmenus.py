from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Store, Base, CatalogItem, User

engine = create_engine('sqlite:///storeCatalogwithusers.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy user
User1 = User(name="Robo Barista", email="tinnyTim@udacity.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()

# Catalog for WWE
store1 = store(user_id=1, name="WWE")

session.add(store1)
session.commit()

catalogItem2 = CatalogItem(user_id=1, name="John Cena t-shirt hustle, loyalty, respect", description="black t-shirt",
                     price="$25.50", item="T-shirt", store=store1)

session.add(catalogItem2)
session.commit()


catalogItem1 = CatalogItem(user_id=1, name="Wrestlemania 32", description="The grandest stage of them all in Dallas",
                     price="$30.99", item="DVDS",store=store1)

session.add(catalogItem1)
session.commit()

catalogItem2 = CatalogItem(user_id=1, name="Summerslam 2016", description="Brock Lesnar vs Randy Orton",
                     price="$5.50", item="DVDS", store=store1)

session.add(catalogItem2)
session.commit()

catalogItem3 = CatalogItem(user_id=1, name="WWE 2k17", description="for PS4 and Xbox one",
                     price="$3.99", item="videogames", store=store1)

session.add(catalogItem3)
session.commit()

catalogItem4 = CatalogItem(user_id=1, name="Royal Rumble", description="who will go to the main event of wrestlemania",
                     price="$7.99", item="DVDS", store=store1)

session.add(CatalogItem4)
session.commit()

catalogItem5 = CatalogItem(user_id=1, name="Monday night Raw live", description="March 15 at united center in chicago illinois at 7:00pm",
                     price="$1.99", item="Tickets", store=store1)

session.add(CatalogItem5)
session.commit()

catalogItem6 = CatalogItem(user_id=1, name="WWE smackdown", description="March 16 at all state center in chicago illinois at 7:00pm"",
                     price="$.99", item="Tickets", store=store1)

session.add(CatalogItem6)
session.commit()

catalogItem7 = CatalogItem(user_id=1, name="The Best of NXT",
                     description="Best NXT matches", price="$3.49", item="DVDS", store=store1)

session.add(CatalogItem7)
session.commit()

catalogItem8 = CatalogItem(user_id=1, name="NXT Takeover:Respect", description="Becky Lynch vs Bayley",
                     price="$5.99", course="DVDS", store=store1)

session.add(CatalogItem8)
session.commit()


# Catalog for TNA
store2 = store(user_id=1, name="WWE")

session.add(store1)
session.commit()

catalogItem2 = CatalogItem(user_id=1, name="John Cena t-shirt hustle, loyalty, respect", description="black t-shirt",
                     price="$25.50", item="T-shirt", store=store1)

session.add(catalogItem2)
session.commit()


catalogItem1 = CatalogItem(user_id=1, name="Best of TNA", description="Best matches",
                     price="$30.99", item="DVDS",store=store1)

session.add(catalogItem1)
session.commit()

catalogItem2 = CatalogItem(user_id=1, name="Slamiversary 2016", description="Brock Lesnar vs Randy Orton",
                     price="$5.50", item="DVDS", store=store1)

session.add(catalogItem2)
session.commit()

catalogItem3 = CatalogItem(user_id=1, name="TNA 2k17", description="for PS4 and Xbox one",
                     price="$3.99", item="videogames", store=store1)

session.add(catalogItem3)
session.commit()

catalogItem4 = CatalogItem(user_id=1, name="Final Deletion", description="Matt hardy vs Jeff Hardy",
                     price="$7.99", item="DVDS", store=store1)

session.add(CatalogItem4)
session.commit()

catalogItem5 = CatalogItem(user_id=1, name="TNA impact", description="tickets to the live events",
                     price="$1.99", item="Tickets", store=store1)

session.add(CatalogItem5)
session.commit()



# Catalog for Ring of Honor
sstore3 = store(user_id=3, name="ROH")

session.add(store1)
session.commit()

catalogItem2 = CatalogItem(user_id=3, name="Moose Ojinaka shirt", description="black t-shirt",
                     price="$25.50", item="T-shirt", store=store1)

session.add(catalogItem2)
session.commit()


catalogItem1 = CatalogItem(user_id=3, name="death before dishoner", description="Will Ospreay vs billy king for ROH championship",
                     price="$30.99", item="DVDS",store=store1)

session.add(catalogItem1)
session.commit()



catalogItem5 = CatalogItem(user_id=3, name="ROH live events", description="tickets to live shows and payperviews.",
                     price="$1.99", item="Tickets", store=store1)

session.add(CatalogItem5)
session.commit()







