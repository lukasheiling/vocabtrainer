import random
from sqlalchemy import text
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create a SQLite database file called "vocab.db"
engine = create_engine('sqlite:///vocab.db')
Base = declarative_base()

# Define a vocabulary table with columns for English and German words
class Vocab(Base):
    __tablename__ = 'vocab'
    id = Column(Integer, primary_key=True)
    english = Column(String)
    german = Column(String)

# Create the vocabulary table in the database
Base.metadata.create_all(bind=engine)

# Start a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

print("Welcome to the vocabulary trainer!")
print("Please choose a language to learn:")
print("1. German to English")
print("2. English to German")
language_choice = int(input("Enter your choice (1 or 2): "))


# Add vocabulary words to the table
session.add(Vocab(english='cat', german='Katze'))
session.add(Vocab(english='dog', german='Hund'))
session.add(Vocab(english='book', german='Buch'))
session.add(Vocab(english='house', german='Haus'))
session.add(Vocab(english='pig', german='Schwein'))
session.add(Vocab(english='correct', german='richtig'))
session.add(Vocab(english='mother', german='Mutter'))
session.add(Vocab(english='father', german='Vater'))
session.add(Vocab(english='siblings', german='Geschwister'))
session.add(Vocab(english='red', german='Rot'))
session.add(Vocab(english='green', german='Grün'))
session.add(Vocab(english='blue', german='Blau'))
session.add(Vocab(english='bird', german='Vogel'))
session.add(Vocab(english='cow', german='Kuh'))
session.add(Vocab(english='tree', german='Baum'))
session.add(Vocab(english='twenty', german='Zwanzig'))
session.add(Vocab(english='apple', german='Apfel'))
session.commit()