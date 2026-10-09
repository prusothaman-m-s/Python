# if statements

num = int(input("Enter a number :"))
if num >=18:
    print("your eligible for vote")

# if else statements

number = int(input("Enter a number :"))
if number % 3 == 0 and number % 5 == 0:
    print("whether it is divisible by 3 and 5")
else:
    print("whether it is not divisible by 3 and 5")

num = int(input("enter a number :"))
if num % 2 == 0:
    print("even")
else:
    print("odd")

#if elseif else statements

num = int(input("Enter a number :"))
if num <= 30:
    print("Poor student")
elif num > 30 and num < 70:
    print("Average student")
elif num > 70 and num <= 100:
    print("Good student")
else:
    print("Invalid input")

#

score = int(input("Enter your score : "))
if score >= 70:
    print("Your eligible")
    name = input("Enter your name : ")
    age = int(input("Enter your age : "))
    location = input("Enter your location : ")
    print("Name = ",name)
    print("Age = ",age)
    print("Location = ",location)
else:
    print("Your not eligible")

# nested if else statements

salary = int(input("Enter your salary : "))
age = int(input("Enter your age : "))
if salary >= 20000 or age <= 25:
    lone = int(input("Enter your lone : "))
    if lone >=100000:
        print("maximum lone amout is 100000")
    else:
        print("you can get loan amount = ",lone)
else:
    print("Your not eligible for the loan")

#

tamil = int(input())
english = int(input())
maths = int(input())
science = int(input())
social = int(input())
sum = tamil+english+maths+science+social
avg = sum/5
print("Your total score = " , sum)
print("Your average score = ",avg)
if avg < 35:
    print("Additional class for required")
else:
    print("You are good to go")   

# for loop

a = 10
for i in range(a):
    print(i) 

a = 10
for i in range(a):
    if i%2 == 0:
        print("Even",i)
    else:
        print("Odd",i)


e_count = 0
o_count = 0
for i in range(1,11):
    if i%2 == 0:
        e_count = e_count+1
    else:
        o_count = o_count+1
print("count of even numbers =" ,e_count)
print("count of odd numbers =" ,o_count)


count = 0
for i in range(1,100):
    if i % 3 == 0 and i % 5 == 0:
        count = count+1
        print(i)
print(count)


a = []
print('Enter 10 numbers')
for i in range(10):
    a.append(int(input(f"Enter a number {str(i+1)}")))

print(a)
sum = 0
for i in a:
    sum = sum+i
print("total :",sum)
avg = sum/10
print("average :",avg)

#for loop cube code

n = int(input("enter a number : "))
print(f"the first {n} natural number is : ")
for i in range(1,n+1):
    print(f"cube of {i} is = {i*i*i}")

#for nested loop

for i in range(1,6):
    print("week :",i)
    for j in range(1,4):
        print(" ","day :",j)
    for k in range(1,3):
        print(".... .. ....")

# use for loop for pattern prints
for i in range(1,6):
    print('*'*(i))