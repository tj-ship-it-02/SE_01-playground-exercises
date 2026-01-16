import random

def computer_random_guess(lowest_number, highest_number):
    return random.randint(lowest_number, highest_number)

computer_choice = random.randint(1, 3)
if computer_choice == 1:
    computer_choice = "rock"
elif computer_choice == 2:
    computer_choice = "scissor"
elif computer_choice == 3:
    computer_choice = "paper"
print(computer_choice)

