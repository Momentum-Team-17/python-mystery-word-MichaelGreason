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
        # print(rw_as_list)
    return rw_as_list, blanks


def play_game():
    word, underscores = open_file_start_game('words.txt')
    print(word, underscores)
    answer = []
    wrong_guesses = []
    user_guess = input("Guess a letter! ")
    print('user_guess: ', user_guess)
    if user_guess in word:
        for i in range(len(word)):
            if user_guess == word[i]:
                underscores[i] = user_guess
    else:
        wrong_guesses.append(user_guess)
    print('Answer: ', underscores)
    print('wrong guesses: ', wrong_guesses)


# game_board = ''
# for letter in word:
#     if letter in right_guesses:
#         game_board += letter + ' '
#     else:
#         game_board += '_ '
# print(game_board)
if __name__ == "__main__":
    play_game()
