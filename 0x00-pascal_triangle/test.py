array = int(input("Enter a number: "))
for i in range(0, array):
    x = 1
    for j in range(1, array - i):
        print("  ", end="")

    for k in range(0, i + 1):
        print("  ", x, end="")
        x = int(x * (i-k) / (k + 1))
    print()
