# to find the factorial of a number
def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)


num = int(input("Enter the number to find factorial:"))
print("The factorial of", num, "is", fact(num))
