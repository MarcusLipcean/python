i = 3
a = 0
b = 1
c = 1
print("Enter how many numbers you want.")
many = int(input("How many: "))
print(a,"  ",b,"  ",c,"  ",end="")
while i != many:
    i = i + 1
    c = a + b
    a = b
    b = c
    print(c,"  ",end="")
