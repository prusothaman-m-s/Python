try:
    num1 = int(input("Enter number: "))
    num2 = int(input("Enter divisor: "))
    result = num1 / num2  # Could cause ZeroDivisionError or ValueError
except ZeroDivisionError:
    print("Error: You cannot divide a number by zero!")
except ValueError:
    print("Error: Please input whole numbers only.")
else:
    print("Division successful! Result is:", result)
finally:
    print("Calculation attempt finished.")  # Always executes
