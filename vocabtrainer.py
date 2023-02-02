"""import random
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, create_engine, text, UniqueConstraint, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker"""
import random
from time import sleep
import tkinter as tk
from tkinter import messagebox
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

#tkinter
class VocabTrainer(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("Vocabulary Trainer")
        self.geometry("1200x600")

        self.unit_choice = tk.IntVar()
        self.language_choice = tk.IntVar()

        self.unit_label = tk.Label()


app = tk.Tk()
app.title("Vocabulary Trainer")

welcome_label = tk.Label(text="Welcome to the vocabulary trainer!")
welcome_label.pack()

unit_choice = tk.IntVar()
unit_entry = tk.Entry(textvariable=unit_choice)
unit_entry.pack()

language_choice = tk.IntVar()
language_rb1 = tk.Radiobutton(text="German to English", variable=language_choice, value=1)
language_rb2 = tk.Radiobutton(text="English to German", variable=language_choice, value=2)
language_rb1.pack()
language_rb2.pack()

vocab_word = None
guess_var = tk.StringVar()
guessed_var = tk.StringVar()
def submit():
    unit = unit_choice.get()
    #language = language_choice.get()
    result_label.config(text=f"You have selected Unit {unit}")

    guess_vocab_label = tk.Label(textvariable=guess_var)
    guess_vocab_label.pack()

    guessed_entry = tk.Entry(textvariable=guessed_var)
    guessed_entry.pack()

    guessed_button = tk.Button(text="Enter", command=enter)
    guessed_button.pack()
    enter()

def enter():
    global vocab_word
    if vocab_word is not None:
        if guessed_var.get() == vocab_word.german:
            print("Correct!")
        else:
            print("False!")

    vocab_word = session.query(Vocab).filter(Vocab.unit_id == unit_choice.get()).order_by(text("RANDOM()")).first()
    guess_var.set(f"What is the German word for {vocab_word.english}")

    

submit_button = tk.Button(text="Submit", command=submit)
submit_button.pack()

result_label = tk.Label(text="")
result_label.pack()


app.mainloop()

root = tk.Tk()
root.withdraw()
messagebox.showinfo("Vocab Trainer Lukas Heiling", "Hopefully u learned some vocabs today!")

#ouput console
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

# filter die units 
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
