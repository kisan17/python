def test(num):
    if num>1:
        count=0
        for i in range(2,num):
            if num%i==0:
                count+=1
                print("Not a prime Number:")
                break
            elif(count==2):
                print("Prime Number:")
                break
        
    else:
        print("Not a prime Number:")

num=int(input("Enter the value of num:-"))
test(num)

        









