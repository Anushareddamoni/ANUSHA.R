#calculation program
#input:num1,num2,operation
#output:perform the operation on the inputs

num1 = float(input("Give 1st Number: "))
num2 = float(input("Give 2nd Number: "))
operator = input("Give operator: ")

if(operator == "+"):
    print(f"Addition of two numbers is: {num1+num2}")
elif(operator == "-"):
    print(f"Subtraction of two numbers is: {num1-num2}")
elif(operator == "*"):
    print(f"Multiplication of two numbers is: {num1*num2}")
elif(operator == "/"):
    print(f"Division of two numbers is: {num1/num2}")
else:
    print("operator not found")                
