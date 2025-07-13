import random
number = 0
number_think = random.randint(1, 100)
while number != number_think:
    number = int(input("Guess the number, from 1 to 100: "))
    if number == number_think:
        break
    elif number > number_think:
        if number - number_think >= 25:
            print("You are very cold.")
        elif number - number_think >= 15:
            print("You are cold.")
        elif number - number_think <=10 and number - number_think >= 5:
            print("You are hot")
        else:
            print("You are very hot.")
    else:
        if number_think - number >= 25:
            print("You are very cold.")
        elif number_think - number >= 15:
            print("You are cold.")
        elif number_think - number <=10 and number_think - number >= 5:
            print("You are hot")
        else:
            print("You are very hot.")
print("Winner!!!")
   
