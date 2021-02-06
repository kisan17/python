def string(str):
    reversed_string=""
    for i  in str:
        reversed_string=i+reversed_string
    print("Reversed_string",reversed_string)

str=input("Enter the string:-")
string(str)
