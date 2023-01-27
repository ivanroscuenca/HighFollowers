
from art import logo, vs

from game_data import data

import random

from replit import clear 

""" take the account data and returns in printable format"""

def format_data(account):
  account_name = account['name']
  account_descr = account['description']
  account_country = account['country']
  return(f"{account_name} a {account_descr} from {account_country}")        

##Use if statement to check if user is correct and returns if its right
def check_answer(guess,a_followers,b_followers):
  if a_followers>b_followers:
    return guess=='a'
  else:
    return guess=='b'

print(logo)
score=0
game_continue=True
account_b=random.choice(data)

  #make game repeatable
while game_continue:
  
  #generate random account
  #making position at position b become next account at position A
  account_a=account_b
  account_b=random.choice(data)
  if account_a==account_b:
    account_b=random.choice(data)
  
  
  
  #Print values
  
  print(f"Compare A: {format_data(account_a)}")
  
  print(vs)
  print(f"Against B: {format_data(account_b)}")
  
  #ask for a guess
  guess=input("Who has more followers? Type 'A' or type 'B':").lower()
  
  #check if user is correct
  ##get follower count of each account_a
  
  a_follower_count= account_a['follower_count']
  b_follower_count= account_b['follower_count']
  
  is_correct = check_answer(guess,a_follower_count,b_follower_count)
  #clear the screen
  clear()
  print(logo)
  
  #give user feedback on their guess
  #score keeping
  
  if is_correct:
    print("You're right")
    score+=1
    print(f"Current score is {score}")
  else:
    game_continue=False
    print("Sorry, that's wrong")
    print(f"Final score is {score}")

    


