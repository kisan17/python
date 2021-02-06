#we can clone a list into another list using Slicing.
a=[10,20,30,40,50,60]
b=a[:]

print("A:",a)
print("B:",b)
print()
print("Modifying  A:")
a[3]=45
print("A:",a)
print("B:",b)

print("Modifying B:")
b[4]=55
print("A:",a)
print("B:",b)