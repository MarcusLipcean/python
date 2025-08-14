#This is the game 3 in 3, the rules are: every player writes a number in ascending order until somebody writes a number that divides 3 without remainder the game is over 
print("Welcome in the 3 in 3 game!")
number = int(input("Write the number: "))
b = True
while b:
    if number % 3 == 0:
        print("Game Over!")
        break
    number = int(input("Write the number: ")) 
        
