def prime(num):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                print("Not a prime number:")
                break
        else:
            print("Is a prime Number:")


    else:
        print("Not a Prime Number" )


num=int(input("Enter the value of num:-"))
prime(num)




