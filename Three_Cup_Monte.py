from  random import shuffle

# Shuffeling the cups

ball_under_cup = ['','O','']

# shuffled_board = shuffle(ball_under_cup)

def shuffle_board(ball_under_cup):
    shuffle(ball_under_cup)
    return ball_under_cup

mixed_position = shuffle_board(ball_under_cup)

# Taking a guess from the user

def user_guess():

    ball_position = ['0','1','2']
    guess = ""
    while guess not in ball_position :
        guess = input("Guess the number from 0 or 1 or 2 where the ball might be in: ")
    return int(guess)

player_choice = user_guess()
print(f"Your choice is {player_choice}")


# Comparing Values

def verify_guess (mixed_position,player_choice):
    if mixed_position [player_choice] == "O":
        print ("Correct!")
    else:
        print("Wrong Guess.")
        print (ball_under_cup)


verify_guess (ball_under_cup,player_choice)