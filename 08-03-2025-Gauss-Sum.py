s = 0
print("Enter the first and last numbers in the Gauss sum.")
first = int(input("First number: "))
last = int(input("Last number: "))
if last%2==0:
    s = (first + last) * (last / 2)
    print(s)
else:
    s = (first + last - 1) * ((last - 1 )/ 2) + last
    print(s)
