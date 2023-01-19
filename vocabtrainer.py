import random
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, create_engine, text, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create a SQLite database file called "vocab.db"
engine = create_engine('sqlite:///vocab.db')
Base = declarative_base()

# Define tables
class Vocab(Base):
    __tablename__ = 'vocab'
    id = Column(Integer, primary_key=True)
    english = Column(String)
    german = Column(String)

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

print("Welcome to the vocabulary trainer!")
unit_choice = int(input("Enter which unit u want to learn (1 to 5): "))
print("Please choose which word u want to guess: ")
print("1. German to English")
print("2. English to German")
language_choice = int(input("Enter your choice (1 or 2): "))

# create a session 
session = create_session()

# list of units
units = ['UNIT 1','UNIT 2','UNIT 3','UNIT 4','UNIT 5']

for unit in units:
    try:
        existing_unit = session.query(Unit).filter_by(name=unit).one()
        print(f"Unit {unit} already exists in the database")
    except NoResultFound:
        session.add(Unit(name=unit))
        print(f"Unit {unit} added to the database")

session.commit()
# close the session
session.close()


session.add(Unit(name='UNIT 1'))
session.add(Unit(name='UNIT 2'))
session.add(Unit(name='UNIT 3'))
session.add(Unit(name='UNIT 4'))
session.add(Unit(name='UNIT 5'))



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
        # Print the English word and prompt the trainee to guess the German translation
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