a=[10,20,30,40,50,60]
b=a.copy()
print("A",a)
print("B",b)
print()
#changing element  in A doesnot change  the element of B.
print("Modifying A:")
a[2]=35
print("A:",a)
print("B:",b)
print()
#changing element  in B doesnot change  the element of A.
print("Modifying B:")
b[3]=45
print("A:",a)
print("B:",b)
print()


