# --- IMPORTS ---
from random import randint
# ---------------

# `options[input]` to go from name to integer id
options = {
    "rock": 0,
    "paper": 1,
    "scissors": 2
}

# Generate computer's choice
computer = randint(0,2)

#Take user input
user = -1
while True:
    userOption = input("Rock, Paper, or Scissors?").lower()
    #turn input into integer id
    if userOption in options:
        user = options[userOption]
        break
    else:
        print("invalid input")

print(user)

#See who wins

dif = (computer - user) % 3 #0: Draw, 1: computer, 2: user

#Evaluate a draw
if dif == 0:
    print("Its a draw!")
