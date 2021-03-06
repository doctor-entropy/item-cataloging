import sys

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Hardware(Base):

    __tablename__ = 'hardware'

    hardware_name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)

class Item(Base):

    __tablename__ = 'item'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    price = Column(String(8))
    hardware_id = Column(Integer, ForeignKey('hardware.id'))
    image_name = Column(String(250))
    hardware = relationship(Hardware)

# class Images(Base):

#     __tablename__ = 'image_paths'

#     path = Column(String(250), nullable=False)
#     id = Column(Integer, primary_key=True)
#     item_id = Column(Integer, ForeignKey('item.id'))
#     item = relationship(Item)

engine = create_engine('sqlite:///hardware.db')

Base.metadata.create_all(engine)
