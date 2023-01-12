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


# Add some vocabulary words to the table
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
session.commit()

import random

while True:
    # Get a random vocabulary word from the table
    vocab_word = session.query(Vocab).order_by(text("RANDOM()")).first()
    if language_choice == 1:
        # Print the German word and prompt the trainee to guess the English translation
        print("German:", vocab_word.german)
        guess = input("What is the English translation? ")

        # Check if the trainee's guess is correct
        if guess == vocab_word.english:
            print("Correct!")
        else:
            print("Incorrect. The correct answer is", vocab_word.english)

        cont = input("Do you want to continue? (y/n) ")
        if cont.lower() != "y":
            break
    else: 
        # Print the German word and prompt the trainee to guess the English translation
        print("English:", vocab_word.english)
        guess = input("What is the German translation? ")

        # Check if the trainee's guess is correct
        if guess == vocab_word.german:
            print("Correct!")
        else:
            print("Incorrect. The correct answer is", vocab_word.german)

        cont = input("Do you want to continue? (y/n) ")
        if cont.lower() != "y":
            break

