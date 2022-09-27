import random

def get_choices():
  player_choice = input(" Enter the choice ( rock, paper, scissors) : ")
  computer_choice = random.choice(["paper", "rock", "scissors"])
  choices = {"player": player_choice, "computer": computer_choice}
  return choices

def check_win(player, computer):
  print(f"You chose {player}, computer chose {computer}")
  if player == computer:
    return "it's a tie!!!"
  elif player == "rock":
    if computer == "scissors":
      return "Rock smashes scissor. You Win!!! "
    else:
      return "Paper covers rock. You Loose!"
  elif player == "paper":
    if computer == "rock":
      return "Paper covers rock. You win!"
    else:
      return "Scissor cuts paper. You loose! "
  elif player == "scissors":
    if computer == "paper":
      return "Scissor cuts paper. You win! "
    else:
      return "Rock smashes scissor. You lose!!! "

choices = get_choices()
print(check_win(choices["player"], choices["computer"]))