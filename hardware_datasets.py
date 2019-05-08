from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Hardware, Item

engine = create_engine('sqlite:///hardware.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

########
# 1. CPU
hardware1 = Hardware(hardware_name="CPU")
session.add(hardware1)
session.commit()

item1 = Item(name='AMD Ryzen Threadripper 1950X', description='AMD Ryzen threadripper series processor with 16 cores and 32 threads',
             price='$550', image_name='ryzen1950.jpg', hardware=hardware1)
session.add(item1)
session.commit()

# Second Item
item2 = Item(name='Intel i9 processor', description='9th Gen Intel Processor with turbo frequency of 5.0 Hz',
             price='$750', image_name='intelI9.jpg', hardware=hardware1)
session.add(item2)
session.commit()

################
# 2. Motherboard
hardware2 = Hardware(hardware_name="Motherboard")
session.add(hardware2)
session.commit()

item1 = Item(name='Aorus X399 Gaming Pro 7', description='AMD X399 Gaming motherboard with RGB Fusion, Digital LED strip support',
             price='$550', image_name='aorusx399.jpg', hardware=hardware2)
session.add(item1)
session.commit()

# Second item
item2 = Item(name='ASUS Rog Strix X399', description='ASUS ROG STRIX X399-E GAMING AMD Ryzen Threadripper TR4 DDR4 M.2 U.2',
             price='$450', image_name='asusrstrix.jpg', hardware=hardware2)
session.add(item2)
session.commit()

########
# 3. RAM
hardware3 = Hardware(hardware_name="RAM")
session.add(hardware3)
session.commit()

item1 = Item(name='Corsair Vengenance 16GB', description='2X 8GB Corsair Vengenance RAM sricks, 2333Hz',
             price='$250', image_name='corsairV16.jpg', hardware=hardware3)
session.add(item1)
session.commit()

# Second item
item2 = Item(name='G.SKILL TridentZ', description='G.SKILL TridentZ RGB Series 16GB (2 x 8GB) 288-Pin DDR4 SDRAM DDR4 3000',
             price='$109', image_name='tridentx16.jpg', hardware=hardware3)
session.add(item2)
session.commit()

########
# 4. GPU
hardware4 = Hardware(hardware_name="GPU")
session.add(hardware4)
session.commit()

item1 = Item(name='Nvidia RTX 2070', description='The powerful new GeForce RTX™ 2070 takes advantage of the cutting-edge NVIDIA Turing™ architecture to immerse you in incredible realism and performance in the latest games',
             price='$699', image_name='nvidiartx2070.jpg', hardware=hardware4)
session.add(item1)
session.commit()

# Second item
item2 = Item(name='NVidia GTX 1080 Ti', description='GeForce GTX 10 Series graphics cards are powered by Pascal to deliver up to 3X the performance of previous-generation graphics cards, plus breakthrough gaming technologies and VR experiences.',
             price='$599', image_name='nvidiagtx1080ti.jpeg', hardware=hardware4)
session.add(item2)
session.commit()

###################
# 5. Liquid coolers
hardware5 = Hardware(hardware_name="Liquid Coolers")
session.add(hardware5)
session.commit()

item1 = Item(name='NZXT Kraken X62', description='The all-new Kraken Series features the most advanced controls ever to be included in an all-in-one liquid cooler',
             price='$150', image_name='krakenx62.jpg', hardware=hardware5)
session.add(item1)
session.commit()

# Second item
item2 = Item(name='Corsair H115i', description='Corsair H115i 240mm radiator with liquid cooling',
             price='$120', image_name='corsairh115i.png', hardware=hardware5)
session.add(item2)
session.commit()

############
# 6. Storage
hardware6 = Hardware(hardware_name="Storage")
session.add(hardware6)
session.commit()

item1 = Item(name='Samsung 860 EVO 1TB', description='Samsung 860 EVO 1TB 2.5 Inch SATA III Internal SSD (MZ-76E1T0B/AM)',
             price='$90', image_name='samsung860evo.jpg', hardware=hardware6)
session.add(item1)
session.commit()

# Second item
item2 = Item(name='Seagate Barracuda', description='Seagate Barracuda, 4TB with SATA connection',
             price='$70', image_name='seagatebarracuda4tb.jpg', hardware=hardware6)
session.add(item2)
session.commit()

print("Added all items")
