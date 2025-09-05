n=int(input("Enter the value of n: "))
for i in range(n):
    for j in range(n - i): #Adding Blank spaces
        print(" ", end="")
    for j in range(i+1): #Adding stars
        print("*", end="")
    print()
