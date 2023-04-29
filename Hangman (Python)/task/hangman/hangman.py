import random
import string

def replace_letter(word, hint, letter_guess):
    indexes = []
    aux_hint = list(hint)
    for i, letter in enumerate(word):
        if letter == letter_guess:
            indexes.append(i)
    for index in indexes:
        aux_hint[index] = letter_guess
    return ''.join(aux_hint)


def test_input(letter):
    result = True
    if len(letter) != 1:
        result = False
        print("Please, input a single letter.")
    else:
        if letter not in string.ascii_lowercase:
            result = False
            print("Please, enter a lowercase letter from the English alphabet.")
    return result


def play(words):
    random.seed()
    selected_word = random.choice(words)
    set_selected_word = set(selected_word)
    hint = len(selected_word) * "-"
    guesses = set()
    attempts = 0
    won = False
    while attempts < 8 and not won:
        print("")
        print(hint)
        user_letter = input("Input a letter:")
        if test_input(user_letter):
            if user_letter not in guesses:
                guesses.add(user_letter)
                if user_letter in set_selected_word:
                    hint = replace_letter(selected_word, hint, user_letter)
                    if hint == selected_word:
                        won = True
                else:
                    print("That letter doesn't appear in the word.")
                    attempts += 1
            else:
                print("You've already guessed this letter.")
    print("")
    if won:
        print(f"You guessed the word {selected_word}!")
        print("You survived!")
    else:
        print("You lost!")
    return won

print("H A N G M A N")
words = ["python", "java", "swift", "javascript"]
wins = 0
losses_ = 0
exit_ = False
while not exit_:
    print('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
    options = frozenset({"play", "results", "exit"})
    user_opt = "0"
    while user_opt not in options:
        user_opt = input()
    if user_opt == "play":
        result = play(words)
        if result:
            wins += 1
        else:
            losses_ += 1
    elif user_opt == "results":
        s_string = "s"
        if wins == 1:
            s_string = ""
        print(f"You won: {wins} time{s_string}")
        s_string = "s"
        if losses_ == 1:
            s_string = ""
        print(f"You lost: {losses_} time{s_string}")
    else:
        exit_ = True


