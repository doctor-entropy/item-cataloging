from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Hardware, Item, Images

engine = create_engine('sqlite:///hardware.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

hardware1 = Hardware(name="CPU")
session.add(hardware1)
session.commit()

item1 = Item(name='AMD Ryzen Threadripper 1950X', description='AMD Ryzen threadripper series processor with 16 cores and 32 threads',
			 price='$550', hardware=hardware1)
session.add(item1)
session.commit()

item1_imgp = Images(path='images/ryzen1950.jpg', item=item1)
session.add(item1_imgp)
session.commit()
