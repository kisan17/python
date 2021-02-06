def  multiply(numbers):
    total=1
    for i in numbers:
        total*=i
    return total

n=multiply((8,2,3,4))
print("The multiply of these numbers is",n)