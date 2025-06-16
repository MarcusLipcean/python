#This program helps players roll the dice in Monopoly.
#I used random module to generate random numbers.
import random
k = 0
yes_no='Yes'
while yes_no != 'No':
    for k in range(1,3):
        number1 = random.randint(1,6)
        number2 = random.randint(1,6)
        print(number1 ,"  ", number2 ," sum = ", number1+number2)
        if number1 != number2:
            break
        else:
            print("Double!")
            k = k+1
            if k == 3:
                print("Go at the jail!")
                break
    yes_no = str(input("Do you want to continue the game? (Write Yes or No)"))
