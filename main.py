import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

display = list()
for _ in range(len(chosen_word)):
    display.append("_")

guess = input("Guess a letter: ").lower()
for index, letter in enumerate(chosen_word):
    if guess == letter:
        display[index] = letter

print(display)
