num1 = int(input("Please enter a number: "))

num2 = num1
counter = 0
small = 9
high = 0

while num2 > 0:
    digit = num2 % 10
    num2 //= 10
    counter += 1
    if digit < small:
        small = digit
    if digit > high:
        high = digit

print("The number of digits in the given number is: ", counter)
print("Smallest number is: ", small)
print("Highest number is: ", high)

