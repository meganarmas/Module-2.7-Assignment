def divider(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Division by zero is not allowed"

while True:
    try:
        numberator = float(input("Enter the numerator: "))
        denom = float(input("Enter the other one: "))
        result = divider(numberator, denom)
        print(f"The result of division is {result}")
    except ValueError:
        print("Please enter numbers")
    continuous_input = input("Would you like to perform another?").lower()
    if continue_input != 'yes':
            break

