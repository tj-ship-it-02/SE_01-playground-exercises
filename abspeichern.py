# This code will generate a random number:
import random

def random_number_within_range(lowest_number, highest_number):
  return random.randint(lowest_number, highest_number)

# 👇 Add your code below:

def run_game(question, correct_answer, start_range, end_range):
  game_1_player_choice = int(input("Guess a number between " + str(start_range) + " and " + str(end_range))
  game_1_computer_choice = random.randint(start_range, end_range)
  print("The computer chose " + str(game_1_computer_choice) + "and the player chose" + str(game_1_player_choice))

run_game("How high is Mount Everest in meters?", 8849, 0, 10000)


def guess_distance_to_mount_everest():
  correct_answer = int("8449")
  print("First one: guess how many meters to my Mount Everest?")
  user_guess = int(input())
  computer_guess = random_number_within_range(100, 10000)
  print("The computer guessed:")
  print(computer_guess)
  user_answer_distance = (correct_answer - user_guess)
  print("The user's distance to the correct answer is: ")
  print(user_answer_distance)
  computer_answer_distance = (correct_answer - computer_guess)
  print("The computer's distance to the correct answer is: ")
  print(computer_answer_distance)
  if abs(user_answer_distance) < abs(computer_answer_distance):
    print("The winner is YOU!!!")
  elif abs(computer_answer_distance) < abs(user_answer_distance):
    print("The winner is the computer...")


def guess_distance_to_bathroom():
  correct_answer = int("12")
  print("Okaaay second guess... How many meters to the bathroom?")
  user_guess = int(input())
  computer_guess = random_number_within_range(1, 100)
  print("The computer guessed:")
  print(computer_guess)
  user_answer_distance = (correct_answer - user_guess)
  print("The user's distance to the correct answer is: ")
  print(user_answer_distance)
  computer_answer_distance = (correct_answer - computer_guess)
  print("The computer's distance to the correct answer is: ")
  print(computer_answer_distance)
  if abs(user_answer_distance) < abs(computer_answer_distance):
    print("The winner is YOU!!!")
  elif abs(computer_answer_distance) < abs(user_answer_distance):
    print("The winner is the computer...")


def guess_distance_to_home():
  correct_answer = int("3100")
  print("Aaaaand last guess... How many meters to my home?")
  user_guess = int(input())
  computer_guess = random_number_within_range(100, 10000)
  print("The computer guessed:")
  print(computer_guess)
  user_answer_distance = (correct_answer - user_guess)
  print("The user's distance to the correct answer is: ")
  print(user_answer_distance)
  computer_answer_distance = (correct_answer - computer_guess)
  print("The computer's distance to the correct answer is: ")
  print(computer_answer_distance)
  if abs(user_answer_distance) < abs(computer_answer_distance):
    print("The winner is YOU!!!")
  elif abs(computer_answer_distance) < abs(user_answer_distance):
    print("The winner is the computer...")

guess_distance_to_mount_everest()
guess_distance_to_bathroom()
guess_distance_to_home()










