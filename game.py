import random

# This is the game of rock, paper, scissors
# We have the user playing against the computer
# So we gonna define the user and computer instructions

def game():
    user = input("Choose an option: 'ro' for Rock, 'pp' for Paper and 'ss' for Scissors\n").lower()
    computer = random.choice(['ro', 'pp', 'ss'])

# Game instruccions:
# Scissors wins against papper (ss > pp)
# Rock wins against scissors (ro > ss)
# Paper wins against rock (pp > ro)

    if user == computer:
        return 'Tie!'

    if ((user == 'ss' and computer == 'pp')
    or (user == 'ro' and computer == 'ss')
    or (user == 'pp' and computer == 'ro')):
        return 'You win!'

    else:
        return 'You lose!'

print(game())