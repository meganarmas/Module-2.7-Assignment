def safe_addition():
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            return num1 + num2
        except:
            print("Enter only numbers")


while True:
    result = safe_addition()
    print(f"The sum is {result}")

    continue_input = input("Would you like to perform another addition? (yes/no): ")
    if continue_input != 'yes':
        break

