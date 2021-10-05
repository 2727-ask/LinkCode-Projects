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
    