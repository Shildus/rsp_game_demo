import random
print("Welcome to our rock paper scissors game!")
while True:
    player_choice = input("Please enter your choice from rock, paper or scissors. ")
    print(player_choice)
    computer_choice = random.randint(1,3)
    if computer_choice == 1:
        print("You chose " + player_choice, "I chose rock")
    if computer_choice == 2:
        print("You chose " + player_choice, "I chose paper")
    if computer_choice == 3:
        print("You chose " + player_choice, "I chose scissors")