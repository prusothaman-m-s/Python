# calculater using if elseif else statements
a = int(input("Enter a number :"))
b = int(input("Enter a number :"))
oprater = input("Enter an oprater :")
if oprater == "+":
    print(a+b)
elif oprater == "-":
    print(a-b)
elif oprater == "*":
    print(a*b)
elif oprater == "/":
    print(a/b)
elif oprater == "%":
    print(a%b)
else:
    print("Invalid oprater")