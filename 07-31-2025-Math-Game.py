import random
print("Welcome in the math game of quizzes!")
how_many = int(input("How many questions do you want?"))
for i in range(1, how_many+1):
    semn = random.randint(1, 4)
    number1 = random.randint(1,100)
    number2 = random.randint(1, number1)
    if(semn==1):
        print("How much is: ",number1," + ",number2)
        rez = int(input("Your guess: "))
        real_rez = number1 + number2
        if(rez==real_rez):
            print("Correct!")
        else:
            print("Sorry but the real guess is: " + str(real_rez))
    elif(semn==2):
        print("How much is: ",number1," - ",number2)
        rez = int(input("Your guess: "))
        real_rez = number1 - number2
        if(rez==real_rez): 
            print("Correct!")
        else:
            print("Sorry but the real guess is: " + str(real_rez))
    elif(semn==3):
         print("How much is: ",number1," : ",number2)
         rez = float(input("Your guess: "))
         real_rez = number1 / number2
         if(rez==real_rez):
            print("Correct!")
         else:
            print("Sorry but the real guess is: " + str(real_rez))
    elif(semn==4):
         print("How much is: ",number1," x ",number2)
         rez = int(input("Your guess: "))
         real_rez = number1 * number2
         if(rez==real_rez):
            print("Correct!")
         else:
            print("Sorry but the real guess is: " + str(real_rez))
    
