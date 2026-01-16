import random

# 👇 Add your code below:

def computer_random_number(lowest_number, highest_number):
  return random.randint(lowest_number, highest_number)

computer_guess = random.randint(1, 10)
print(computer_guess)

counter = 0

def user_number_guess():
  while True:
    user_guess = input("Guess my number, it's between 1 and 10: ")
    if not user_guess.isnumeric():
        print("Fookin hell, you need to guess a number, not text.")
    else:
      break
  return int(user_guess)


while True:
  user_guess = user_number_guess()
  counter = counter + 1
  if user_guess > computer_guess:
    print("Your number is too high, try again: ")
  elif user_guess < computer_guess:
    print("Your number is too low, try again: ")
  else:
    print("You are goddamn right, it's: " + str(computer_guess))
    print("Your score is:")
    print(counter * -1)
    break


