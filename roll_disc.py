import random

min_val=1
max_val=6

roll_again='yes'

while roll_again == 'yes' or roll_again == 'y':
    print("Rolling the Dices")
    print("The value are :")

    print(random.randint(min_val, max_val))

    print(random.randint(min_val, max_val))

    #asking the user to roll the dice again.
    roll_again=input("Roll the Dices Again ?")

