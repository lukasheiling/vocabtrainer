import random
import sys
from time import sleep
import tkinter as tk
from tkinter import PhotoImage, messagebox
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, create_engine, text, UniqueConstraint, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from database import session, Vocab, Unit


class VocabTrainer(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("Vocabulary Trainer")
        self.unit_choice = tk.IntVar()
        self.language_choice = tk.IntVar()
        self.unit_label = tk.Label()


app = tk.Tk()
app.geometry("1200x600")
#app.configure(bg='lightblue')

app.title("Vocabulary Trainer")

welcome_label = tk.Label(text="Welcome to the vocabulary trainer!", font=(10))
welcome_label.pack(pady=10)

unit_label = tk.Label(text="Please choose the Unit (1-5)!", font=(10))
unit_label.pack(pady=2)

unit_choice = tk.IntVar()
unit_entry = tk.Entry(textvariable=unit_choice, font=(10))
unit_entry.pack(pady=2)

choose_label = tk.Label(text="Which word do you want to guess?", font=(10))
choose_label.pack(pady=2)

language_choice = tk.IntVar()
language_rb1 = tk.Radiobutton(
    text="English", variable=language_choice, value=1, font=(10))
language_rb2 = tk.Radiobutton(
    text="German", variable=language_choice, value=2, font=(10))
language_rb1.pack(pady=2)
language_rb2.pack(pady=2)


vocab_word = None
guess_var = tk.StringVar()
guessed_var = tk.StringVar()


def submit():
    unit = unit_choice.get()
    result_label.config(text=f"You have selected Unit {unit}!")

    guess_vocab_label = tk.Label(textvariable=guess_var, font=(10))
    guess_vocab_label.pack(pady=2)

    guessed_entry = tk.Entry(textvariable=guessed_var, font=(10))
    guessed_entry.pack(pady=2)

    guessed_button = tk.Button(text="Enter", command=enter, font=(10))
    guessed_button.pack(pady=2)

    correction_label = tk.Label(
        textvariable=correction, font=(10), fg='orange')
    correction_label.pack(pady=2)

    close_button.pack(pady=10)
    enter()


correction = tk.StringVar()


# when enter button is pressed
def enter():
    global vocab_word
    if vocab_word is not None:  # vocab_word is set None at the beginning, it only gets corrected if the trainee has guessed something
        if language_choice.get() == 1:

            if guessed_var.get() == vocab_word.english:
                correction.set("Correct!")
            else:
                correction.set(
                    f"Incorrect!")
        else:
            if guessed_var.get() == vocab_word.german:
                correction.set("Correct!")
            else:
                correction.set(
                    f"Incorrect!")
    
    guessed_var.set("")

    if language_choice.get() == 1:
        vocab_word = session.query(Vocab).filter(
            Vocab.unit_id == unit_choice.get()).order_by(text("RANDOM()")).first()  # selects a random word from choosen unit
        guess_var.set(f"What is the English word for {vocab_word.german}?")
    else:
        vocab_word = session.query(Vocab).filter(
            Vocab.unit_id == unit_choice.get()).order_by(text("RANDOM()")).first()
        guess_var.set(f"What is the German word for {vocab_word.english}?")
    

submit_button = tk.Button(text="Submit", command=submit, font=(10))
submit_button.pack(pady=2)

# if the unit is submitted
result_label = tk.Label(text="", font=(2), fg='green')
result_label.pack(pady=2)


# exit
def close_debugging():
    sys.exit()


close_button = tk.Button(
    text="Close", command=close_debugging, font=(10), fg='red')


app.mainloop()

root = tk.Tk()
root.withdraw()
messagebox.showinfo("Vocab Trainer Lukas Heiling",
                    "Hopefully u learned some vocabs today!")


# ouput terminal
print("Welcome to the vocabulary trainer!")
unit_choice = int(input("Enter which unit u want to learn (1 to 5): "))
print("Please choose which word u want to guess: ")
print("1. German to English")
print("2. English to German")
language_choice = int(input("Enter your choice (1 or 2): "))


# filter
for unit in Unit:
    existing_unit = session.query(Unit).filter_by(name=unit).one()

for word in Vocab:
    if session.query(Vocab).filter(Vocab.english == word[0]).count() == 0:
        session.add(Vocab(english=word[0], german=word[1], unit_id=word[2]))

# für terminal 
while True:
    # Get a random vocabulary word from the table
    if unit_choice == 1 or 2 or 3 or 4 or 5:
        vocab_word = session.query(Vocab).filter(
            Vocab.unit_id == unit_choice).order_by(text("RANDOM()")).first()
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
