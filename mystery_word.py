import random


def open_file_start_game(file):
    # opening the file in read mode and choosing a random word
    with open(file) as my_file:
        # reading the file
        data = my_file.read()
        format_data = data.split()
        random_word = random.choice(format_data)
        rw_as_list = list(random_word)
        blanks = [' _ '] * len(random_word)
    return rw_as_list, blanks


def play_game():
    word, underscores = open_file_start_game('words.txt')
    print(' '.join(underscores))
    wrong_guesses = []
    difficulty = input(
        'What kind of challenge do you prefer? Type Hard, Medium or Easy: ')
    if difficulty == 'Hard':
        guesses = 8
        len(word) >= 8
    elif difficulty == 'Medium':
        guesses = 8
        len(word) >= 6 and len(word) < 8
    elif difficulty == 'Easy':
        guesses = 8
        len(word) < 6
    else:
        print('Invalid Entry')
    while guesses > 0:
        user_guess = input("Guess a letter! ")
        print('user_guess: ', user_guess)
        if user_guess in wrong_guesses:
            print('Already guessed that! Try again!')
            guesses += 0
        elif user_guess in underscores:
            print('Already guessed that! Try again!')
            guesses += 0
        elif user_guess in word:
            guesses -= 1
            for i in range(len(word)):
                if user_guess == word[i]:
                    underscores[i] = user_guess
        else:
            wrong_guesses.append(user_guess)
            guesses -= 1
        print('Answer: ', ' '.join(underscores))
        print('wrong guesses: ', wrong_guesses)
        print('Guesses remaing: ', guesses)
        if underscores == word:
            print('YOU WON! The answer is: ', ' '.join(word))
            break
        if guesses == 0:
            print('OUT OF GUESSES! The correct answer was ', ' '.join(word))
            break
    play_again = input('Do you want to play again Yes or No? ')
    if play_again == 'Yes':
        play_game()
    else:
        print('Okay BYE!')


if __name__ == "__main__":
    play_game()
