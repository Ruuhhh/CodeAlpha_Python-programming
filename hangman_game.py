import random
import Hangman_stages
import word_file
#word_list = ["apple", "beautiful", "potato"]
lives = 6
chosen_word = random.choice(word_file.words)
print(chosen_word)   # for debugging

# create blanks
display = []
for i in range(len(chosen_word)):
    display += "_"
print(display)

game_over = False

while not game_over:
    guessed_letter = input("Guess a letter: ").lower()

    # check guessed letter in word
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guessed_letter:
            display[position] = guessed_letter

    print(display)

    # wrong guess
    if guessed_letter not in chosen_word:
        lives -= 1
        print(f"Wrong! Lives left: {lives}")
        if lives == 0:
            game_over = True
            print("You lose!!")

    # check if won
    if "_" not in display:
        game_over = True
        print("You win!!")
    print(Hangman_stages.stages[lives])
