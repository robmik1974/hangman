import random
import hangman_art

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

lives = 6

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

display = list()
for _ in range(len(chosen_word)):
    display.append("_")

end_of_the_game = False

while not end_of_the_game:

    guess = input("Guess a letter: ").lower()
    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if guess == letter:
                display[index] = letter
    else:
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
