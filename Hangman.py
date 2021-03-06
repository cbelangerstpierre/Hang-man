import os
import string


def game():
    os.system("clear")

    # asking if the user want to play again
    def play_again():
        answer = input("Do you want to play again ?\n")
        if answer.lower() == "yes":
            os.system("clear")
            game()
        elif answer.lower() == "no":
            print("\nHope you had fun !\n\nEnd of the game.")
            quit()
        else:
            print("\n\nPlease answer by yes or no")
            play_again()

    # getting the word the user want his friend to discover
    def get_word():
        word_input = input(
            'Write down the word that needs to be discovered without the other person seeing it !\n').lower()
        if len(word_input) == 0:
            game()
        elif word_input == "quit":
            quit()
        for each_letter in word_input:
            if each_letter not in string.ascii_lowercase[:26]:
                game()
        return word_input

    word = get_word()

    # Start of the game, rules
    def game_initializer():
        print(f"""You have 5 lives to guess the word chosen. 
Each time you choose a letter that 
isn't part of the word you will lose a life. 
The word have {len(word)} letters.
Good luck !\n\n""")

    os.system("clear")
    game_initializer()

    lives_remaining = 5
    letters_chosen = ""
    current_word_progress = "_ " * len(word)

    # Print different messages concerning the number of lives the user have
    def lives_print():
        if lives_remaining > 1:
            print(f"You have {lives_remaining} lives left.\n")
        else:
            print(f"You only have {lives_remaining} life left.\n")

    # Print every letters the user already have tried
    def letters_chosen_print():
        if letters_chosen == "":
            print("You haven't tried any letter yet\n\n")
        else:
            print(f"Here's every letters you already tried :\n{letters_chosen}\n\n")

    # Print what the user already have discover about the word
    def current_word_progress_print():
        print(current_word_progress, '\n')

    # Each time the user try a new letter, it will be added with this function
    def change_letters_chosen(letter_input):
        if letters_chosen == "":
            new_letters_chosen = letter_input
        else:
            new_letters_chosen = letters_chosen + f", {letter_input}"
        return new_letters_chosen

    # Each time the user guess a correct letter, it will be added with this function
    def change_current_word_progress(letter_input):
        indices = []
        new_current_word_progress = list(current_word_progress)
        for i in range(len(word)):
            if word[i] == letter_input:
                indices.append(i)
        for index in indices:
            new_current_word_progress[index * 2] = letter_input
        new_current_word_progress = "".join(new_current_word_progress)
        return new_current_word_progress

    # This function print everything that the user need to know before guessing again
    def action():
        lives_print()
        letters_chosen_print()
        current_word_progress_print()

    # This loop until the user win or lose
    while lives_remaining > 0 and "_" in current_word_progress:
        action()
        letter = input("Which letter do you want to pick ?\n\n")
        if letter == "quit":
            quit()
        elif len(letter) == 1 and letter not in list(letters_chosen) and letter in string.ascii_lowercase[:26]:
            letters_chosen = change_letters_chosen(letter)
            if letter in word:
                current_word_progress = change_current_word_progress(letter)
            else:
                lives_remaining -= 1
        os.system("clear")

    # If the user lose
    if lives_remaining == 0:
        print(f"""You lost...
The word you had to find was \"{word}\".
Maybe you can try again.""")
        play_again()

    # If the user win
    if "_" not in current_word_progress:
        print(f"""You win !!!
You successfully found the word \"{word}\" !
Maybe you could try and win another game.""")
        play_again()


game()
