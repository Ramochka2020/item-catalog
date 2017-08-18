from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime
from database_setup import *

engine = create_engine('sqlite:///catalog1.db')
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

# Delete Categories if exisitng.
session.query(Category).delete()
# Delete Items if exisitng.
session.query(Items).delete()
# Delete Users if exisitng.
session.query(User).delete()

# Create fake users
User1 = User(name="Rama Ibrahim",
              email="rama.ibrahim",
              picture='http://dummyimage.com/200x200.png/ff4444/ffffff')
session.add(User1)
session.commit()


# Create a food categories

Category1 = Category(name="American cuisine",
                      user_id=1)
session.add(Category1)
session.commit()


Category2 = Category(name="mexican cuisine",
                      user_id=1)
session.add(Category2)
session.commit

Category3 = Category(name="Chinese cuisine",
                      user_id=1)
session.add(Category3)
session.commit()

Category4 = Category(name="French cuisine",
                      user_id=1)
session.add(Category4)
session.commit()


Category5 = Category(name="Asian cuisine",
                      user_id=1)
session.add(Category5)
session.commit()

# Populate a category with items for testing

Item1 = Items(name="Dominos Pizza",
               date=datetime.datetime.now(),
               description="The international fast food pizza",
               picture="https://goo.gl/tf6ak3",
               category_id=1,
               user_id=1)
session.add(Item1)
session.commit()

Item2 = Items(name="Waffletown USA",
               date=datetime.datetime.now(),
               description="Waffletown is a family restaurant ",
               picture="https://goo.gl/6BiFj1",
               category_id=1,
               user_id=1)
session.add(Item2)
session.commit()

Item3 = Items(name="Burger King",
               date=datetime.datetime.now(),
               description="Every day, more than 11 million restaurants around the world",
               picture="https://goo.gl/TRPJ47",
               category_id=1,
               user_id=1)
session.add(Item3)
session.commit()

print "Your database has been populated!"