# row_1 = ['','','']
# row_2 = ['','','']
# row_3 = ['','','']

# def display(row1,row2,row3):
#     print(row1)
#     print(row2)
#     print(row3)


# output = display(row_1,row_2,row_3)

# def user_choice():
#     while True:
#         choice = input("Please use a valid input between 0 to 9: ")

#         if choice.isdigit():
#             choice = int(choice)
#             if choice in range(10):
#                 return choice
#             else:
#                 print("Print a number between 0 to 9. ")
#         else:
#             print("Invalid input. Digits only allowed.")

# user_choice()

def position_choice():
    while True:
        choose_position = input("Choose to place your number in which position, choose either from 0 or 1 or 2: ")

        if choose_position not in ['0','1','2']:
            print("Invalid input. Try again.")
            continue
        final_value = int(choose_position)
        return final_value

position_choice()

from xoboard import xo_board
print(xo_board)


# def replacement_value(game_list,position):
