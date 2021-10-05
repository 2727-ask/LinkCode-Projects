flag = 1
while (flag != '0'):
    print("-----------DS PROGRAM INITIATED---------")
    print("Enter A for Pascals Triangle")
    print("Enter B for TWO SUM")
    print("Enter 0 to exit")
    choice = input("Enter Your Choice")
    print("----------------------------------------")
    if (choice == "A"):
        n = int(input("Enter Number"))
        for x in range(n):
            print(" " * (n - x), end="")
            print(" ".join(map(str, str(11 ** x))))
            # Two Sum
    if (choice == "B"):
        print("-------Welcome to Two Sum Program--------")
        arr = []
        count = int(input("Enter Number of elements in Array"))
        for x in range(count):
            no = int(input("Enter Number"))
            arr.append(no)
        print("Array is :", arr)
        target = int(input('Enter Target'))
        hashmap = {}
        for x, y in enumerate(arr):
            diff = target - y
            if (diff in hashmap):
                print('Indices are', [hashmap[diff], x])
            hashmap[y] = x
    if (choice == "0"):
        flag = "0"

    