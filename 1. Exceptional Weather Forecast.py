# Objective: The aim of this assignment is to 
# enhance your understanding of exception handling by 
# creating a weather forecast application that gracefully handles 
# unexpected user input and provides user-friendly error messages.

# Task 1: Start Begin by asking the user to enter 
# the temperature in Fahrenheit.

# Task 2: Temperature Conversion Write a 
# function that converts the Fahrenheit temperature to Celsius. 
# Remember that the formula is (Fahrenheit - 32) * 5/9.

# Use a try block to catch any potential errors 
# during the conversion process. What happens if they 
# type out "thirty" instead of doing 30?

# Task 3: User Experience Implement an else block 
# that prints the converted temperature in a user-friendly format. 
# Example: "100 degrees Fahrenheit is 37.78 degrees Celsius."


# Task 4: Finally Add a finally block that 
# thanks the user for using the weather forecast 
# application, ensuring that this message is displayed 
# regardless of whether an exception was caught or not.


def forecast():
        try:    
            faren_temp = int(input("Enter the current temperature in Fahrenheit: "))
            result = (faren_temp - 32) * 5/9
        except ValueError:
            print("Please enter a number in numerical format.")
        else:
            print(f"The temperature in Celsius is {result:.2f} degrees.")
        finally:
            print("Thank you for the use of our app!")

forecast()