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