import random
print("Welcome to our rock paper scissors game!")
print("If you wish to quit type 'quit' into the console")
while True:
    player_choice = input("Please enter your choice from rock, paper or scissors. ")

    if player_choice.lower() == "quit" or player_choice.lower() == "q":
      print("Thank you so much for playing our game")
      break

    computer_choice = random.randint(1,3)
    if computer_choice == 1:
        print("You chose " + player_choice + ", I chose rock")
    if computer_choice == 2:
        print("You chose " + player_choice + ", I chose paper")
    if computer_choice == 3:
        print("You chose " + player_choice + ", I chose scissors")