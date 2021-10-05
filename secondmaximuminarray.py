print("Hello World")
arr = []
n = int(input("Enter Number of Elements in array"))
for i in range(n):
    no = int(input("Enter Number"))
    arr.append(no)

first = 0
second = 0

for x in arr:
    if(first<x):
        second = first
        first = x
    elif(second<x and x!=first):
        second = x
print('Second Largest Element in Array is',second)

