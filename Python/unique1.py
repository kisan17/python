def  unique_list(l):
    x=[]
    for a in l:
        if a not in x:
            x.append(a)
    print(x)
    

unique_list([1,2,3,4,5,6,7,2,3,4,5])