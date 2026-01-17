import random

def get_user_input():
    while True:
        choice = input("select rock (1) paper (2) scissors (3) >: ")
        if choice in ['1', '2', '3']:
            return int(choice)
        print("Invalid choice, try again!")

def get_computer_choice(A,B):
    return random.randint(A, B)

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    if (user == 1 and computer == 3) or (user == 2 and computer == 1) or (user == 3 and computer == 2):
        return "user"
    return "computer"

def play_round(round_num):
    print(f"\n--- Round {round_num} ---")
    user = get_user_input()
    computer = get_computer_choice(1, 3)
    choices = {1: "rock", 2: "paper", 3: "scissors"}
    print(f"You: {choices[user]}, Computer: {choices[computer]}")
    return determine_winner(user, computer)

def main():
    scores = {"user": 0, "computer": 0, "tie": 0}
    for round_num in range(1, 4):
        result = play_round(round_num)
        scores[result] += 1
        print(f"Winner: {result if result != 'tie' else 'Tie'}")
    
    print(f"\n=== Final Score ===")
    print(f"You: {scores['user']}, Computer: {scores['computer']}, Ties: {scores['tie']}")

main()

----

while True:
      if user_guess == computer_guess:
        print("You are goddamn rightttt, my number was " + computer_guess + ".")
        break
      if user_guess > computer_guess:
        print("Your number is too high, try again: ")
        continue
      if user_guess < computer_guess:
        print("Your number is too low, try again: ")
        continue



def user_number_guess():
  while True:
    user_guess = input("Guess my number, it's between 1 and 10: ")
    if not user_guess.isnumeric():
      print("You can't write text, give me a number: ")
    else:
      return int(user_guess)


def run_game():
    user_number_guess()
    if user_guess == computer_guess:
      print("You are goddamn rightttt, my number was " + computer_guess + ".")

run_game()
