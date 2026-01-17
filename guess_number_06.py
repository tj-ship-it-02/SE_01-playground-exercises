import random

# 👇 Add your code below:

def random_number_within_range(lowest_number, highest_number):
  return random.randint(1, 10)

computer_guess = random.randint(1, 10)

user_tries_counter = 0

while True: 
  user_guess = int(input("Guess my number brev: "))
  user_tries_counter = user_tries_counter + 1
  if user_guess > computer_guess:
    print("Your number is too high!")
    
  if user_guess < computer_guess:
    print("Your number is too low!")
    
  if user_guess == computer_guess:
    print("You are goddamn right!!")
    print("Your score is: " + str(user_tries_counter * -1))
    break



