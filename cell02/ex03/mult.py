num1 = int(input("Enter the first number:\n"))
num2 = int(input("Enter the second number:\n"))
mult = num1*num2
if mult > 0 :
    result = "The result is positive."
elif mult < 0:
    result = "The result is negative."
else :
    result = "The result is positive and negative"
print(f"{num1} x {num2} ={mult}")
print(result)