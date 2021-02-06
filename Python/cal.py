
def string(s):
    d={"UPPER_CASE":0,"LOWER_CASE":0}
    for c in s:
        if c.isupper():
            d["UPPER_CASE"]+=1
        elif c.islower():
            d["LOWER_CASE"]+=1
        else:
            pass
    print("Orginal string",s)
    print("The UPPER_CASE letter is",d["UPPER_CASE"])
    print("The LOWER_CASE letter is",d["LOWER_CASE"])
s=str(input("Enter the value of string:"))
string(s)