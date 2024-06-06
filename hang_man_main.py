import random
import words_listing
import stages

chosen_word = random.choice(words_listing.word_list).lower()
# print(f"The chosen word is {chosen_word}")

display = []
word_length = len(chosen_word)
lives = 6

for _ in chosen_word:
    display += "_"
print(display)

end_of_game = False

while not end_of_game:
    guess = input("Guess a word: ")

    if guess in display:
        print(f"You've Already Guessed the word {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(display)

    if guess not in chosen_word:
        lives -= 1
        if lives == 5:
            print(f"Your guessed word '{guess}' is wrong , So yo losed a Life...")
        elif lives == 4:
            print(f"Your guessed word '{guess}' is wrong , So yo losed a Life...")
        elif lives == 3:
            print(f"Your guessed word '{guess}' is wrong , So yo losed a Life...")
        elif lives == 2:
            print(f"Your guessed word '{guess}' is wrong , So yo losed a Life...")
        elif lives == 1:
            print(f"Your guessed word '{guess}' is wrong , So yo losed a Life...")
        if lives == 0:
            end_of_game = True
            print(f"The chosen word is: {chosen_word}")
            print("You Lose")

    if "_" not in display:
        end_of_game = True
        print("You Win")

    print(stages.stage[lives])




