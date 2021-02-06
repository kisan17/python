def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)

n=int(input("Enter the value of n:-"))
a=fact(n)
print("The factorial of n is:",a)

    