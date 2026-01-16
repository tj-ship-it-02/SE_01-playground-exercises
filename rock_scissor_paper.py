import random

def random_number_within_range(lowest_number, highest_number):
  return random.randint(lowest_number, highest_number)

def rsp_game():
    player_choice = input("Rock, Scissor or Paper? ")
    computer_choice = random_number_within_range(1, 3)
    if computer_choice == 1:
        computer_choice = "rock"
    elif computer_choice == 2:
        computer_choice = "scissor"
    elif computer_choice == 3:
        computer_choice = "paper"
    print("You chose: " + player_choice + " and the computer chose: " + str(computer_choice) + " meaning the winner is...")
    if player_choice == "rock" and computer_choice == "scissor":
        winner = "YOU!"
    elif player_choice == "scissor" and computer_choice == "paper":
        winner = "YOU!"
    elif player_choice == "paper" and computer_choice == "rock":
        winner = "YOU!"
    elif player_choice == "rock" and computer_choice == "paper":
        winner = "the computer"
    elif player_choice == "scissor" and computer_choice == "rock":
        winner = "the computer"
    elif player_choice == "paper" and computer_choice == "scissor":
        winner = "the computer"
    elif player_choice == "rock" and computer_choice == "rock":
        winner = "NOBODY"
    elif player_choice == "scissor" and computer_choice == "scissor":
        winner = "NOBODY"
    elif player_choice == "paper" and computer_choice == "paper":
        winner = "NOBODY"
    print(winner)


rsp_game()
rsp_game()
rsp_game()
