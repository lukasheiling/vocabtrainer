import random
import sys
from time import sleep
import tkinter as tk
from tkinter import PhotoImage, messagebox
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, create_engine, text, UniqueConstraint, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///vocab.db')
Base = declarative_base()

class Vocab(Base):
    __tablename__ = "vocab"
    id = Column(Integer, primary_key=True)
    unit_id = Column(Integer, ForeignKey('unit.id'))
    english = Column(String, unique=True)
    german = Column(String, unique=True)
    __table_args__ = (UniqueConstraint(
        'english', name='uq_english'), UniqueConstraint('german', name='uq_german'))

class Unit(Base):
    __tablename__ = "unit"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    __table_args__ = (UniqueConstraint('name', name='uq_name'), )


# Create the vocabulary table in the database
Base.metadata.create_all(bind=engine)

# Start a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

session = Session()

def add_vocabs():
    session.add(Unit(name='UNIT 1'))
    session.add(Unit(name='UNIT 2'))
    session.add(Unit(name='UNIT 3'))
    session.add(Unit(name='UNIT 4'))
    session.add(Unit(name='UNIT 5'))
    
    session.add(Vocab(english='cat', german='Katze', unit_id=1))
    session.add(Vocab(english='dog', german='Hund', unit_id=1))
    session.add(Vocab(english='book', german='Buch', unit_id=2))
    session.add(Vocab(english='house', german='Haus', unit_id=3))
    session.add(Vocab(english='pig', german='Schwein', unit_id=4))
    session.add(Vocab(english='correct', german='richtig', unit_id=5))
    session.add(Vocab(english='mother', german='Mutter', unit_id=1))
    session.add(Vocab(english='father', german='Vater', unit_id=5))
    session.add(Vocab(english='siblings', german='Geschwister', unit_id=5))
    session.add(Vocab(english='red', german='Rot', unit_id=4))
    session.add(Vocab(english='green', german='Grün', unit_id=1))
    session.add(Vocab(english='blue', german='Blau', unit_id=3))
    session.add(Vocab(english='bird', german='Vogel', unit_id=5))
    session.add(Vocab(english='cow', german='Kuh', unit_id=2))
    session.add(Vocab(english='tree', german='Baum', unit_id=2))
    session.add(Vocab(english='twenty', german='Zwanzig', unit_id=5))
    session.add(Vocab(english='apple', german='Apfel', unit_id=3))
    session.add(Vocab(english='pillow', german='Polster', unit_id=5))
    session.add(Vocab(english='good', german='gut', unit_id=5))
    
if __name__ == "__main__":
    add_vocabs()
    session.commit()
    session.close()