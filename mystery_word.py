import random


def open_file(file):
    # opening the file in read mode
    with open(file) as my_file:
        # reading the file
        data = my_file.read()
        format_data = data.split()
        random_word = random.choice(format_data)
        rw_list = list(random_word)
        blanks = [' _ '] * len(random_word)
        print(random_word)
        print(rw_list)
    return blanks


print(open_file('words.txt'))


# open('test-word.txt')
# print(read_file)


# def play_game():
# random_word = random.choice(format_data)
# return random_word


#     word =
#     wrong_guesses = []
#     right_guesses = []

# game_board = ''
# for letter in word:
#     if letter in right_guesses:
#         game_board += letter + ' '
#     else:
#         game_board += '_ '
# print(game_board)


# if __name__ == "__main__":
#     play_game()
