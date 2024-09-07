
print("Welcome to our rock paper scissors game!")
while True:
    player_choice = input("Please enter your choice from rock, paper or scissors. ")

    if player_choice.lower() == "rock" or player_choice.lower() == "r":
        print('Chosen rock')

    elif player_choice.lower() == "paper" or player_choice.lower() == "p":
        print('Chosen paper')

    elif player_choice.lower() == "scissors" or player_choice.lower() == "s":
        print('Chosen scissors')

    else:
        print('please choose a valid input')        