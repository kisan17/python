def check(num):
    for num in range(p,n):
        print(" Congrats number is found!!")
        break

    else:
        print("Sorry number not found in this range:")
    

num=int(input("Enter the value of num:-"))
p=int(input("Enter the value of p:-"))
n=int(input("Enter the value of n:-"))
check(num)