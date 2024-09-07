import random
print("Welcome to our rock paper scissors game!")
print("If you wish to quit type 'quit' into the console")
while True:
    player_choice = input("Please enter your choice from rock, paper or scissors. ")

    if player_choice.lower() == "quit" or player_choice.lower() == "q":
      print("Thank you so much for playing our game")
      break

    if player_choice.lower() == "rock" or player_choice.lower() == "r":
        print('Chosen rock')

    elif player_choice.lower() == "paper" or player_choice.lower() == "p":
        print('Chosen paper')

    elif player_choice.lower() == "scissors" or player_choice.lower() == "s":
        print('Chosen scissors')

    else:
        print('please choose a valid input')  
        continue      

    computer_choice = random.randint(1,3)
    if computer_choice == 1:
        print("You chose " + player_choice + ", I chose rock")
    if computer_choice == 2:
        print("You chose " + player_choice + ", I chose paper")
    if computer_choice == 3:
        print("You chose " + player_choice + ", I chose scissors")
