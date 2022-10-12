from RPSLS_player import RPSLS_player
import random

class P15007(RPSLS_player):
  def __init__(self):
    self.hand = ["rock", "scissors", "paper", "lizard", "spock"]

  def shoot(self):
    i = random.randint(0, 4)

    return self.hand[i]
  
  def update(self, result: str, competitor_shot: str):
    pass