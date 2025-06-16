#This program is a number card game between two players
#I used random module because it generates random numbers for the program to fill the players decks
import random
ordine = 0
player1 = True
player2 = True
a1 = [0 for i1 in range(0, 13)]
for i1 in range(0, 12):
    a1[i1] = random.randint(2, 13)
a2 = [0 for i2 in range(1, 13)]
for i2 in range(0, 12):
    a2[i2] = random.randint(2, 13)
a1 = sorted(a1)
a2 = sorted(a2)
print("1 Player:",a1,"\n","2 Player:",a2,"\n")
ho1 = 1
ho2 = 2
while player1 != False or player2 != False:
    print(ho1," Player: ")
    card1 = int(input("Put a card from your deck: (1, 2, 3 ... 13)"))
    print(ho2," Player: ")
    yes_no = str(input("Can you beat that number with a higher number from your deck? (Yes, No)"))
    if yes_no == 'Yes':
        print(ho2," Player: ")
        card2 = int(input("Put a higher number than the first player: "))
        if card1 != card2:
            print(ho2," Player: ")
            print("You have beat his card!")
            ordine = a2.index(card2)
            del a2[ordine]
            ordine = a1.index(card1)
            del a1[ordine]
    else:
        if ho2 == 2:
            player2 = False
            print("The winner is...player number 1!!!")
            break
        else:
            player1 = False
            print("The winner is...player number 2!!!")
            break
    print("The remaining cards: ")
    print(a1,"\n",a2)
    ho1 = ho2
