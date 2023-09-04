import random
import hangman_art
import hangman_words
import os

os.system('clear')
word_list = hangman_words.word_list
chosen_word = random.choice(word_list)

lives = 6

print(hangman_art.logo)

display = list()
for _ in range(len(chosen_word)):
    display.append("_")

end_of_the_game = False

while not end_of_the_game:

    guess = input("Guess a letter: ").lower()

    os.system('clear')

    if guess in display:
        print(f"You have already guessed the letter '{guess}', try agin")

    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if guess == letter:
                display[index] = letter
    else:
        print(f"You guessed '{guess}', that's not in the the word, you lose a life")
        lives -= 1
        if lives == 0:
            end_of_the_game = True

    print(" ".join(display))
    print(hangman_art.stages[lives])

    if end_of_the_game:
        print("You lose")
    elif "_" not in display:
        end_of_the_game = True
        print("You win!")
