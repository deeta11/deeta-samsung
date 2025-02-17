import math
num=int(input("Enter a positive number:"))
root=math.sqrt(num)
if root.is_integer():
    print("perfect square")
else:
    print("Not perfect sqaure")