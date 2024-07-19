import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False, unique=True)
    password = Column(String(15), nullable=False)
    firstname = Column(String(100), nullable=False)
    lastname = Column(String(100), nullable=False)
    email = Column(String(200), nullable=False, unique=True)

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False, unique=True)
    description = Column(String(1000))
    diameter = Column(Integer, nullable=False)
    gravity = Column(String(500), nullable=False)
    climate = Column(String(100), nullable=False)
    url = Column(String(1500), nullable=False, unique=True)
    people_id = Column(Integer, ForeignKey('people.id'))
    vehicles_id = Column(Integer, ForeignKey('vehicles.id'))
    

class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False, unique=True)
    description = Column(String(1000))
    height = Column(Integer, nullable=False)
    mass = Column(Integer, nullable=False)
    hair_color =  Column(String(100), nullable=False)
    eye_color = Column(String(100), nullable=False)
    birth_yeah = Column(String(10), nullable=False)
    gender = Column(String(10), nullable=False)
    url = Column(String(1500), nullable=False, unique=True)
    planet_id = Column(Integer, ForeignKey('planets.id'))
    vehicles_id = Column(Integer, ForeignKey('vehicles.id'))

class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False, unique=True)
    description = Column(String(1000))
    manufacturer = Column(String(500), nullable=False)
    model = Column(String(500), nullable=False)
    cost_in_credits = Column(Integer, nullable=False)
    crew = Column(Integer, nullable=False)
    planet_id = Column(Integer, ForeignKey('planets.id'))
    people_id = Column(Integer, ForeignKey('people.id'))

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planet_id = Column(Integer, ForeignKey('planets.id'))
    people_id = Column(Integer, ForeignKey('people.id'))
    vehicles_id = Column(Integer, ForeignKey('vehicles.id'))
    



# class Address(Base):
    # __tablename__ = 'address'
    # # Here we define columns for the table address.
    # # Notice that each column is also a normal Python instance attribute.
    # id = Column(Integer, primary_key=True)
    # street_name = Column(String(250))
    # street_number = Column(String(250))
    # post_code = Column(String(250), nullable=False)
    # person_id = Column(Integer, ForeignKey('person.id'))
    # person = relationship(Person)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
