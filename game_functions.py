
# function to be used by game_1: Guess the Number
def pick_value(poss_values):
    len_value_list = len(poss_values)
    
    x=poss_values[(round(len_value_list/2))]
    
    return x
    
# function to be used in game_2: Higher or Lower
def check_higher_lower(current_val, next_val, user_input):
    if next_val > current_val and user_input == 'h':
        return True 
    elif next_val < current_val and user_input == 'l':
        return True 
    else: 
        return False
    

# function to be used in game_3: Hangman
def process_guess(letter, board, word):
    word_length= len(word)
    word_list = list(word)
    for i in range(word_length) :
        if letter == word_list[i]:
            board[i] = letter
    if letter in board:
        print("The letter " + letter+" is in the word")
        return True
    else:
        return False
        print("The letter " + letter+" is not in the word")
