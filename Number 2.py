num1 = int(input("Enter 1st Digit: "))
num2 = int(input("Enter 2nd Digit: "))
num3 = int(input("Enter 3rd Digit: "))

if num1 >= num2 and num1 >= num3:
    print(num1)
elif num2 >= num1 and num2 >= num3:
    print(num2)
else:
    print(num3)
