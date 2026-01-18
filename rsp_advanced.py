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

def determine_round_winner(computer_choice, player_choice):
    if player_choice == computer_choice:
        print("NOBODY won, it's a tie.")
        return "tie"
    elif (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissor" and computer_choice == "paper") or \
         (player_choice == "rock" and computer_choice == "scissor"):
        print("YOU WON!!")
        return "player"
    else:
        print("The computer won..")
        return "computer"



def calculate_scoring_board(result, player_score, computer_score):
    if result == "player":
        player_score = player_score + 1
        print("THE SCORE BOARD IS:")
        print("Player Score: " + str(player_score))
        print("Computer Score: " + str(computer_score))
        return player_score, computer_score
    elif result == "computer":
        computer_score = computer_score + 1
        print("THE SCORE BOARD IS:")
        print("Player Score: " + str(player_score))
        print("Computer Score: " + str(computer_score))
        return player_score, computer_score
    else:
        print("THE SCORE BOARD IS:")
        print("Player Score: " + str(player_score))
        print("Computer Score: " + str(computer_score))
        return player_score, computer_score


def run_rsp_game():
    player_score = 0
    computer_score = 0

    while True:
        computer_choice = get_computer_choice()
        print(computer_choice)
        player_choice = player_choice_validation()
        result = determine_round_winner(computer_choice, player_choice)
        player_score, computer_score = calculate_scoring_board(result, player_score, computer_score)

        if player_score >= 3:
            print("The finale winner is: YOU!!")
            break
        elif computer_score >= 3:
            print("The finale winner is: The computer :(")
            break

run_rsp_game()
    


