import random
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, create_engine, text, UniqueConstraint, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create a SQLite database file called "vocab.db"
engine = create_engine('sqlite:///vocab.db')
Base = declarative_base()

# Define tables
class Vocab(Base):
    __tablename__ = 'vocab'
    id = Column(Integer, primary_key=True)
    unit_id = Column(Integer, ForeignKey('unit.id'))
    english = Column(String, unique=True)
    german = Column(String, unique=True)
    __table_args__ = (UniqueConstraint('english', 'german', name='uq_english_german'), )
    

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
session = Session()

# list of units
unit_list = ['UNIT 1','UNIT 2','UNIT 3','UNIT 4','UNIT 5']

# list of vocabs
words_to_add = [('cat', 'Katze', 1), ('dog', 'Hund', 1), ('book', 'Buch', 2), ('house', 'Haus', 3), 
('pig', 'Schwein', 4), ('correct', 'richtig', 5), ('mother', 'Mutter', 1), ('father', 'Vater', 5), 
('siblings', 'Geschwister', 5), ('red', 'Rot', 4), ('green', 'Grün', 1), ('blue', 'Blau', 3), 
('bird', 'Vogel', 5), ('cow', 'Kuh', 2), ('tree', 'Baum', 2), ('twenty', 'Zwanzig', 5), ('apple', 'Apfel', 3)]


for unit in unit_list:
    existing_unit = session.query(Unit).filter_by(name=unit).one()

for word in words_to_add:
    if session.query(Vocab).filter(Vocab.english == word[0]).count() == 0:
        session.add(Vocab(english=word[0], german=word[1], unit_id=word[2]))

# Add vocabulary words to the table
"""session.add(Vocab(english='cat', german='Katze', unit_id=1))
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
session.add(Vocab(english='apple', german='Apfel', unit_id=3))"""

session.commit()
session.close()


while True:
    # Get a random vocabulary word from the table
    if unit_choice == 1 or 2 or 3 or 4 or 5:
        vocab_word = session.query(Vocab).filter(Vocab.unit_id == unit_choice).order_by(text("RANDOM()")).first()
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

