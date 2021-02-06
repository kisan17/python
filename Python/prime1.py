def prime(num):
    if num>1:
        for i in (2,num):
            if num%i==0:
                print("Not a prime number:")
            else:
                print(" prime number:")
            break
    else:
        print("Not a prime number:")
    
num=int(input("Enter the value of number:"))
prime(num)
