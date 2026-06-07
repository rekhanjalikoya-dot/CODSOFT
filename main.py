#calculator
while True:
           num1 = float(input("Enter first number: "))
           num2 = float(input("Enter second number: "))
           operation = input("Enter operation (+, -, *, /): ")
           if operation == "+":
              result = num1 + num2
           elif operation == "-":
             result = num1 - num2
           elif operation == "*":
              result = num1 * num2
           elif operation == "/":
             if num2 != 0:
               result = num1 / num2
             else:
               result = "Error: Division by zero"
           else:
               result = "Error: Invalid operation"
           print("Result:", result)
           again = input("Do you want to perform another calculation? (yes/no): ")
           if again.lower() != "yes":
            break
print("Thank you for using the calculator!")

