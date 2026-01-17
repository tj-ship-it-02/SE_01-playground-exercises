import random

def computer_random_guess(lowest_number, highest_number):
    return random.randint(lowest_number, highest_number)

print("Welcome, my friend. It's a rsp game - first to win 3 rounds!")

def get_computer_choice():
    random_number = random.randint(1, 3)
    if random_number == 1:
        return "rock"
    elif random_number == 2:
        return "scissor"
    elif random_number == 3:
        return "paper"

def player_choice_validation():
    while True:
        player_choice = input("Rock, Scissor or Paper? ")
        if player_choice != "rock" and player_choice != "scissor" and player_choice != "paper":
            print("You can only choose 'rock', 'scissor' or 'paper'. Nothing else, try again.")
        else:
            break
    return player_choice

def determine_winner(computer_choice, player_choice):
    if player_choice == computer_choice:
        return "tie"
    elif (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissor" and computer_choice == "paper") or \
         (player_choice == "rock" and computer_choice == "scissor"):
        return "player"
    else:
        return "computer"

player_score = 0
computer_score = 0

def scoring_board(result):
    if result == "player":
        player_score == player_score + 1
    if result == "computer":
        computer_score == computer_score + 1




def run_rsp_game():
    computer_choice = get_computer_choice()
    print(computer_choice)
    player_choice = player_choice_validation()

    result = determine_winner(computer_choice, player_choice)

    if result == "tie":
        print("NOBODY won, it's a tie.")
    elif result == "player":
        print("YOU WON!!")
    else:
        print("The computer won..")
    



run_rsp_game()

#print(computer_choice)
#print(player_choice)


# if player_choice == computer_choice:
#         print("TIES! Nobody won.")
#     elif player_choice == "paper" and computer_choice == "rock":
#         print("YOU WON!!")
#     elif player_choice == "rock" and computer_choice == "scissor":
#         print("YOU WON!!")
#     elif player_choice == "scissor" and computer_choice == "paper":
#         print("YOU WON!!")
#     elif player_choice == "paper" and computer_choice == "scissor":
#         print("The computer won...")
#     elif player_choice == "rock" and computer_choice == "paper":
#         print("The computer won...")
#     elif player_choice == "scissor" and computer_choice == "rock":
#         print("The computer won...")