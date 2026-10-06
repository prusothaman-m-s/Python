num1 = int(input("Enter a number:"))
num2 = int(input("Enter a number:"))
oprater = input("Enter an operator (+,-,*,/,%):")
if (oprater == "+"):
    print(num1+num2)
elif (oprater == "-"):
    print(num1-num2)
elif (oprater == "*"):
    print(num1*num2)
elif (oprater == "/"):
    print(num1/num2)
elif (oprater == "%"):
    print(num1 % num2)
else:
    print("Invalid operator")
