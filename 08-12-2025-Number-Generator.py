#This program generates you a number with how many figures you want
import random
k = 0
number = 0
n = int(input("How many figures do you want for our number? "))
for i in range(1, n):
    k = k + 1
    if k == 1:
        figure = random.randint(1, 9)
    else:
        figure = random.randint(0, 9)
    number = number * 10 + figure
print("This is your number: ",number)
