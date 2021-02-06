
x=[101,102,103,104,105,106,107,108]
print("Orginal list",x)
n=len(x)
print(n)
for i in range(n):
    print(i,"=",x[i])


print("From 1st position to 4th position:")
a=x[1:5]
print(a)

print()

print("from 2nd position to 5th position:")
b=x[1:6]
print(b)
print()


print("From 5th position  to last position")
c=x[5:]
print(c)
print()

print("from 0th position to 6th position")
d=x[:7]
print(d)
print()

print("'From 0th positon to 5th position  leaving 2 steps")
e=x[0:6:2]
print(e)
print()



print("Counting the elements in list:")
num=x.count
print(num)


