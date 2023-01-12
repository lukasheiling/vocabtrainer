import random

vocab = {
    "car": "auto",
    "goodbye": "tschuess",
    "please": "bitte",
    "thank you": "danke"
}

while True:
    # Choose a random vocabulary word
    word = random.choice(list(vocab.keys()))
    ger_word = vocab[word]

    # Ask the user to provide the definition
    guess = input("What is the german word for " + word + "? ")

    # Check if the guess is correct
    if guess.lower() == ger_word.lower():
        print("Correct!")
    else:
        print("Incorrect. The correct word is: " + ger_word)
