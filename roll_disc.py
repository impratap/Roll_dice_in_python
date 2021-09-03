import random

roll_again='yes'

while roll_again == 'yes' or roll_again == 'y':
    print("Rolling the Dices")
    print("The value are :")

    print(random.randint(1,6))

    print(random.randint(1,6))

    #asking the user to roll the dice again.
    roll_again=input("Roll the Dices Again ?")

