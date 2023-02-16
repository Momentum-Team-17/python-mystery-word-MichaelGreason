def open_file(file):
    # opening the file in read mode
    with open(file) as my_file:
        # reading the file
        data = my_file.read()
        format_data = data.split()
    return format_data


print(open_file('words.txt'))


# open('test-word.txt')
# print(read_file)

# def choose_random_word():
#     random_word = random.choice(open)
#     print(random_word)


# def play_game():

# open_file('words.txt')


#     word =
#     wrong_guesses = []
#     right_guesses = []

#     game_board = ''
#     for letter in word:
#         if letter in right_guesses:
#             game_board += letter + ' '
#         else:
#             game_board += '_ '
#     print(game_board)


# if __name__ == "__main__":
#     play_game()
