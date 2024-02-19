import os
import random
import nltk

BG_GREEN = "\u001b[42m"
BG_YELLOW = "\u001b[43m"
BG_RESET = "\u001b[0m"

if os.name == 'posix':
    os.system("clear")
elif os.name == 'nt':
    os.system("cls")

word_list = nltk.corpus.words.words()
word_set = {word.lower() for word in word_list if len(word) == 5}

with open ('words.txt', 'r') as file:
    words = [word.strip() for word in file.read().split()]
correct = random.choice(words)

print("Welcome to Wordle in terminal")



for _ in range(0,6):
    guess = input("Enter a five lettered word: ")
    while not (guess in word_set):
        guess = input("Enter a valid five lettered word: ")
    for i in range(5):
        if guess[i] == correct[i]:
            print(f"{BG_GREEN}{guess[i]}{BG_RESET}", end='')
        elif guess[i] in correct:
            print(f"{BG_YELLOW}{guess[i]}{BG_RESET}", end='')
        else:
            print(f"{guess[i]}", end='')
    print()
    if guess == correct:
        print("Yay!! you have guessed the correct word.")
        exit()

print(f"All the attempts are over!\nCorrect Word is {correct}")

