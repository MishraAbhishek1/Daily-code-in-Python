# # import re


# # def get_choicces():
# #   player_choice = "rock"
# #   comoputer_choice = "paper"
# #   return player_choice, comoputer_choice
# # resposne = get_choicces()
# # print(resposne)

# # def greeting():
# #   return "HI"

# # resposne = greeting()
# # print(resposne)
  

  
  
  
# def get_choices():
#   player_choice = "rock"
#   computer_choice = "paper"
#   choices = {"player": player_choice, "computer": computer_choice}
#   return choices
# response = get_choices()
# print(response)
import random
def get_choices():
  player_choice = input("Enter a choice (rock, paper, scissors: ")
  options = ["rock", "paper", "scissors"]
  computer_choice = random.choice(options)
  choices = {"player": player_choice, "computer": computer_choice}
  return choices
# message = get_choices()
# print(message)

# def check_win(player_choice, computer_choice):
#   if player_choice == computer_choice:
#     return "Match is Tie -> again play"
#   elif player_choice != computer_choice:
#     return "Match is Tie -> again play"  
#   # return [player_choice, computer_choice] 

def check_win(player, computer):
  print(f"You chose {player}, computer chose {computer}")
  if player == computer:
    return "Match is Tie -> again play"
  # elif player == "rock" and computer == "scissors":
  #   return "Rock smashes scissors! You win!"
  # elif player == "paper" and computer == "rock":
  #   return "Paper covers rock! You win!"
  # elif player == "scissors" and computer == "paper":
  #   return "Scissors cuts paper! You win!"
  # elif player == "rock" and computer == "paper":
  #   return "Paper covers rock! You lose."
  elif player == "rock":
    if computer == "scissors":
      return "Rock smashes scissors! You Win!"
    else:
      return "Papers covers rock! You Lose!"

  elif player == "paper":
    if computer == "rock":
      return "Papers Covers rock! You Win!"
    else:
      return "Papers covers rock! you Lose!"

  elif player == "scissors":
    if computer == "paper":
      return "Scissors cuts paper! You Win!"
    else:
      return "Scissors! cuts paper You Lose"

choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)