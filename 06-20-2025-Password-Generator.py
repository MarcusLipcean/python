import random
n = int(input("How many caraters does your password want to have? "))
s = ''
for i in range(1, n):
    c = random.randint(33, 126)
    s+=chr(c)
print("This is your password:",s)
