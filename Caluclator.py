import math

def scientific_calculator():
    print("Welcome to the scientific calculator!")
    print("Please select an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square root")
    print("6. Logarithm")
    print("7. Trigonometry")
    print("8. Exponentiation")
    print("9. Factorial")
    print("10. Combination")
    print("11. Permutation")
    
    operation = input("Enter operation number: ")
    
    if operation == "1":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 + num2
        print("Result: ", result)
        
    elif operation == "2":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 - num2
        print("Result: ", result)
        
    elif operation == "3":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 * num2
        print("Result: ", result)
        
    elif operation == "4":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 / num2
        print("Result: ", result)
        
    elif operation == "5":
        num = float(input("Enter a number: "))
        result = math.sqrt(num)
        print("Result: ", result)
        
    elif operation == "6":
        num = float(input("Enter a number: "))
        base = float(input("Enter the logarithm base: "))
        result = math.log(num, base)
        print("Result: ", result)
        
    elif operation == "7":
        angle = float(input("Enter an angle in degrees: "))
        radian = math.radians(angle)
        print("sin({0}) = {1}".format(angle, math.sin(radian)))
        print("cos({0}) = {1}".format(angle, math.cos(radian)))
        print("tan({0}) = {1}".format(angle, math.tan(radian)))
        
    elif operation == "8":
        base = float(input("Enter the base: "))
        exponent = float(input("Enter the exponent: "))
        result = math.pow(base, exponent)
        print("Result: ", result)
        
    elif operation == "9":
        num = int(input("Enter a non-negative integer: "))
        result = math.factorial(num)
        print("Result: ", result)
        
    elif operation == "10":
        n = int(input("Enter the number of items: "))
        r = int(input("Enter the number of items to choose: "))
        result = math.comb(n, r)
        print("Result: ", result)
        
    elif operation == "11":
        n = int(input("Enter the number of items: "))
        r = int(input("Enter the number of items to choose: "))
        result = math.perm(n, r)
        print("Result: ", result)
        
    else:
        print("Invalid operation number. Please try again.")
        
    choice = input("Would you like to perform another operation? (y/n): ")
    if choice == "y":
        scientific_calculator()
    else:
        print("Thank you for using the scientific calculator!")
        
scientific_calculator()
